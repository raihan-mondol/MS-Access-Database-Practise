import pyodbc

msa_drivers = [i for i in pyodbc.drivers() if 'ACCESS' in i.upper()]
print(f"MS-Access Drivers :  {msa_drivers}")
