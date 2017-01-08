from json import loads
from os.path import exists, abspath
from os import makedirs
from behave import when, then
from app import make


@when('send a "{file}" json')
def send(context, file):
    context.temp = './tmp'
    if not exists(context.temp):
        makedirs(context.temp)

    context.json_file = '{}/{}.json'.format(context.temp, file)

    with open(context.json_file, 'w') as _file:
        _file.writelines(context.text)


@when('set "{lang}" lang "{template}" template')
def select(context, lang, template):
    context.output = 'tmp/{}_{}'.format(lang, template)

    make.create(lang,
                template,
                context.json_file,
                context.output)


@then('resume was generated at "{path}"')
def check(context, path):
    assert exists('{}.{}'.format(context.output, 'pdf')), \
        'Resume was not generated'
