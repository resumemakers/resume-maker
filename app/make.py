from weasyprint import HTML
from app.mount_template import select_template
from app.auxiliar import read_json, templates, mount_i18n


def create(lang, template, json_file, output):
    template_vars = read_json(json_file)
    template_vars.update(mount_i18n(lang))

    template = select_template(template)

    build = template.render(template_vars)

    HTML(string=build, encoding='utf-8').write_pdf("{}.pdf".format(output))
