from jinja2 import FileSystemLoader, Environment
from os.path import abspath


def select_template(template):
    """
    Função que seleciona o tamplate HTML que vai ser usado.

    :args:
        template: template escolhido para o resume

    :return: o template para ser montado em pdf
    """
    temp_path = FileSystemLoader(searchpath=abspath("./templates"))

    j_env = Environment(loader=temp_path)

    return j_env.get_template("{}.html".format(template))
