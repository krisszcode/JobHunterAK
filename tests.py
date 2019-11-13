import unittest
import data_manager

from application import application
from company import company
from position import position
from student import student

def check_forbidden_functions(tester, file_name):
    with open(file_name, "r") as file:
        lines = file.read()
        tester.assertEqual(lines.find("find("), -1)
        tester.assertEqual(lines.find("sort("), -1)
        tester.assertEqual(lines.find("sorted("), -1)
        tester.assertEqual(lines.find("sum("), -1)
        tester.assertEqual(lines.find("count("), -1)
        tester.assertEqual(lines.find("index("), -1)
        tester.assertEqual(lines.find("print("), -1)
        tester.assertEqual(lines.find("input("), -1)

def check_forbidden_list_functions(tester, file_name):
    with open(file_name, "r") as file:
        lines = file.read()
        tester.assertEqual(lines.find("find("), -1)
        tester.assertEqual(lines.find("sort("), -1)
        tester.assertEqual(lines.find("sorted("), -1)
        tester.assertEqual(lines.find("sum("), -1)
        tester.assertEqual(lines.find("count("), -1)
        tester.assertEqual(lines.find("index("), -1)

def compare_file_contents(first, second):
    first_content = _readfile(first)
    second_content = _readfile(second)

    return first_content == second_content

def _readfile(filename):
    content = ''
    with open(filename, 'r') as f:
        content = f.read()

    return content

class MainTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "main.py")

    def check_forbidden_list_functions(self):
        check_forbidden_functions(self, "main.py")

class CommonTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "common.py")

    def check_forbidden_list_functions(self):
        check_forbidden_functions(self, "common.py")

class UITester(unittest.TestCase):

    def check_forbidden_list_functions(self):
        check_forbidden_functions(self, "ui.py")

class Data_ManagerTester(unittest.TestCase):

    def setUp(self):
        self.test_filename = 'test_file.txt'
        self.test_list = [
            ["ID","NAME","AGE"],
            ["00","Mike","17"],
            ["01","Nora","21"]
        ]

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "data_manager.py")

    def check_forbidden_list_functions(self):
        check_forbidden_functions(self, "data_manager.py")

    def test_imports_from_file(self):
        actual = data_manager.imports_from_file(self.test_filename)

        self.assertListEqual(actual, self.test_list)

    def test_export_to_file(self):
        import os
        tmp_filename = 'test_data_tmp.txt'
        data_manager.export_to_file(tmp_filename, self.test_list)
        are_identical = compare_file_contents(self.test_filename, tmp_filename)
        os.remove(tmp_filename)

        self.assertTrue(are_identical)

class StudentTester(unittest.TestCase):
    data_file = "student/students.txt"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "student/student.py")

    def check_forbidden_list_functions(self):
        check_forbidden_functions(self, "student/student.py")

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()