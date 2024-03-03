import sys
import click


@click.command()
@click.argument('files', required=False, nargs=-1, type=click.Path())
def wc(files):
    if files:
        total_lines, total_words, total_bytes = 0, 0, 0
        for i, filename in enumerate(files):
            lines, words, bytes = 0, 0, 0
            with open(filename, 'r') as f:
                for l in f.readlines():
                    lines += 1
                    words += len(l.split())
                    bytes += len(l)
            total_lines += lines
            total_words += words
            total_bytes += bytes
            click.echo(f"{lines:4} {words:4} {bytes:4} {filename}")
        if len(files) > 1:
            click.echo(f"{total_lines:4} {total_words:4} {total_bytes:4} total")
    else:
        total_lines, total_words, total_bytes = 0, 0, 0
        while True:
            try:
                line = click.get_text_stream('stdin').readline()
            except KeyboardInterrupt:
                return
            except EOFError:
                break
            if not line:
                break
            total_lines += 1
            total_words += len(line.split())
            total_bytes += len(line)

        click.echo(f"{total_lines:8} {total_words:8} {total_bytes:8}")


if __name__ == '__main__':
    wc()
