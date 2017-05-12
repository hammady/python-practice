#!/usr/bin/env python
''' Set class implementation with its tests'''

import unittest

class Set(object):
    '''A pedagogical implementation of the set collection using dict'''

    def __init__(self, value_or_list=None):
        self.__dict = {}
        if value_or_list is not None:
            self.add(value_or_list)

    def __repr__(self):
        return "Set(" + str(self.__dict.keys()) + ")"

    def __len__(self):
        return len(self.__dict.keys())

    def __iter__(self):
        return iter(self.__dict)

    def add(self, value_or_list):
        '''Adds a value or a list of values to the set
           If a value to be added is a duplicate, it will not be added'''
        self.__apply_value_or_list(value_or_list, self.__add_value)

    def remove(self, value_or_list):
        '''Removes a value or a list of values from the set
           If a non-existent value is requested to be removed, nothing will happen'''
        self.__apply_value_or_list(value_or_list, self.__remove_value)

    def contains(self, value):
        '''Checks whether a value exists in the set
           Returns True (exists) or False (does not exist)'''
        return self.__dict.has_key(value)

    @staticmethod
    def __apply_value_or_list(value_or_list, proc):
        if isinstance(value_or_list, list):
            for value in value_or_list:
                proc(value)
        else:
            proc(value_or_list)

    def __add_value(self, value):
        self.__dict[value] = True

    def __remove_value(self, value):
        if self.__dict.has_key(value):
            del self.__dict[value]


class SetTest(unittest.TestCase):
    '''Unit tests for the class Set'''

    @staticmethod
    def test_init_empty():
        '''tests init with no values'''
        set1 = Set()
        assert str(set1) == 'Set([])'
        assert not set1     # empty (based on len)
        set2 = Set()
        assert str(set2) == 'Set([])'
        assert not set2     # empty (based on len)

    @staticmethod
    def test_init_values():
        '''tests init with specified values'''
        set1 = Set([1, 2])
        assert str(set1) == 'Set([1, 2])'
        assert len(set1) == 2
        set2 = Set(3)
        assert str(set2) == 'Set([3])'
        assert len(set2) == 1

    @staticmethod
    def test_add():
        '''tests add with value or list of values'''
        set1 = Set()
        set1.add(1)
        assert str(set1) == 'Set([1])'
        assert len(set1) == 1
        set1.add([2, 3])
        assert str(set1) == 'Set([1, 2, 3])'
        assert len(set1) == 3

    @staticmethod
    def test_remove():
        '''tests remove with value or list of values'''
        set1 = Set()
        set1.add(1)
        set1.remove(1)
        assert str(set1) == 'Set([])'
        assert not set1     # empty (based on len)
        set1.remove(2)
        set1.add([3, 4, 5])
        set1.remove([3, 4])
        assert str(set1) == 'Set([5])'
        assert len(set1) == 1

    @staticmethod
    def test_contains():
        '''tests contains'''
        set1 = Set([1, 2])
        assert set1.contains(1)
        assert not set1.contains(3)

    @staticmethod
    def test_len():
        '''tests len'''
        set1 = Set([1, 2])
        assert len(set1) == 2

    @staticmethod
    def test_iter():
        '''tests iterator using for loop'''
        set1 = Set([1, 2, 3])
        values = [x for x in set1]
        assert values == [1, 2, 3]


if __name__ == '__main__':
    unittest.main()
