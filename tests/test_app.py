import unittest
from functions import camel_case, snake_case, pascal_case, kebab_case
from functions import upper_case, lower_case, alternate_case, title_case
from functions import reverse_text, remove_spaces


class TestStringFunctions(unittest.TestCase):

    # testes unitários
    def test_camel_case(self):
        self.assertEqual(camel_case("hello world"), "helloWorld")
        self.assertEqual(camel_case("HELLO WORLD"), "helloWorld")
        self.assertEqual(camel_case("Python testing"), "pythonTesting")

    def test_snake_case(self):
        self.assertEqual(snake_case("hello world"), "hello_world")
        self.assertEqual(snake_case("Hello World"), "hello_world")
        self.assertEqual(snake_case("Unit testing"), "unit_testing")

    def test_pascal_case(self):
        self.assertEqual(pascal_case("hello world"), "HelloWorld")
        self.assertEqual(pascal_case("Python Testing"), "PythonTesting")
        self.assertEqual(pascal_case("unit test"), "UnitTest")

    def test_kebab_case(self):
        self.assertEqual(kebab_case("hello world"), "hello-world")
        self.assertEqual(kebab_case("Unit Test"), "unit-test")
        self.assertEqual(kebab_case("Python Testing"), "python-testing")

    def test_upper_case(self):
        self.assertEqual(upper_case("hello world"), "HELLO WORLD")
        self.assertEqual(upper_case("Unit Test"), "UNIT TEST")
        self.assertEqual(upper_case("python testing"), "PYTHON TESTING")

    def test_lower_case(self):
        self.assertEqual(lower_case("HELLO WORLD"), "hello world")
        self.assertEqual(lower_case("Unit Test"), "unit test")
        self.assertEqual(lower_case("Python Testing"), "python testing")

    def test_alternate_case(self):
        self.assertEqual(alternate_case("hello world"), "HeLlO WoRlD")
        self.assertEqual(alternate_case("unit test"), "UnIt tEsT")

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")
        self.assertEqual(title_case("unit test"), "Unit Test")

    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello world"), "dlrow olleh")
        self.assertEqual(reverse_text("Unit Test"), "tseT tinU")

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("hello world"), "helloworld")
        self.assertEqual(remove_spaces("Unit Test"), "UnitTest")
        self.assertEqual(remove_spaces(" multiple   spaces "), "multiplespaces")


if __name__ == '__main__':
    unittest.main()
