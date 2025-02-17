from models.base import Base
import unittest


class TestBaseInstantiation(unittest.TestCase):

    
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1._Base__nb_objects, 1)
        self.assertEqual(b2._Base__nb_objects, 2)
        self.assertEqual(b3._Base__nb_objects, 3)

    def test_a_value(self):
        b1 = Base(12)
        self.assertEqual(b1._Base__nb_objects, 12)

    def test_assign_objectid(self):
        b1 = Base()
        b1.id = 12
        self.assertEqual(b1.id, 12)


    def test_private_instance_id(self):
        with self.assertRaises(AttributeError):
            print(Base(12)._Base__nb_objects)



if __name__ == '__main__':
    unittest.main()
