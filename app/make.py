from weasyprint import HTML
from mount_template import select_template
from auxiliar import read_json, templates
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
@click.argument('template', default='basic')
@click.argument('output', default='resume')
@click.argument('file', default='../data/info.json')
def create(template, file, output):
    template_vars = read_json(file)

    template = select_template(template)
    build = template.render(template_vars)

    HTML(string=build).write_pdf("{}.pdf".format(output))


if __name__ == '__main__':
    main()
