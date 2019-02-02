import os
import sys


TEMPLATE_DIR = 'template/'
TARGET_DIR = 'target/'
MESSAGE_TEMPLATE = 'message.xml.tpl'
MESSAGE = 'message.xml'
OPTIONS_TEMPLATE = 'options.txt.tpl'
OPTIONS = 'options.txt'


def _parse_options_from_csv(csv_filename):
    return {
        k.strip(): v.strip() for _, _, k, v in (
            line.split(';', 3) for line in open(csv_filename) if line.strip()
        )
    }


def _parse_options_from_txt():
    return {
        k.strip(): v.strip() for k, v in (
            line.split('=', 1) for line in open(OPTIONS) if not line.startswith('#') and line.strip()
        )
    }


def _apply_tempalates(options):
    message_template_filepath = os.path.join(TEMPLATE_DIR, MESSAGE_TEMPLATE)
    with open(message_template_filepath) as message_template:
        message_content = message_template.read()
    
    for k, v in options.items():
        message_content = message_content.replace(k, v, 1)

    with open(MESSAGE, 'w+') as dest_file:
        dest_file.write(message_content)


def _copy_options_template():
    options_template_filepath = os.path.join(TEMPLATE_DIR, OPTIONS_TEMPLATE)
    with open(options_template_filepath) as options_template:
        options_content = options_template.read()

    with open(OPTIONS, 'w+') as dest_file:
        dest_file.write(options_content)


def main():
    if len(sys.argv) > 1:
        if (sys.argv[1] == 'cp'):
            _copy_options_template()
            sys.exit()

        csv_filename = sys.argv[1]
        options = _parse_options_from_csv(csv_filename)
    else:
        options = _parse_options_from_txt()

    _apply_tempalates(options)

if __name__ == '__main__':
    main()
