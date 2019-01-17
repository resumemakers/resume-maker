from itertools import filterfalse
from json import loads
from typing import Dict, Tuple, List, Text

KEYS = {
    "name": Text,
    "profession": Text,
    "phone": Text,
    "email": Text,
    "address": Text,
    "portfolio": str,
    "education": List,
    "experience": List,
    "skills": List,
    "languages": List,
}


def read_json(json_file: Text) -> Dict:
    """
    Função que seleciona o arquivo json a ser lido.

    :args:
        json_file: Arquivo json com as informações para o resume

    :return: um dicionario com as informações do json
    """
    with open(json_file) as _file:
        return loads(_file.read())


def check_json_keys(
    json: Dict, *, keys: Dict = KEYS
) -> Tuple[bool, List[Text]]:
    """Check necessary keys to make resume."""
    missing_keys = list(filter(lambda key: key not in json.keys(), KEYS))
    return not any(missing_keys), missing_keys


def check_json_types(
    json: Dict, *, keys: Dict = KEYS
) -> Tuple[bool, List[Text]]:
    """Check types on json."""
    missing_keys = list(
        filterfalse(lambda key: isinstance(json[key], KEYS[key]), KEYS)
    )
    return not any(missing_keys), missing_keys
