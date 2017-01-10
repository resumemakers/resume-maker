from app.make import create, templates
import click


@click.group()
def main():
    """
    Resume maker
    """
    pass


@main.command(help='List templates')
def list():
    print("Templates: \n")
    for template in templates:
        print("\t{} - {}".format(template,
                                 templates[template]))


@main.command(help='Create a resume')
@click.argument('lang', default='en')
@click.argument('template', default='basic')
@click.argument('json_file', default='examples/info.json')
@click.argument('output', default='resume')
def make(lang, template, json_file, output):
    create(lang, template, json_file, output)

if __name__ == '__main__':
    main()
