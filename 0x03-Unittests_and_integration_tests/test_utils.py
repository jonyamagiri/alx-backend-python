#!/usr/bin/env python3
""" module test_utils.py """

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from utils import access_nested_map


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
