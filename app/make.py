from weasyprint import HTML
from pdfkit import from_string
from app.mount_template import select_template
from app.auxiliar import read_json, templates, mount_i18n


def create(lang, template, json_file, output):
    """
    Função que cria o pdf baseado no html

    :params:
        - lang: Linguagem escolhida
        - template: Template escolhido
        - json_file: Arquivo a ser lido para gerar o cv
        - output: arquivo de saida para o pdf

    :returns: cv em pdf
    """
    template_vars = read_json(json_file)
    template_vars.update(mount_i18n(lang))

    template = select_template(template)

    build = template.render(template_vars)

    from_string(build, 'teste.pdf')
