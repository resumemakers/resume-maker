from weasyprint import HTML
from mount_template import select_template
from auxiliar import read_json


template = select_template()
template_vars = read_json()

build = template.render(template_vars)


HTML(string=build).write_pdf("resume.pdf")
