from json import loads


def read_json(file):
    """
    Função que seleciona o arquivo json a ser lido
    """
    with open(file) as _file:
        return loads(_file.read())


templates = {'basic': 'A very simple resume',
             'red': 'Moder red resume'}
