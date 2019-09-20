"""
Example of connecting to edvards oracle instance
Stanislav Vohnik 2019-08-21
"""
from os import environ
from sqlalchemy import create_engine
import pandas as pd
from keyring import get_password as pswd

# we have to point to oracle client directory
environ['PATH'] = 'C:/oracle/instantclient_19_3;%PATH%'

HOST = 'awor-pddwhdb01'
USER = "stanislav_vohnik"
SID = 'dwhprd'
URL = f'oracle://{USER}:{pswd(HOST, USER)}@{HOST}/{SID}'

# SQL Alchemy Engine
ENGINE = create_engine(URL)

# PAndas DataFrame
DF = pd.read_sql('select * from all_tables', ENGINE)
print(DF.info())
