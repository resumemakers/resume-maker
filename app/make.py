from weasyprint import HTML
from mount_template import select_template
from auxiliar import read_json, templates, mount_i18n
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
@click.argument('file', default='../data/info.json')
@click.argument('output', default='resume')
def create(lang, template, file, output):
    template_vars = read_json(file)
    template_vars.update(mount_i18n(lang))

    template = select_template(template)

    build = template.render(template_vars)

    HTML(string=build, encoding='utf-8').write_pdf("{}.pdf".format(output))


if __name__ == '__main__':
    main()
