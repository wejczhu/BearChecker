import re
import logging

class IncludeChecker():

    def __init__(self, first_name, content):
        """
        Init class
        """
        self.first_name = first_name
        self.content = content


    def find_all_include_file(self, content):
        """
        Find include files which start with #include
        """
        include_lines = []

        for line in content:
            if line.startswith("#include"):
                include_lines.append(line)

        self.private_include_lines = self.find_private_include_file_name(include_lines)
        self.public_include_lines = self.find_public_include_file_name(include_lines)


    def check(self):
        """
        Check if all the thing is good
        """
        ret = True
        self.find_all_include_file(self.content)
        ret &= self.check_first_include_file(self.first_name, self.private_include_lines)
        # Check private include
        ret &= self.check_include_order(self.private_include_lines)
        # Check public include
        ret &= self.check_include_order(self.public_include_lines)

        return ret


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
        """
        Check if the first include file is the input file name
        """
        order_include = lines.copy()
        order_include.sort()
        if lines != order_include:
            logging.error("The order for include files in incorrect!")
            return False

        return True


    def find_private_include_file_name(self, include_line):
        """
        Find private include files
        """
        result = []
        for line in include_line:
            if re.search('#include \"(.*)\"', line):
                result.append(re.search('#include \"(.*)\"', line).group(1))

        return result


    def find_public_include_file_name(self, include_line):
        """
        Find public include files
        """
        result = []
        for line in include_line:
            if re.search('#include <(.*)>', line):
                result.append(re.search('#include <(.*)>', line).group(1))

        return result