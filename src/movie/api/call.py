import requests
import os
import pandas as pd

def req(load_dt="20120101"):
    #url=gen_url('20240720')
    url=gen_url(load_dt)
    r=requests.get(url)
    code =  r.status_code
    data = r.json()
    print(data)
    return code, data

def gen_url(load_dt="20120101"):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key=get_key() 
    url=f"{base_url}?key={key}&targetDt={load_dt}"
    return url 

def get_key():
    """must get key"""
    key=os.getenv("MOVIE_API_KEY")
    return key

def req2df(load_dt):
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
#    l = [
#            {'rnum':'1', 'rank':'1'},
#            {'rnum':'2', 'rank':'1'},
#            {'rnum':'3', 'rank':'1'}
#
#            ]
    df = pd.DataFrame(l)
    return df 

def list2df(load_dt='20120101'):
    l=req2df(load_dt)
    df = pd.DataFrame(l)
    return df

def save2df(load_dt='20120101'):
    """"airflow"""
    df=list2df(load_dt)
    df['load_dt']=load_dt
    print(df.head(5))
    # add column 'load_dt' in df (forman: YYYYMMDD)
    # saving file, partitioning (standard: load_dt)
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])
    return df

def echo(yaho):
    return yaho
