class Settings():
  def __init__(self) -> None:
    self.default_settings = {
      'subnet_mask': '255.255.255.0',
      'slash_notation': 24,
      'host_id_bits': 8,
      'subnets': 1
    }

    self.output_settings = {
      'supported_output_formats': ['terminal'], # TODO: Add more supported types: 'md', 'csv'
      'output_format': 'terminal',
      'output_file': 'output',
      'output_directory': './' # TODO: Let user choose directory
    }

    self.output_table = {
      'Network Address': [],
      'Slash Notation': [],
      'First Usable IP Address': [],
      'Last Usable IP Address': [],
      'Broadcast Address': [],
    }

__settings__ = Settings()
__app_name__ = 'Subnetting Calculator'
__version__ = '0.1.0'