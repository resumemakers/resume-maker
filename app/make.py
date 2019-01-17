from weasyprint import HTML
from app.mount_template import select_template
from app.languages import mount_i18n
from app.dict_tools import read_json, check_json_keys, check_json_types


def create(lang, template, json_file, output):
    """
    Função que cria o pdf baseado no html.

    :params:
        lang: Linguagem escolhida
        template: Template escolhido
        json_file: Arquivo a ser lido para gerar o cv
        output: arquivo de saida para o pdf

    :vars:
        css: path do stylesheet
        pdf: path do pdf de saida
        template_vars: dict para o jinja
        build: HTML page

    :returns: cv em pdf
    """
    css = "./templates/stylesheet/{}.css".format(template)
    pdf = "{}.pdf".format(output)

    template_vars = read_json(json_file)

    checked_field = check_json_keys(template_vars)

    if not checked_field[0]:
        raise Exception(f'Json no has keys: {checked_field[1]}')

    checked_types = check_json_types(template_vars)

    if not checked_types[0]:
        raise Exception(f'Json no has wrong types on keys: {checked_types[1]}')

    template_vars.update(mount_i18n(lang))

    template = select_template(template)

    build = template.render(template_vars)

    HTML(string=build, encoding='utf-8').write_pdf(pdf, [css])
