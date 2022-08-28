import pandas as pd
from scalc import __settings__

def generate_table(subnets: int) -> None:
  output_table = pd.DataFrame(
      data=__settings__.output_table, 
      index=pd.RangeIndex(
        start=1, 
        stop=(subnets+1), 
        name='Subnet')
    )

  if __settings__.output_settings['output_format'] == 'terminal':
    print(output_table.to_markdown())
