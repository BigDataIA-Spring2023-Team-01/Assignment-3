
import ast
import sqlite3
import os
import pandas as pd
from pathlib import Path

mod_path = Path(__file__).parent
relative_path_1 = '../data/s3_nexrad.dbo'
src_path_1 = (mod_path / relative_path_1).resolve()



def query_into_dataframe():
    conn = sqlite3.connect(src_path_1)
    cursor = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM folders", conn)
    conn.close()
    return df


def retieve_months(year):
    conn = sqlite3.connect(src_path_1)
    cursor = conn.cursor()
    query = "SELECT distinct month FROM folders where year = ?"
    tdf = pd.read_sql_query(query, conn, params=(year,))
    df = [x for x in tdf]
    conn.close()
    return tdf

def retieve_days(year,month):
    conn = sqlite3.connect(src_path_1)
    cursor = conn.cursor()
    query = "SELECT distinct day FROM folders where year = ? and month = ?"
    tdf = pd.read_sql_query(query, conn,params=(year,month))
    df = [x for x in tdf]
    conn.close()
    return tdf

def retieve_stations(year,month,day):
    conn = sqlite3.connect(src_path_1)
    cursor = conn.cursor()
    query = 'SELECT nexrad_station FROM folders where year = ? and month = ? and day = ?'
    tdf = pd.read_sql_query(query, conn,params=(year,month,day))
    conn.close()
    df = tdf['nexrad_station'][0]
    df1 = ast.literal_eval(df)

    return df1

