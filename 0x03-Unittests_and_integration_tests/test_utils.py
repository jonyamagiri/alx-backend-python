#!/usr/bin/env python3
""" module test_utils.py """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Any, Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str, ...],
        expected_output: Any
    ) -> None:
        """
        Test that the access_nested_map function returns the expected result.
        Args:
            nested_map: The nested map to access.
            path: The path to the value in the nested map.
            expected_output: The expected result of accessing the nested map.
        Returns:
            None.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str, ...],
        exception_msg: Exception
    ) -> None:
        """
        Test that a KeyError is raised when accessing a non-existent key
         in the nested map.
        Args:
            nested_map: The nested map to access.
            path: The path to the value in the nested map.
            exception_msg: The expected exception message.
        Returns:
            None.
        """
        with self.assertRaises(exception_msg):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict[str, Any],
        mock_get: Any
    ) -> None:
        """
        Test that get_json returns the expected result.
        Args:
            test_url: The URL to use in the test.
            test_payload: The expected payload to be returned.
            mock_get: Mocked requests.get object.
        Returns:
            None.
        """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator."""
    class TestClass:
        """Class to test the memoize decorator."""
        def a_method(self) -> int:
            return 42

        @memoize
        def a_property(self) -> int:
            return self.a_method()

    def test_memoize(self) -> None:
        """
        Test that the memoize decorator caches the result and avoids
        redundant method calls.
        """
        obj = self.TestClass()
        with patch.object(obj, 'a_method') as mock_method:
            result1: int = obj.a_property
            result2: int = obj.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, result2)
