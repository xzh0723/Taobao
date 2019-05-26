import time
import random

appKey = '12574478'
cookie = 'JSESSIONID=8F01EE33D3B2B0882FCAC25D107FEE2E; cna=vFJwFYAqyRUCAXb6mYJCrFI8; enc=JLqySlUSM%2FVolLOVv1UDwDdev%2BXH40f7cJrOJEPvOo5xxqbIzvQH8MPvjgr2MjFYjKreWcjUTsVOEs62RR1ozg%3D%3D; isg=BGtrPAVOs1jXu--M8adQnJpx-Y-VKH9pwdh-dd3pZaoAfIjeZVQNUo6e0ny3x9f6; t=b414a9fa4524b91dbe1f40c8dfc12403; _m_h5_tk=bcf3c86f59efa6e8f77267c68c66a119_1558863491544; _m_h5_tk_enc=925d6d14875fb1003c1d8a6a7d07cbe9; l=bBgj0sdRv7nJK86tBOfwNuI8aG79FIOV1kPzw4_GXICP_gfH5FfFWZtweE8MC31Va6FJR3PS1JJJByT7cyUIh; um=GF0EA6924C43F47D5E2B6BB9C820D5668BF4070; cookie2=1ab2eeff88fb992b67f12582a8ac58f5; v=0; _tb_token_=7b0585b0efbb4; ockeqeudmj=lGdbbfc%3D; munb=2038739682; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BtPLNWCRWyXf7cyMUwPnOYMAwcq65%2BAbgbzY%3D; _w_app_lg=19; unb=2038739682; sg=%E4%B8%B62b; _l_g_=Ug%3D%3D; skt=678965cab68ea3c1; uc1=cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=URm48syIIVrSKA%3D%3D&cookie14=UoTZ7H0y5DLMtg%3D%3D; cookie1=W8zKdT4ZJ%2FsFpEdkKvoq0lkIojZWjc567pY3OoT%2FJ1s%3D; csg=58cd2b1d; uc3=vt3=F8dBy3vOz0wd0VHH10A%3D&id2=UUjSXbeGYmRHvg%3D%3D&nk2=odrzK7YqUe%2BZLpqekcWZcw%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=%5Cu843D%5Cu53F6%5Cu6210%5Cu53EA%5Cu5F71%5Cu6210%5Cu5355%5Cu4E36; lgc=%5Cu843D%5Cu53F6%5Cu6210%5Cu53EA%5Cu5F71%5Cu6210%5Cu5355%5Cu4E36; _cc_=WqG3DMC9EA%3D%3D; dnk=%5Cu843D%5Cu53F6%5Cu6210%5Cu53EA%5Cu5F71%5Cu6210%5Cu5355%5Cu4E36; _nk_=%5Cu843D%5Cu53F6%5Cu6210%5Cu53EA%5Cu5F71%5Cu6210%5Cu5355%5Cu4E36; cookie17=UUjSXbeGYmRHvg%3D%3D; ntm=0'
url = 'https://m.tb.cn/h.eWpEcRD?sm=24a58d'

t = str(int(time.time() * 1000))

with open('./ua.log', 'r', encoding='utf-8') as f:
    random_ua = random.choice(f.read().split('\n'))

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'user-agent': random_ua,
    'accept': '*/*',
    'referer': 'https://h5.m.taobao.com/?sprefer=sypc00',
    'authority': 'h5api.m.taobao.com',
}

proxy_url = 'http://api.http.niumoyun.com/v1/http/ip/get?p_id=228&s_id=2&u=AmFVNwE5B2FSYwAuB0kHOA8gVWldZQsaBVJUUFNV&number=1&port=1&type=1&map=1&pro=0&city=0&pb=1&mr=2&cs=1'

MONGO_URI = 'localhost'
MONGO_PORT = 27017
