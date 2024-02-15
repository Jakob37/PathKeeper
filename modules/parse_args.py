import argparse


def parse_arguments() -> any:
    parser = argparse.ArgumentParser()

    sub_parsers = parser.add_subparsers(dest="subcommand", required=True)

    setup = sub_parsers.add_parser(
        "setup", help="Setup the db next to the called script"
    )

    add = sub_parsers.add_parser("add", help="Add new path")
    add.add_argument("path")
    add.add_argument("--label", required=True)
    add.add_argument("--alias", required=True)

    remove = sub_parsers.add_parser("rm", help="Add new path")
    remove.add_argument("path_id")
    remove.add_argument("--type", default="id", help="Removal field type")

    list_paths = sub_parsers.add_parser("view", help="List paths")
    list_paths.add_argument(
        "--showid", action="store_const", const=True, help="Show ID column"
    )
    # list_paths.add_argument('')

    goto = sub_parsers.add_parser("goto", help="Go to path")
    goto.add_argument("path", help="Path")
    # parser_crazy.add_argument('--fool', action='store_const', const=True, help='it is foolish option')

    args = parser.parse_args()

    return args
