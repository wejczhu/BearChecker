
import unittest
import IncludeChecker

class TestIncludeChecker(unittest.TestCase):
    def setUp(self):
        """Create test cpp file for test"""
        

        # Create test cpp file


    def test_first_include_file(self):
        write_content = """#include \"a.h\"\n#include \"b.h\""""
        self.__create_test_file(write_content)

        with open (self.test_file, 'r') as file:
            content = file.readlines()
        include_checker = IncludeChecker.IncludeChecker("test", content)
        self.assertFalse(include_checker.check())

    def test_include_file_order(self):
        write_content = """#include \"test.h\"\n#include \"b.h\"\n#include \"a.h\"\n"""
        self.__create_test_file(write_content)

        with open (self.test_file, 'r') as file:
            content = file.readlines()
        include_checker = IncludeChecker.IncludeChecker("test", content)
        self.assertFalse(include_checker.check())

    def test_all_right(self):
        write_content = """#include \"test.h\"\n#include \"a.h\"\n#include \"b.h\"\n"""
        self.__create_test_file(write_content)

        with open (self.test_file, 'r') as file:
            content = file.readlines()
            print(content)
        include_checker = IncludeChecker.IncludeChecker("test", content)
        self.assertTrue(include_checker.check())

    def __create_test_file(self, content):
        self.test_file = "test.cpp"
        with open (self.test_file, 'w') as file:
            file.write(content)




if __name__ == "__main__":
    unittest.main()