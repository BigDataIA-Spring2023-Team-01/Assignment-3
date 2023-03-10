import sqlite3
import pandas as pd
import requests
from pathlib import Path

mod_path = Path(__file__).parent
relative_path_2 = '../data/s3_goes.dbo'
src_path_2 = (mod_path / relative_path_2).resolve()

def query_into_dataframe():
    conn = sqlite3.connect(src_path_2)
    cursor = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM folders", conn)
    conn.close()

def retieve_year():
    conn = sqlite3.connect(src_path_2)
    cursor = conn.cursor()
    query = "SELECT distinct year FROM folders"
    tdf = pd.read_sql_query(query, conn)
    df = [x for x in tdf]
    conn.close()
    return tdf


def retieve_day_of_year(year):
    conn = sqlite3.connect(src_path_2)
    cursor = conn.cursor()
    query = "SELECT distinct day_of_year FROM folders where year = ?"
    tdf = pd.read_sql_query(query, conn,params=(year,))
    df = [x for x in tdf]
    conn.close()
    return tdf

def retieve_hour(year,day_of_year):
    conn = sqlite3.connect(src_path_2)
    cursor = conn.cursor()
    query = "SELECT distinct hour FROM folders where year = ? and day_of_year = ?"
    tdf = pd.read_sql_query(query, conn,params=(year,day_of_year))
    df = [x for x in tdf]
    conn.close()
    return tdf

def log_file_download(file_name, timestamp,dataset):
    conn = sqlite3.connect(src_path_2)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS file_logs (file_name text, timestamp text,dataset text)")
    cursor.execute("INSERT INTO file_logs VALUES(?,?,?)",(file_name,timestamp,dataset))    
    conn.commit()
    conn.close()

df = retieve_year()
print(df)