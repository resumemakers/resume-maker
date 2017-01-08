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
        'k_portifolio': 'portifolio'
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
            'portifolio': 'Portifolio'},

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
            'portifolio': 'Portifólio'},

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
            'portifolio': 'Portifolio'}
     }

templates = {'basic': 'A very basic resume',
             'red': 'A red template - by:magnvmOpvs'}


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
