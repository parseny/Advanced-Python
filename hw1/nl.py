import sys
import click


@click.command()
@click.argument("file", required=False, default='', type=click.Path())
def nl(file):
    """"""
    cnt = 1
    if file:
        with open(file, 'r') as f:
            for line in f:
                click.echo(f"{cnt}  {line}", nl=False)
                cnt += 1
        f.close()
    else:
        try:
            for line in sys.stdin:
                click.echo(f"{cnt}  {line}", nl=False)
                cnt += 1
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    nl()
