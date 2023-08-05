# coding: utf-8

"""
    printnanny-api-client

    Official API client library for printnanny.ai  # noqa: E501

    The version of the OpenAPI document: 0.121.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import printnanny_api_client
from printnanny_api_client.api.accounts_api import AccountsApi  # noqa: E501
from printnanny_api_client.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = printnanny_api_client.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts2fa_auth_email_create(self):
        """Test case for accounts2fa_auth_email_create

        """
        pass

    def test_accounts2fa_auth_token_create(self):
        """Test case for accounts2fa_auth_token_create

        """
        pass

    def test_accounts_email_waitlist_create(self):
        """Test case for accounts_email_waitlist_create

        """
        pass

    def test_accounts_login_create(self):
        """Test case for accounts_login_create

        """
        pass

    def test_accounts_logout_create(self):
        """Test case for accounts_logout_create

        """
        pass

    def test_accounts_password_change_create(self):
        """Test case for accounts_password_change_create

        """
        pass

    def test_accounts_password_reset_confirm_create(self):
        """Test case for accounts_password_reset_confirm_create

        """
        pass

    def test_accounts_password_reset_create(self):
        """Test case for accounts_password_reset_create

        """
        pass

    def test_accounts_registration_create(self):
        """Test case for accounts_registration_create

        """
        pass

    def test_accounts_registration_resend_email_create(self):
        """Test case for accounts_registration_resend_email_create

        """
        pass

    def test_accounts_registration_verify_email_create(self):
        """Test case for accounts_registration_verify_email_create

        """
        pass

    def test_accounts_user_nkey_retrieve(self):
        """Test case for accounts_user_nkey_retrieve

        """
        pass

    def test_accounts_user_partial_update(self):
        """Test case for accounts_user_partial_update

        """
        pass

    def test_accounts_user_retrieve(self):
        """Test case for accounts_user_retrieve

        """
        pass

    def test_accounts_user_update(self):
        """Test case for accounts_user_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
