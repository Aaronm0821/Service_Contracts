import unittest
from apps.auth.utils import UserValidator, AuthenticationMessages, BoolResponse


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.form_dict = {}

    def test_when_invalid_email(self):
        # Arrange
        self.form_dict["email"] = "Invalid@Email"

        # Act
        result = BoolResponse(passed=False, msg="")

        # Assert
        self.assertFalse(result.passed)
        self.assertEqual(result.msg, AuthenticationMessages.InvalidEmail)
