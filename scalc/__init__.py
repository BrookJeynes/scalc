class Settings():
  def __init__(self) -> None:
    self.default_settings = {
      'subnet_mask': '255.255.255.0',
      'slash_notation': '24',
      'host_id_bits': '8',
      'subnets': '2'
    }

__settings__ = Settings()
__app_name__ = 'Subnetting Calculator'
__version__ = '0.1.0'