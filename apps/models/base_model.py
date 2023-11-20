import sqlalchemy as sa
from flask_sqlalchemy.model import Model
from sqlalchemy.orm import declared_attr


# Before implementing this model the database need updating to replace the id field.
# Implement by db = SQLAlchemy(model_class=BaseModel) in apps/__init__.py
class BaseModel(Model):
    @declared_attr
    def id(cls):
        return sa.Column(sa.Integer, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    @classmethod
    def check_exists(cls, **kwargs) -> bool:
        return cls.query.filter_by(**kwargs).first() is not None
