import sys
sys.path.append("./")
import pandas as pd
import numpy as np
import pymssql
from sqlalchemy import create_engine


if __name__ == "__main__":
    df = pd.read_csv("AQS_Sites.txt", sep="|", header=0)
    datatype = {'State_Code': str,
    'County_Code': 'int64',
    'Site_Number':'int64',
    'Latitude': 'float64',
    'Longitude': 'float64',
    'Datum': str,
    'Elevation': 'float64',
    'Land Use': str,
    'Location Setting': str,
    'Site Established Date': 'datetime64',
    'Site Closed Date': 'datetime64',
    'Met Site State Code': 'float64',
    'Met Site County Code': 'float64',
    'Met Site Site Number': 'float64',
    'Met Site Type':str,
    'Met Site Distance': 'float64',
    'Met Site Direction': str,
    'GMT Offset': 'int64',
    'Owning Agency': str,
    'Local_Site_Name': str,
    'Address': str,
    'Zip_Code': 'int64',
    'State_Name': str,
    'County_Name': str,
    'City_Name': str,
    'CBSA_Name': str,
    'Tribe_Name': str,
    'Extraction Date': 'datetime64'}

    df.fillna(0, inplace=True)
    df = df.astype(datatype)
    conn = pymssql.connect(server='db', user='sa', password='root', port="1433",database='Weather')
    connection_String= "mssql+pymssql://sa:password@db/Weather?charset=utf8"
    conn = create_engine(connection_String)
    df.to_sql('AQS_Sites', con=conn,  if_exists='replace', index=False)