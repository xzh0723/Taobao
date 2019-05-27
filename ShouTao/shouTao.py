import random
import requests
import re
import execjs
from pyquery import PyQuery as pq
import json
from ShouTao.config import *
from ShouTao.mongodb import MongoDB
from ShouTao.proxy import get_random_proxy

class ShouTao():

    def __init__(self, page):
        self.cookie = cookie
        self.url = url
        self.page = page
        self.token = re.search('_m_h5_tk=(.*?);', self.cookie).group(1).split('_')[0]
        self.t = t
        self.appKey = appKey
        self.proxies = get_random_proxy()
        self.db = MongoDB()

    def get_redireact_url(self):
        """
        拿到重定向后的url
        :return:
        """
        res = requests.get(self.url, headers=headers)
        redireact_url = re.search("var url = '(.*?)';", res.text, re.S).group(1)
        return redireact_url

    def get_data(self, redireact_url):
        """
        获取搜索参数data
        :param redireact_url: 重定向后的url
        :return:
        """
        r = requests.get(redireact_url, headers=headers)
        # print(r.text)
        doc = pq(r.text)
        script = doc('script').text()
        # print(script)
        x = script.split(';')[0]
        # print(x)
        y = x.split('=')[1]
        # print(y)
        lis = re.findall('params:\{ (.*?) \}', y, re.S)
        #print(lis)
        lis.remove('}')
        #print(lis)
        data = {}
        for li in lis:
            items = li.split(',')
            for item in items:
                key = item.split(':')[0].replace("'", '').replace(' ', '')
                value = item.split(':')[1].replace("'", '').replace(' ', '')
                data[key] = value
        data['page'] = self.page
        data = json.dumps(data)
        print(f'data: {data}')
        return data

    def get_sign(self, data):
        """
        执行js，构造sign参数
        :param data:
        :return:
        """
        with open('sign.js', 'r', encoding='utf-8') as f:
            js = f.read()

        ctx = execjs.compile(js)
        sign = ctx.call('Y', self.token + '&' + t + '&' + self.appKey + '&' + data)
        print(f'sign: {sign}')
        return sign

    def search(self, data, sign):
        """
        抓取页面
        :param data: 搜索参数
        :param sign: 每页的sign参数都不相同
        :return:
        """
        params = {
            'jsv': '2.3.16',
            'appKey': appKey,
            't': t,
            'sign': sign,
            'api': 'mtop.taobao.wsearch.h5search',
            'v': '1.0',
            'H5Request': 'true',
            'ecode': '1',
            'AntiCreep': 'true',
            'AntiFlool': 'true',
            'type': 'jsonp',
            'dataType': 'jsonp',
            'callback': 'mtopjsonp2',
            'data': data
        }

        headers['cookie'] = self.cookie

        response = requests.get('https://acs.m.taobao.com/h5/mtop.taobao.wsearch.h5search/1.0/?', headers=headers,
                                params=params)
        # print(response.text)
        html = re.search('mtopjsonp2\((.*?)\)', response.text).group(1)
        result = json.loads(html)
        # print(result)
        listItem = result['data']['listItem']
        for item in listItem:
            print(item)
            self.db.save(item)

    def main(self):
        redireact_url = self.get_redireact_url()
        data = self.get_data(redireact_url)
        sign = self.get_sign(data)
        self.search(data, sign)

if __name__ == '__main__':
    max_page = input('请输入你要下载最大页码>>>')
    for page in range(1, int(max_page) + 1):
        shoutao = ShouTao(page)
        shoutao.main()
        # 设置抓取延时
        time.sleep(random.random() * 10)
