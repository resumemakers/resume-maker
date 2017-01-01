from json import loads


def read_json(file='../data/info.json'):
    """
    Função que seleciona o arquivo json a ser lido
    """
    with open(file) as _file:
        return loads(_file.read())
