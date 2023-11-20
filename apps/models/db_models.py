from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column, Session
from apps import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from typing import TypedDict

# UserRoles = Table(
#     "UserRoles",
#     db.metadata,
#     Column("UserID", ForeignKey("Auth.Users.id"), primary_key=True),
#     Column("RoleID", ForeignKey("Auth.Roles.id"), primary_key=True),
#     schema="Auth"
# )


class Roles(db.Model):
    __table_args__ = {"schema": "Auth"}
    id: Mapped[int] = mapped_column(primary_key=True)
    RoleTitle: Mapped[str]

    # users: Mapped["Users"] = relationship(back_populates="roles")

    def __eq__(self, other):
        return self.RoleTitle == other.RoleTitle


class KnownRoles(TypedDict):
    Standard: Roles
    Manager: Roles
    Support: Roles
    Dev: Roles


ROLES: KnownRoles = {r.RoleTitle: r for r in db.session.query(Roles).all()}


class Users(db.Model, UserMixin):
    __table_args__ = {"schema": "Auth"}
    UserEmail: Mapped[str]
    PasswordHash: Mapped[str]
    FirstName: Mapped[str]
    LastName: Mapped[str]
    IsActive: Mapped[bool]
    Role: Mapped[int] = mapped_column(ForeignKey("Auth.Roles.id"))

    roles: Mapped[list["Roles"]] = relationship()

    def has_role(self, role: str) -> bool:
        # print(role)
        user_role = self.roles.RoleTitle

        print(user_role, print(role))

        return bool(user_role == role)

    def update_password(self, new_password: str, session: Session = db.session) -> None:
        self.PasswordHash = generate_password_hash(new_password)
        session.commit()

    def deactivate(self, session: Session = db.session) -> None:
        self.IsActive = False
        session.commit()
