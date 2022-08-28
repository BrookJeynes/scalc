from operator import ge
import typer
import math

from scalc import __settings__
from scalc.callbacks import _version_callback
from scalc.generate_table import generate_table
from scalc.validate_ip import validate_ip

app = typer.Typer(add_completion=False)

@app.command()
def main(
  version: bool = typer.Option(None, '--version', '-v', help='Show version.', callback=_version_callback),
    ip_address: str = typer.Argument(..., help='IP address.'),
      slash_notation: int = typer.Option(__settings__.default_settings['slash_notation'], '--slash-notation', '-sn', help='Slash notation.'),
        subnets: int = typer.Option(__settings__.default_settings['subnets'], '--subnets', '-s', help='Number of subnets.'),
          # host_id_bits: int = typer.Option(__settings__.default_settings['host_id_bits'], '--host-id-bits', '-hid', help='Number of host id bits.'),
            output_format: str = typer.Option(__settings__.output_settings['output_format'], '--output-format', '-of', help=f'Output format. Supported formats: {", ".join(__settings__.output_settings["supported_output_formats"])}'),
):
  host_id_bits = __settings__.default_settings['host_id_bits']
  borrowed_bits: int =  math.ceil(math.log(subnets, 2))
  IP_address_per_subnet: int = int(math.pow(2, host_id_bits - borrowed_bits))

  # If the user specified a slash notation, use it.
  if slash_notation > 24:
    host_id_bits = 8 - (slash_notation - 24)
    borrowed_bits = 8 - host_id_bits
    IP_address_per_subnet = int(math.pow(2, host_id_bits))
  else:
    slash_notation = slash_notation + borrowed_bits

  subnets_needed: int = int(math.pow(2, borrowed_bits))

  # TODO: Possibly move these to an error checking function?
  if output_format not in __settings__.output_settings['supported_output_formats']:
    raise typer.BadParameter('Unsupported output format.')
  else:
    __settings__.output_settings['output_format'] = output_format

  if not validate_ip(ip_address):
    raise typer.BadParameter('Invalid IP address.')

  if slash_notation < 24 or slash_notation > 32:
    raise typer.BadParameter('Slash notations smaller than 24 and greater than 32 are not yet supported / are invalid.')
  
  for i in range(256+IP_address_per_subnet):
    if i % IP_address_per_subnet == 0 and i - IP_address_per_subnet >= 0:
      __settings__.output_table['Network Address'].append(f'`{ip_address[0:-1]}{i-IP_address_per_subnet}`')
      __settings__.output_table['Slash Notation'].append(f'/{slash_notation}')
      __settings__.output_table['First Usable IP Address'].append(f'`{ip_address[0:-1]}{int((i-IP_address_per_subnet)+1)}`')
      __settings__.output_table['Last Usable IP Address'].append(f'`{ip_address[0:-1]}{int(i-2)}`')
      __settings__.output_table['Broadcast Address'].append(f'`{ip_address[0:-1]}{int(i-1)}`')

  generate_table(subnets_needed)
