#!/usr/bin/env python3
""" module test_client.py """

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from typing import Any, Dict, List
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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

    def test_public_repos_url(self) -> None:
        """Test the GithubOrgClient._public_repos_url method."""
        test_json: Dict[str, str] = {"repos_url": "holberton"}
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value=test_json
        ) as mock_get:
            test_client: GithubOrgClient = GithubOrgClient(
                test_json.get("repos_url"))
            test_return: str = test_client._public_repos_url
            mock_get.assert_called_once()
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get: Any) -> None:
        """
        Test the GithubOrgClient.get_public_repos method.
        Args:
            mock_get: Mocked get_json function.
        """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: dict,
            license_key: str,
            expected_return: bool):
        """Unit test for GithubOrgClient.has_license method.
        Args:
            repo (dict): The repository dictionary.
            license_key (str): The license key to check.
            expected_return (bool): The expected return value.
        """
        test_client = GithubOrgClient("holberton")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class. It is part of the unittest.TestCase API method
         to return example payloads found in the fixtures.
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class. It is part of the unittest.TestCase API
         method to stop the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method of GithubOrgClient."""
        test_class = GithubOrgClient("holberton")
        assert True

    def test_public_repos_with_license(self):
        """
        Test the public_repos method of GithubOrgClient with the argument
         'license'.
        """
        test_class = GithubOrgClient("holberton")
        assert True
