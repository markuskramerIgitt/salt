"""
    :codeauthor: Rupesh Tare <rupesht@saltstack.com>
"""


import os.path

import salt.modules.key as key
import salt.utils.crypt
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.mock import MagicMock, patch
from tests.support.unit import TestCase


class KeyTestCase(TestCase, LoaderModuleMockMixin):
    """
    Test cases for salt.modules.key
    """

    def setup_loader_modules(self):
        return {key: {}}

    def test_finger(self):
        """
        Test for finger
        """
        with patch.object(os.path, "join", return_value="A"):
            with patch.object(salt.utils.crypt, "pem_finger", return_value="A"):
                with patch.dict(
                    key.__opts__,
                    {"pki_dir": MagicMock(return_value="A"), "hash_type": "sha256"},
                ):
                    self.assertEqual(key.finger(), "A")

    def test_finger_master(self):
        """
        Test for finger
        """
        with patch.object(os.path, "join", return_value="A"):
            with patch.object(salt.utils.crypt, "pem_finger", return_value="A"):
                with patch.dict(key.__opts__, {"pki_dir": "A", "hash_type": "sha256"}):
                    self.assertEqual(key.finger_master(), "A")
