import sys
import click


def tail_file(filename, lines=10):
    try:
        with open(filename, 'r') as file:
            for line in file.readlines()[-lines:]:
                click.echo(line, nl=False)
    except FileNotFoundError:
        click.echo(f"tail: cannot open '{filename}' for reading: No such file or directory")


@click.command()
@click.argument('files', required=False, nargs=-1, type=click.Path())
def tail(files):
    if files:
        for i, filename in enumerate(files):
            if len(files) > 1:
                click.echo(f"==> {filename} <==")
            tail_file(filename)
            if i < len(files) - 1:
                click.echo()
    else:
        input_lines = []
        while True:
            try:
                line = click.get_text_stream('stdin').readline()
            except KeyboardInterrupt:
                return
            except EOFError:
                break
            if not line:
                break

            input_lines.append(line)
        for line in input_lines[-17:]:
            click.echo(line, nl=False)


if __name__ == '__main__':
    tail()
