# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
#
# Server="RDX-SQL-DEV03"
# Database="RHUSA_Service_Contracts_DEV"
# Driver="ODBC Driver 17 for SQL Server"
# Database_Con= f'mssql://@{Server}/{Database}?driver={Driver}'
#
#
# engine = create_engine(Database_Con)
# con = engine.connect()
#
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# # Dependancy
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()