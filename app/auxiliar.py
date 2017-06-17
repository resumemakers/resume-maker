from json import loads

keys = {'k_name': 'name',
        'k_function': 'function',
        'k_phone': 'phone',
        'k_email': 'email',
        'k_address': 'address',
        'k_education': 'education',
        'k_experience': 'experience',
        'k_skills': 'skills',
        'k_languages': 'languages',
        'k_contact': 'contact',
        'k_portfolio': 'portfolio'
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
            'languages': 'Languages',
            'contact': 'Contact',
            'portfolio': 'Portfolio'},

     'pt': {'name': 'Nome',
            'function': 'Cargo',
            'phone': 'Telefone',
            'email': 'E-mail',
            'address': 'Endereço',
            'education': 'Escolaridade',
            'experience': 'Experiência',
            'skills': 'Habilidades',
            'languages': 'Línguas',
            'contact': 'Contato',
            'portfolio': 'Portfólio'},

     'es': {'name': 'Nombre',
            'function': 'Cargo',
            'phone': 'Teléfono',
            'email': 'E-mail',
            'address': 'Dirección',
            'education': 'Educacíon',
            'experience': 'Experiencia',
            'skills': 'Habildades',
            'languages': 'Idiomas',
            'contact': 'Contacto',
            'portfolio': 'Portfolio'}
     }

templates = {'basic': 'A very basic resume',
             'red': 'A red template - by:magnvmOpvs',
             'Simple': 'A simple template - by:magnvmOpvs'}


def read_json(json_file):
    """
    Função que seleciona o arquivo json a ser lido.

    :args:
        json_file: Arquivo json com as informações para o resume

    :return: um dicionario com as informações do json
    """
    with open(json_file) as _file:
        return loads(_file.read())


def mount_i18n(lang: str) -> dict:
    """
    Monta as chaves no jinja para o idioma escolhido.

    :args:
        lang: Linguagem selecionada

    :return: Um dicionario monstado com a lingua escolida
    """
    return {e: langs[lang][keys[e]] for e in keys}
