import argparse
import logging
import re
from pathlib import Path

def main(args):
    current_file = Path(args.file)
    name = current_file.stem

    with open (current_file, "r") as file:
        content = file.readlines()

    include_checker = CheckInclude(name, content)
    include_checker.check()
    #check_include_order(name, include_lines)

    #current_file = read


class CheckInclude():

    def __init__(self, first_name, content):
        self.first_name = first_name
        self.content = content


    def find_all_include_file(self, content):
        include_lines = []

        for line in content:
            if line.startswith("#include"):
                include_lines.append(line)

        self.private_include_lines = self.find_private_include_file_name(include_lines)
        self.publice_include_lines = self.find_public_include_file_name(include_lines)

        print(self.private_include_lines)

    def check(self):
        self.find_all_include_file(self.content)
        self.check_first_include_file(self.first_name, self.private_include_lines)
        self.check_include_order(self.private_include_lines)


    def check_first_include_file(self, name, lines):
        """
        Check if the first include file is the input file name
        """
        if lines[0] != name + ".h":
            logging.error("The first include must be itself")
            return False
        
        lines.remove(lines[0])
 
        return True



    def check_include_order(self, lines):
        print(lines)
        order_include = lines
        order_include.sort()
        print(order_include)
        if sorted(lines) == sorted(order_include):
            logging.error("The order for include files in incorrect!")
        else:
            print("two line are equal")
            return False

        return True

    def find_private_include_file_name(self, include_line):
        result = []
        for line in include_line:
            if re.search('#include \"(.*)\"', line):
                result.append(re.search('#include \"(.*)\"', line).group(1))

        return result


    def find_public_include_file_name(self, include_line):
        result = []
        for line in include_line:
            if re.search('#include <(.*)>', line):
                result.append(re.search('#include <(.*)>', line).group(1))

        return result


def args():
    """
    Parse the import argument
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The cpp file needs to be checked")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main(args())