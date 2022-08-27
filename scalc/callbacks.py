import typer
from scalc import __settings__, __app_name__, __version__

def _version_callback(value: bool) -> None:
  if value:
    typer.echo(f'{__app_name__} {__version__}')
    raise typer.Exit()
