import typer
import math

from scalc import __settings__
from scalc.callbacks import _version_callback

app = typer.Typer(add_completion=False)

@app.command()
def main(
  version: bool = typer.Option(None, '--version', '-v', help='Show version.', callback=_version_callback),
    ip_address: str = typer.Argument(..., help='IP address.'),
      slash_notation: int = typer.Option(__settings__.default_settings['slash_notation'], '--slash-notation', '-sn', help='Slash notation.'),
        subnets: int = typer.Option(__settings__.default_settings['subnets'], '--subnets', '-s', help='Number of subnets.'),
          host_id_bits: int = typer.Option(__settings__.default_settings['host_id_bits'], '--host-id-bits', '-hid', help='Number of host id bits.'),
):
  subnet_count = 0
  output_string = '| Subnet | Network Address | Slash Notation | First Usable IP Address | Last Usable IP Address | Broadcast Address |\n|-|-|-|-|-|-|'

  borrowed_bits: int =  math.ceil(math.log(subnets, 2))
  IP_address_per_subnet: int = int(math.pow(2, host_id_bits - borrowed_bits))

  if slash_notation != 24:
    raise typer.BadParameter('Slash notations smaller or greater than 24 are not yet supported.')
  
  for i in range(256+IP_address_per_subnet):
    if i % IP_address_per_subnet == 0 and i - IP_address_per_subnet >= 0:
      subnet_count += 1
      output_string += f'\n| {subnet_count} | `{ip_address[0:-1]}{i-IP_address_per_subnet}` | `/{slash_notation+borrowed_bits}` | `{ip_address[0:-1]}{int((i-IP_address_per_subnet)+1)}` | `{ip_address[0:-1]}{int(i-2)}` | `{ip_address[0:-1]}{int(i-1)}` |'

  print(f'\n{output_string}')
