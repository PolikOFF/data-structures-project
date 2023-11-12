import unittest
from src.stack import Stack

"""Здесь надо написать тесты с использованием unittest для модуля stack."""


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(self.stack.push('data1'), None)
        self.assertIsNone(self.stack.push('data1'))
