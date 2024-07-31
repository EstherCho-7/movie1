import requests
import os
import pandas as pd

def req(load_dt="20120101", url_param={}):
    #url=gen_url('20240720')
    url=gen_url(load_dt, url_param)
    r=requests.get(url)
    code =  r.status_code
    data = r.json()
    #print(data)
    return code, data

def gen_url(dt="20120101", url_param={}):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key=get_key() 
    url=f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_param.items():
        # url=url+f"&multiMovieYn=N"
        url = url + f"&{k}={v}"

    print("*=" * 30)
    print(url)
    print("*=" * 30)
    return url 

def get_key():
    """must get key"""
    key=os.getenv("MOVIE_API_KEY")
    return key

def req2df(load_dt, url_param={}):
    _, data = req(load_dt, url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
#    l = [
#            {'rnum':'1', 'rank':'1'},
#            {'rnum':'2', 'rank':'1'},
#            {'rnum':'3', 'rank':'1'}
#
#            ]
    df = pd.DataFrame(l)
    return df 

def list2df(load_dt='20120101', url_param={}):
    l=req2df(load_dt, url_param)
    df = pd.DataFrame(l)
    return df

def save2df(load_dt='20120101', url_param={}):
    """"airflow"""
    df=list2df(load_dt=load_dt, url_param=url_param)
    df['load_dt']=load_dt
    print(df.head())
    # add column 'load_dt' in df (forman: YYYYMMDD)
    # saving file, partitioning (standard: load_dt)
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])
    return df

def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet"):
    df=pd.read_parquet(f'{path}/load_dt={load_dt}')
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
#    for c in num_cols:
#        df[c]=pd.to_numeric(df[c])

    df[num_cols]=df[num_cols].apply(pd.to_numeric)
    return df
# same as for

def echo(yaho):
    return yaho
