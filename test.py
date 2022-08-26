import oracledb
import os

un = os.environ.get("PYTHON_USERNAME")
pw = os.environ.get("PYTHON_PASSWORD")
cs = os.environ.get("PYTHON_CONNECTSTRING")
config_dir = os.environ.get("ORACLE_WALLET_LOCATION")
wallet_password = os.environ.get("ORACLE_WALLET_PW")
wallet_location = os.environ.get("ORACLE_WALLET_LOCATION")

with oracledb.connect(
    user=un,
    password=pw,
    dsn=cs,
    config_dir=wallet_location,
    wallet_location=wallet_location,
    wallet_password=wallet_password,
) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)
