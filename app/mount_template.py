from jinja2 import FileSystemLoader, Environment


def select_template(template='basic'):
    """
    Função que seleciona o tamplate HTML que vai ser usado
    """
    temp_path = FileSystemLoader(searchpath="../templates")

    j_env = Environment(loader=temp_path)

    return j_env.get_template("./{}.html".format(template))
