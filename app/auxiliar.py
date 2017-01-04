from json import loads

keys = {'key_1': 'name',
        'key_2': 'function',
        'key_3': 'phone',
        'key_4': 'email',
        'key_5': 'address',
        'key_6': 'education',
        'key_7': 'experience',
        'key_8': 'skills',
        'key_9': 'languages'
        }

langs = \
    {'en': {'name': 'Name',
            'function': 'Function',
            'phone': 'Phone',
            'email': 'Email',
            'address': 'Address',
            'education': 'Education',
            'experience': 'Experience',
            'skills': 'Skills',
            'languages': 'Languages'},

     'pt': {'name': 'Nome',
            'function': 'Cargo',
            'phone': 'Telefone',
            'email': 'E-mail',
            'address': 'Endereço',
            'education': 'Escolaridade',
            'experience': 'Experiência',
            'skills': 'Habildades',
            'languages': 'Línguas'}
     }

templates = {'basic': 'A very simple resume',
             'red': 'Moder red resume'}


def read_json(file):
    """
    Função que seleciona o arquivo json a ser lido
    """
    with open(file) as _file:
        return loads(_file.read())


def mount_i18n(lang: str) -> dict:
    """
    Monta as chaves no jinja para o idioma escolhido
    """
    return {e: langs[lang][keys[e]] for e in keys}
