# import re
# from werkzeug.security import check_password_hash
# from typing import TypedDict
# from dataclasses import dataclass
# from ..models.db_models import Users
#
#
# @dataclass
# class BoolResponse:
#     passed: bool
#     msg: str
#
#
# class AuthenticationMessages:
#     AccessDenied: str = "You do not have access to this page."
#
#     UserUpdated: str = "User Updated"
#
#     LoggedIn: str = "Logged In."
#
#     UnknownUser: str = "User not registered."
#
#     SuccessCreateUser: str = "User Created."
#
#     UserExists: str = "Emails already exists."
#
#     InvalidEmail: str = "Invalid Randox Email."
#
#     InvalidPassword: str = "Invalid Password."
#
#     InconsistentPassword: str = "Passwords Don't Match."
#
#     PasswordUpdated: str = "Password Updated"
#
#
# class UserLogin(TypedDict):
#     email: str
#     password: str
#
#
# class UserInfo(UserLogin):
#     first_name: str
#     last_name: str
#     password_rep: str
#
#
# class UserValidator:
#     _password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
#     _randox_domain = "@randox.com"
#
#     @staticmethod
#     def validate_user_login(user: Users | None, pw: str) -> BoolResponse:
#         if user is None:
#             return BoolResponse(passed=False, msg=AuthenticationMessages.UnknownUser)
#         return BoolResponse(
#             passed=check_password_hash(user.PasswordHash, pw),
#             msg=AuthenticationMessages.InvalidPassword,
#         )
#
#     def validate_user(self, user_info: UserInfo) -> BoolResponse:
#         msg: str = ""
#         passed: bool = False
#
#         if not self._check_email(user_info["first_name"], user_info["email"]):
#             msg = AuthenticationMessages.InvalidEmail
#
#         elif not self._check_passwords_match(user_info["password"],
#                                              user_info["password_rep"]):
#             msg = AuthenticationMessages.InconsistentPassword
#
#         else:
#             passed = True
#
#         return BoolResponse(passed=passed, msg=msg)
#
#     def create_user(self):
#
#
#
#
#
#     @staticmethod
#     def _check_passwords_match(word1: str, word2: str) -> bool:
#         return word1 == word2
#
#     def _check_password_regex(self, word: str) -> bool:
#         return re.match(self._password_regex, word) is not None
#
#     def _check_email(self, name: str, email: str) -> bool:
#         return (
#             email.lower().startswith(name.lower())
#             and email.lower().endswith(self._randox_domain)
#         )
#
#     def validate_new_password(self, form: dict[str, str]) -> BoolResponse:
#         if self._check_passwords_match(form["pw1"], form["pw2"]):
#             pass
#         elif self._check_password_regex(form["pw1"]):
#             pass
#         else:
#             pass
#         return BoolResponse(passed=True, msg=msg)
#
