from os import scandir
import sqlparse
from ..utils.utils import argument_parser
from ..tools.jde_sql_decorate import comment, OPTIONS

if __name__ == '__main__':

    PARSER = argument_parser()
    ARGS = PARSER.parse_args()
    OPTIONS['strip_comments'] = ARGS.strip_comments

    print(ARGS.path)
    HEADER = ARGS.header
    COPYRIGHT = f'Copyright Edwards Lifesciences {ARGS.year}, All rights reserved.'
    AUTHOR = ARGS.author
    PATH = ARGS.path

    FILES = [entry for entry in scandir(PATH) if entry.is_file()]

    for file in FILES:
        with open(file.path) as in_file:
            print(file.path)
            new_name = file.path.split('.')[0] + '.sql'
            script = sqlparse.format(in_file.read(), **OPTIONS)
            _header = ['/*',
                       f'/*\n{COPYRIGHT}',
                       f'AUTHOR:{AUTHOR}',
                       f'{HEADER}',
                       f'file_name: {file.name.split(".")[0] +".sql"}',
                       '*/\n']
            header = '\n'.join(_header)
            script = header + comment(script)
            new_name = file.path.split('.')[0] + '.sql'
            with open(new_name, 'w') as out_file:
                out_file.write(script)

print('Done')
