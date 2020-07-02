import unittest
from Student_class import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student.Student('Kilmer', 'Lisa')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Kilmer')
        self.assertEqual(self.student.first_name, 'Lisa')

    def test_object_created_all_attributes(self):
        student = self.student.Student('Kilmer', 'Lisa', 'CS', '3.5')
        assert student.last_name == 'Kilmer'
        assert student.first_name == 'Lisa'
        assert student.major == 'CS'
        assert student.gpa == '3.5'

    def test_student_str(self):
        self.assertEqual(str(self.student.first_name, 'Lisa'))

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = self.student.Student('123', 'Lisa')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = self.student.Student('Kilmer', 'abc')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = self.student.Student('Kilmer', 'Lisa', 'abc')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = self.student.Student('Kilmer', 'Lisa', 'abc')



if __name__ == '__main__':
    unittest.main()
