from models.base import Base
import unittest


class TestBaseInstantiation(unittest.TestCase):
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.__nb_objects, 1)
        self.assertEqual(b2.__nb_objects, 2)
        self.assertEqual(b3.__nb_objects, 3)

    def test_a_value(self):
        b1 = Base(12)
        self.assertEqual(b1.__nb_objects, 12)

    def test_assign_objectid(self):
        b1 = Base()
        b1.id = 12
        self.assertEqual(b1.id, 12)


    def test_private_instance_id(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects = 2



if __name__ == '__main__':
    unittest.main()
