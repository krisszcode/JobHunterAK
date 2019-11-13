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