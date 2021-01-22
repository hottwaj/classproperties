import unittest
from classproperties import *

def get_cls_definition():
    class Cls(object):

        @classproperty
        def prop(cls):
            return 1000

        cached_prop_exec_count = 0

        @cached_classproperty
        def cached_prop(cls):
            cls.cached_prop_exec_count += 1
            return 2000
    return Cls


class TestWaterfall(unittest.TestCase):
    """This class contains all tests of the library"""
      
    def test_classproperty(self):
        Cls = get_cls_definition()
        self.assertEqual(Cls.prop, 1000)

    def test_classproperty_instance(self):
        Cls = get_cls_definition()
        self.assertEqual(Cls().prop, 1000)

    def test_cached_classproperty(self):
        Cls = get_cls_definition()
        self.assertEqual(Cls.cached_prop_exec_count, 0)
        self.assertEqual(Cls.cached_prop, 2000)
        self.assertEqual(Cls.cached_prop_exec_count, 1)

    def test_cached_classproperty_executed_once(self):
        Cls = get_cls_definition()
        self.assertEqual(Cls.cached_prop_exec_count, 0)
        self.assertEqual(Cls.cached_prop, 2000)
        self.assertEqual(Cls.cached_prop_exec_count, 1)
        self.assertEqual(Cls.cached_prop, 2000)
        self.assertEqual(Cls.cached_prop_exec_count, 1)

    def test_cached_classproperty_instance(self):
        Cls = get_cls_definition()
        inst = Cls()
        self.assertEqual(inst.cached_prop_exec_count, 0)
        self.assertEqual(inst.cached_prop, 2000)
        self.assertEqual(inst.cached_prop_exec_count, 1)

    def test_cached_classproperty_executed_once_instance(self):
        Cls = get_cls_definition()
        inst = Cls()
        self.assertEqual(inst.cached_prop_exec_count, 0)
        self.assertEqual(inst.cached_prop, 2000)
        self.assertEqual(inst.cached_prop_exec_count, 1)
        self.assertEqual(inst.cached_prop, 2000)
        self.assertEqual(inst.cached_prop_exec_count, 1)

    def test_cached_classproperty_executed_once_instance_cls_share_same_cached_val(self):
        Cls = get_cls_definition()
        inst = Cls()
        self.assertEqual(inst.cached_prop_exec_count, 0)
        self.assertEqual(inst.cached_prop, 2000)
        self.assertEqual(inst.cached_prop_exec_count, 1)
        self.assertEqual(inst.cached_prop, 2000)
        self.assertEqual(inst.cached_prop_exec_count, 1)

        self.assertEqual(Cls.cached_prop_exec_count, 1)
        self.assertEqual(Cls.cached_prop, 2000)
        self.assertEqual(Cls.cached_prop_exec_count, 1)

        inst = Cls()
        self.assertEqual(inst.cached_prop_exec_count, 1)
        self.assertEqual(inst.cached_prop, 2000)
        self.assertEqual(inst.cached_prop_exec_count, 1)

if __name__ == '__main__':
    unittest.main()
