'''
set of tools utilites
'''
from argparse import ArgumentTypeError, ArgumentParser

def str2bool(answer):
    """function for argparse to validate boolean input"""
    if answer.lower() in ('yes', 'true', 't', 'y', '1'):
        result = True
    elif answer.lower() in ('no', 'false', 'f', 'n', '0'):
        result = False
    else:
        raise ArgumentTypeError("Boolean value expected.")
    return result


def argument_parser(description='tools cmd'):
    """Common set of arguments for CMD tools"""

    parser = ArgumentParser(description=description)

    parser.add_argument("--login",
                        help='db login',
                        required=False)

    parser.add_argument("--host",
                        required=False,
                        help='uri of host')

    parser.add_argument("--path",
                        default=None,
                        required=False)

    parser.add_argument("--strip_comments",
                        const=False,
                        default=False,
                        type=str2bool,
                        nargs='?',
                        required=False,
                        help="If True existing comments are removed from the statements")

    parser.add_argument("--author",
                        default='',
                        required=False)

    parser.add_argument("--header",
                        default='JDE Queries',
                        required=False)

    parser.add_argument("--year",
                        default='2019',
                        required=False)

    return parser
