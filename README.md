﻿# hombre_tools

Fast start:
pip install hombre_tools

## examples:
* Comment sql file with jde filels description:

C:\python -m hombre_tools --action jde_comment  --path "C:\dir_with_sql_files\" --strip_comment true
 
* profile sql select:

c:\python -m hombre_tools --action profile --sql "select * from fact_table" --user dwh_dwh --host awor-pddwgapp01 --sid dwhprd
