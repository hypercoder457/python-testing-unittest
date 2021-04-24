import unittest
from .employee import Employee


class EmployeesTestCase(unittest.TestCase):
    def setUp(self):
        first_name = "Janis"
        last_name = "Joplin"
        salary = 30000
        self.employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        employee_money = self.employee.give_raise()
        self.assertEqual(employee_money, 35000)

    def test_give_custom_raise(self):
        employee_money = self.employee.give_raise(6000)
        self.assertEqual(employee_money, 36000)


if __name__ == '__main__':
    unittest.main()
