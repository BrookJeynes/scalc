from scalc import cli, __app_name__, __version__

def main():
    cli.app(prog_name=__app_name__, version=__version__)

if __name__ == '__main__':
    main()