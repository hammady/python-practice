#!/usr/bin/env python

import unittest

class Set(object):
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
        self.__apply_value_or_list(value_or_list, self.__add_value)

    def remove(self, value_or_list):
        self.__apply_value_or_list(value_or_list, self.__remove_value)

    def contains(self, value):
        return self.__dict.has_key(value)

    def __apply_value_or_list(self, value_or_list, proc):
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
    def test_init_empty(self):
        s = Set()
        assert str(s) == 'Set([])'
        assert len(s) == 0
        s2 = Set()
        assert str(s2) == 'Set([])'
        assert len(s2) == 0

    def test_init_values(self):
        s = Set([1, 2])
        assert str(s) == 'Set([1, 2])'
        assert len(s) == 2
        s2 = Set(3)
        assert str(s2) == 'Set([3])'
        assert len(s2) == 1

    def test_add(self):
        s = Set()
        s.add(1)
        assert str(s) == 'Set([1])'
        assert len(s) == 1

    def test_remove(self):
        s = Set()
        s.add(1)
        s.remove(1)
        assert str(s) == 'Set([])'
        assert len(s) == 0
        s.remove(2)
        s.add([3, 4, 5])
        s.remove([3, 4])
        assert str(s) == 'Set([5])'
        assert len(s) == 1

    def test_contains(self):
        s = Set([1, 2])
        assert s.contains(1)
        assert not s.contains(3)

    def test_len(self):
        s = Set([1, 2])
        assert len(s) == 2

    def test_iter(self):
        s = Set([1, 2, 3])
        values = [x for x in s]
        assert values == [1, 2, 3]


if __name__ == '__main__':
    unittest.main()
