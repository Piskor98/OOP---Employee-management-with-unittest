import unittest
from Employee import Employee


class TestEmployeeManagment(unittest.TestCase):


    def test_email(self):
        emp1=Employee('Konrad','Schmidt','Germany','Berlin','ObstStraBe 13', 8264556189, 104000)
        self.assertEqual(emp1.create_employee_email, 'Konrad_Schmidt@gmail.com')

    def test_fullname(self):
        emp1=Employee('Konrad','Schmidt','Germany','Berlin','ObstStraBe 13', 8264556189, 104000)
        self.assertEqual(emp1.full_name,'Konrad Schmidt')

    def test_fulladress(self):
        emp1=Employee('Konrad','Schmidt','Germany','Berlin','ObstStraBe 13', 8264556189, 104000)
        self.assertEqual(emp1.full_address['country'], 'Germany')
        self.assertEqual(emp1.full_address['city'], 'Berlin')
        self.assertEqual(emp1.full_address['address'], 'ObstStraBe 13')

    def test_business_card(self):
        emp2 = Employee('Angela', 'Schmidt', 'Germany', 'Berlin', 'Kanarienvogel 1', 345543189, 112000)
        self.assertEqual(emp2.business_card['employee'],'Angela Schmidt')


    def test_types(self):
        emp2=Employee('Angela','Schmidt','Germany','Berlin','Kanarienvogel 1', 345543189, 112000)
        self.assertRaises(TypeError, emp2.business_card['contact'], '345543189')

    def test_apply_raise_salary(self):
        emp2=Employee('Angela','Schmidt','Germany','Berlin','Kanarienvogel 1', 345543189, 112000)
        self.assertAlmostEqual(emp2.apply_raise_salary(),117600)