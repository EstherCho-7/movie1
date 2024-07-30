from movie.api.call import gen_url,req, get_key, req2df, list2df, save2df
import pandas as pd

def test_private_key():
    key=get_key()
    assert key

def test_gen_url(): 
    url=gen_url()
    assert True
    assert "http" in url
    assert "kobis" in url

def test_req():
    code, data=req()
    assert code == 200

    code, data=req("20230101")
    assert code == 200

def test_dataframe():
    l=req2df(load_dt="20120101")
    assert len(l)>0
    #v=l[0]
    #assert 'rnum' in v.keys() 
    #assert v['rnum']=='1'
   # dataframe=req2dataframe()
   # if len(dataframe)>=1:
   #     print(dataframe)
   # else:
   #     print("Nope")

def test_list2df():
    df = list2df()
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns

def test_save2df():
    df = save2df(load_dt='20120101')
    assert isinstance (df, pd.DataFrame)
    assert 'load_dt' in df.columns



