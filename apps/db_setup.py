"""
This file is for manual / raw SQL queries, also provide an Engine for 
Pandas Bind SQL 
"""


import pymssql
from sqlalchemy import create_engine
from apps.config import app_config


CONN = pymssql.connect(
    server=app_config.SERVER,
    user=app_config.USER,
    password=app_config.PASSWORD,
    database=app_config.DATABASE_NAME,
)
CUR = CONN.cursor()

# Include, if required
ENGINE = create_engine(
    f"mssql+pymssql://{app_config.USER}:{app_config.PASSWORD}@{app_config.SERVER}/{app_config.DATABASE_NAME}"
)
