
from IncludeChecker import IncludeChecker

import argparse

import re
from pathlib import Path

def main(args):
    current_file = Path(args.file)
    name = current_file.stem

    with open (current_file, "r") as file:
        content = file.readlines()

    include_checker = IncludeChecker.IncludeChecker(name, content)
    include_checker.check()
    #check_include_order(name, include_lines)

    #current_file = read





def parse_arguments():
    """
    Parse the import argument
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The cpp file needs to be checked")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main(parse_arguments())