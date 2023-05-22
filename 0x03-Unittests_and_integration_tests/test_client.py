#!/usr/bin/env python3
""" module test_client.py """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Any
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Any) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.
        Args:
            org_name: The name of the organization.
            mock_get: Mocked get_json function.
        """
        test_client: GithubOrgClient = GithubOrgClient(org_name)
        test_return: Any = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once()
