import unittest
from .name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for the `name_function()` in `name_function.py`"""
    def test_first_last_name(self):
        """Do names such as 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names such as 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()