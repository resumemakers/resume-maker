from json import loads


def read_json(json_file):
    """
    Função que seleciona o arquivo json a ser lido.

    :args:
        json_file: Arquivo json com as informações para o resume

    :return: um dicionario com as informações do json
    """
    with open(json_file) as _file:
        return loads(_file.read())
