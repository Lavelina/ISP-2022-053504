from test.test_obj import *
import unittest

import sys

from sourses import SerializerMain as ser


class SerializerTester(unittest.TestCase):

    def __init__(self, method):
        super().__init__(method)
        self.SerializerJson = ser.Serializer()
        path = self.SerializerJson.path
        self.SerializerJson.path = json_file
        ext = self.SerializerJson.extension
        self.SerializerJson.extension = 'json'
        self.SerializerToml = ser.Serializer(path=toml_file, extension='toml')
        self.SerializerYaml = ser.Serializer(path=yaml_file, extension='yaml')

    def test_str(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(str1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(str1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(str1))

        self.assertEqual(json_obj, str1)
        self.assertEqual(toml_obj, str1)
        self.assertEqual(yaml_obj, str1)

    def test_int(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(num1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(num1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(num1))

        self.assertEqual(json_obj, num1)
        self.assertEqual(toml_obj, num1)
        self.assertEqual(yaml_obj, num1)

    def test_float(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(flot1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(flot1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(flot1))

        self.assertEqual(json_obj, flot1)
        self.assertEqual(toml_obj, flot1)
        self.assertEqual(yaml_obj, flot1)

    def test_bool(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(bool1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(bool1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(bool1))

        self.assertEqual(json_obj, bool1)
        self.assertEqual(toml_obj, bool1)
        self.assertEqual(yaml_obj, bool1)

    def test_bytes(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(bytes1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(bytes1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(bytes1))

        self.assertEqual(json_obj, bytes1)
        self.assertEqual(toml_obj, bytes1)
        self.assertEqual(yaml_obj, bytes1)

    def test_bytearray(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(bytearr1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(bytearr1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(bytearr1))

        self.assertEqual(json_obj, bytearr1)
        self.assertEqual(toml_obj, bytearr1)
        self.assertEqual(yaml_obj, bytearr1)

    def test_builtin(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(bltfunc))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(bltfunc))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(bltfunc))

        self.assertEqual(json_obj(lst1), bltfunc(lst1))
        self.assertEqual(toml_obj(lst1), bltfunc(lst1))
        self.assertEqual(yaml_obj(lst1), bltfunc(lst1))

    def test_set(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(set1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(set1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(set1))
        #toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))

        self.assertEqual(json_obj, set1)
        self.assertEqual(toml_obj, set1)
        self.assertEqual(yaml_obj, set1)
       # self.assertEqual(toml_obj, lst1)

    def test_frozenset(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(frzset1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(frzset1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(frzset1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))

        self.assertEqual(json_obj, frzset1)
        self.assertEqual(toml_obj, frzset1)
        self.assertEqual(yaml_obj, frzset1)
        # self.assertEqual(toml_obj, lst1)

    def test_tuple(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(tpl1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(tpl1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(tpl1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))

        self.assertEqual(json_obj, tpl1)
        self.assertEqual(toml_obj, tpl1)
        self.assertEqual(yaml_obj, tpl1)
        # self.assertEqual(toml_obj, lst1)

    def test_list(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(lst1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(lst1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(lst1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(lst1))

        self.assertEqual(json_obj, lst1)
        self.assertEqual(toml_obj, lst1)
        self.assertEqual(yaml_obj, lst1)
        # self.assertEqual(toml_obj, lst1)

    def test_simple_dicts(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(dict1))
        toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(dict1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(dict1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(dict1))
        # print(toml_obj.a)
        # print(toml_obj.b)
        # print(toml_obj)

        self.assertEqual(json_obj, dict1)
        self.assertEqual(toml_obj, dict1)
        self.assertEqual(yaml_obj, dict1)
        # self.assertEqual(toml_obj, dict1)

    def test_simple_object(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(obj1))
        #toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(obj1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(obj1))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(obj1))

        self.assertEqual(json_obj.a, obj1.a)
        self.assertEqual(json_obj.b, obj1.b)
        #self.assertEqual(toml_obj.a, obj1.a)
        #self.assertEqual(toml_obj.b, obj1.b)
        self.assertEqual(yaml_obj.a, obj1.a)
        self.assertEqual(yaml_obj.b, obj1.b)

    def test_classes(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(cls1))
        #toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(cls1))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(cls1))

        self.assertEqual(json_obj.__bases__[0].__name__, cls1.__bases__[0].__name__)
       # self.assertEqual(toml_obj.__bases__[0].__name__, cls1.__bases__[0].__name__)
        self.assertEqual(yaml_obj.__bases__[0].__name__, cls1.__bases__[0].__name__)
        self.assertEqual(json_obj.__bases__[1].__name__, cls1.__bases__[1].__name__)
        #self.assertEqual(toml_obj.__bases__[1].__name__, cls1.__bases__[1].__name__)
        self.assertEqual(yaml_obj.__bases__[1].__name__, cls1.__bases__[1].__name__)

    def test_simple_function(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(hello))
        #toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(hello))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(hello))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(hello))

        self.assertEqual(json_obj(), exp_hello)
       # self.assertEqual(toml_obj(), exp_hello)
        self.assertEqual(yaml_obj(), exp_hello)

    def test_functions_with_global_variable(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(say_hello))
       # toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(say_hello))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(say_hello))

        self.assertEqual(json_obj(), exp_say_hello)
       # self.assertEqual(toml_obj(), exp_say_hello)
        self.assertEqual(yaml_obj(), exp_say_hello)

    def test_function_with_parameters(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(add))
       # toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(add))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(add))
        # toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(add))

        self.assertEqual(json_obj(2, 3), exp_add)
       # self.assertEqual(toml_obj(2, 3), exp_add)
        self.assertEqual(yaml_obj(2, 3), exp_add)
        # self.assertEqual(toml_obj(2, 3), exp_add)

    def test_file_io(self):
        self.SerializerJson.dump(add)
#        self.SerializerToml.dump(add)
        self.SerializerYaml.dump(add)
        json_obj = self.SerializerJson.load()
       # toml_obj = self.SerializerToml.load()
        yaml_obj = self.SerializerYaml.load()

        self.assertEqual(json_obj(2, 3), exp_add)
       # self.assertEqual(toml_obj(2, 3), exp_add)
        self.assertEqual(yaml_obj(2, 3), exp_add)

    def test_lambda(self):
        json_obj = self.SerializerJson.loads(self.SerializerJson.dumps(power))
        #toml_obj = self.SerializerToml.loads(self.SerializerToml.dumps(power))
        yaml_obj = self.SerializerYaml.loads(self.SerializerYaml.dumps(power))

        self.assertEqual(json_obj(2, 3), exp_power)
        #self.assertEqual(toml_obj(2, 3), exp_power)
        self.assertEqual(yaml_obj(2, 3), exp_power)