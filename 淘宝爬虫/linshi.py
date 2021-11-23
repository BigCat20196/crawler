# -*- coding: utf-8 -*-#
# Author: cjf
import re
import os
import time
import random

import requests
from bs4 import BeautifulSoup
from urllib import parse

cookies = {"_samesite_flag_":"true","_tb_token_":"5fbe314b3eed","alitrackid":"www.taobao.com","cna":"zDYvF/cMYhgCAWVdQYIM0Og2","cookie2":"1e6bf57baa6dd1b20ed4d099449ef401","enc":"IwiJ3lt+jvzUQ8ChUAzkOyVnM7M835Pb//JRWipFNi4FELOf4Tzz/h3NYf/iZxJrV1Ky0hRCTK9CQhWteUBo0Q==","hng":"CN|zh-CN|CNY|156","isg":"BK-vc9nDLcYMmynV6M-53JMHPcO5VAN2sYgNScE8TZ4lEM8SySXaxmtCkoAuc9vu","JSESSIONID":"2CFC77D50381E399FD32A85A65FC8409","l":"eBLBsd-4QDdSTGF2BOfChurza779SIOYYuPzaNbMiOCP9_5p5yzCWZxYcB89Cn1VhsZ9R3yblDgJBeYBqS24n5U62j-laskmn","lastalitrackid":"www.taobao.com","sgcookie":"ELof2dZBpiDBPHKZOV+lS","t":"900748a1e21a05857257ec54966062fc","tfstk":"cY0hBROA9DrCuTxakeaIZACFH2ylactUd4uZ72GbjUzK5pu3_sVlbi7N8C2KFyS5.","thw":"cn","tracknick":"","v":"0"}

cookie = {
    'cookie2': '1530c35f48b12d9af4a7796bf4dea35c',
    't': 'd56bb5e9394fbf946734de31ac5f2713',
    'cna': 'pKDhGLpVmXoCAafc/wl54+6a',
    'v': '0',
    '_samesite_flag_': "true",
    'hng': 'CN|zh-CN|CNY|156',
    'thw': 'cn',
    'xlly_s': '1',
    'sgcookie': 'E100P3m3MDS9LFw9g+FVjz8NeKRCVEA7fCqaYYpcsxxsvWm8VYEihV9DkZRHZDoyylLjGM8M5YwE3nXTmzfpmDYXopHjvYMP0t/6d2gGRPmT7q=',
    'uc3': 'lg2=VFC/uZ9ayeYq2g==&nk2=AmulwLJn&vt3=F8dCujpSuMKNymA6g7w=&id2=UUphyus9/2+txg==',
    'csg': '0afd1ef6', 'lgc': 'az5290',
    'cancelledSubSites': 'empty', 'dnk': 'az5290',
    'skt': '5125326cf8aac34b; existShop=MTYzNjY4MzY5Mw==',
    'uc4': 'id4=0@U2grEa2GZyTY3R7luUZ1L3LYxj6N&nk4=0@AIBs7jBdI+E/tD4nE7XEQ5I=',
    'tracknick': 'az5290', '_cc_': 'V32FPkk/hw==',
    'enc': 'nokQPdfrtgkCdw1EXNPWiWi/7obCEJzDP+EWjib0at6Vx4nopWKMvylua9ofY3G9NfZiYqk4wobjPyo9g+9+9g==',
    'mt': 'ci=26_1', '_tb_token_': 'e183ee86b95ee',
    '_m_h5_tk': '04fc9aa8cbb9bbc12f6fbf91c00474f5_1636704728707',
    '_m_h5_tk_enc': 'd892128d6026862a7ee71065c4ea44c9',
    'tfstk': 'cRkRBvDMaEYu5krxbbdmd7YEmg0RaKTLlgahpnG2wVlAG_JWesAZIAQtxQZQ7zKA.',
    'l': 'eBE-utTVgmioI19QBO5ZPurza77taIRb8sPzaNbMiInca12P_F6lRNCdT6uH8dtjgtCxqeKrrNYcMRUXSMUKb14Ki2MzH13bZxvO.',
    'isg': 'BNTUhMY5SQnq891G0Tj17DfbpRJGLfgXcN1sNG61td_iWXWjlz7Gp8ATXVFBoTBv',
    'uc1': 'pas=0&cookie21=W5iHLLyFe3xm&cookie14=Uoe3ccipK6d5Cg==&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA==&existShop=false'
}



headers = {
    "Host": "s.taobao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101",
    "Referer": "https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
 }

headers2 = {
    # ':authority': 'item.taobao.com',
    # ':path': '/item.htm?id=',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44',
    'cookie': 'cookie2=1530c35f48b12d9af4a7796bf4dea35c; t=d56bb5e9394fbf946734de31ac5f2713; cna=pKDhGLpVmXoCAafc/wl54+6a; v=0; _samesite_flag_=true; hng=CN|zh-CN|CNY|156; thw=cn; sgcookie=E100P3m3MDS9LFw9g+FVjz8NeKRCVEA7fCqaYYpcsxxsvWm8VYEihV9DkZRHZDoyylLjGM8M5YwE3nXTmzfpmDYXopHjvYMP0t/6d2gGRPmT7q0=; uc3=lg2=VFC/uZ9ayeYq2g==&nk2=AmulwLJn&vt3=F8dCujpSuMKNymA6g7w=&id2=UUphyus9/2+txg==; csg=0afd1ef6; lgc=az5290; cancelledSubSites=empty; dnk=az5290; skt=5125326cf8aac34b; existShop=MTYzNjY4MzY5Mw==; uc4=id4=0@U2grEa2GZyTY3R7luUZ1L3LYxj6N&nk4=0@AIBs7jBdI+E/tD4nE7XEQ5I=; tracknick=az5290; _cc_=V32FPkk/hw==; _m_h5_tk=21868dcb6a4aff92190a79637e34a5ea_1637654905920; _m_h5_tk_enc=335f833d5f5047cdf01bd13de51d5712; xlly_s=1; mt=ci=-1_0; _tb_token_=ebee864375378; enc=ubNk5hcCs4AhjR0wyrCSlgVn5W9tfklKQn7SG//xhvR6xvUMhFE3Fm4waEzzWouprxi7s/hwMgodUiK5crPRsg==; tfstk=cnaCBp2VtpvCHPjy8W1wTJc8ql3VZORjNMM3OuQHsU2VWxVCig8qhO0aqL3rwf1..; isg=BPX1pll8-ChrgByFKFfEP45sBHGvcqmEOaptt3casWy7ThVAP8K5VANMnBL4DsE8; l=eBE-utTVgmioIVkbBOfwourza77OSIRAguPzaNbMiOCP_Y5M5CcdW6BKedLHC3GVh6SHR3ulSEfvBeYBqS0H3CPie5DDwQHmn; uc1=existShop=false&pas=0&cookie21=W5iHLLyFe3xm&cookie14=Uoe3cOtRsIVIdw==&cookie16=W5iHLLyFPlMGbLDwA+dvAGZqLg=='
}

target = ''

try:
    dir_name = 'tb_img'
    os.mkdir(dir_name)
except:
    pass

def start():
    res = requests.get(url=target, headers=headers, cookies=cookies)
    # soup = BeautifulSoup(res.text, 'html.parser')
    # goods = soup.select('div[class="item J_MouserOnverReq  "]')
    # //*[@id="mainsrp-itemlist"]/div/div/div[1]/div[4]
    # print(res.status_code)
    nids = re.findall('"nid":"(.*?)"', res.text)
    # ok: 652195148849
    item_base_url = 'https://item.taobao.com/item.htm?id='
    # nids = ['652195148849', '545861910789', '602983570199']
    for nid in nids:
        time.sleep(0.5)
        # item_url = item_base_url+nid
        item_url = item_base_url+nid
        res1 = requests.get(url=item_url, headers=headers2)
        if '扫码登录更安全' in res1.text:
            continue
        print(nid)
        title = re.findall('<title>(.*?)</title>', res1.text)[0]

    print("111111111111111")
    # urls = re.findall('"pic_url":"(.*?)"', res.text)
    # print(urls)
    # print(len(urls))
    for url in urls:
        time.sleep(1)
        img_down(url)

def start1():
    res = requests.get(url=target, headers=headers, cookies=cookies)

    titles = re.findall('pid":".*?","title":"(.*?)",', res.text)
    prices = re.findall(',"view_price":"(.*?)",', res.text)
    urls = re.findall('"pic_url":"(.*?)"', res.text)
    sales = re.findall('"view_sales":"(\d{1,4}).人付款",', res.text)

    prices = [int(float(i)) for i in prices]
    sales = [int(i) if int(i) < 100 else int(i)+random.randint(-50, 50) for i in sales]
    clicks = [int(i*(1+random.random())) for i in sales]
    haopins = [int(i*(random.randint(4, 8)+random.random())/10) for i in sales]
    chappins = [int(i*(random.randint(0, 4)+random.random())/10) for i in sales]
    shoucangs = [int(i*(random.randint(4, 8)+random.random())/10) for i in haopins]

    file_names = [f_name.split('/')[-1] for f_name in urls]
    le = min(len(titles), len(urls), len(prices), len(sales))
    for i in range(le):
        pass

    print(urls)
    print(len(urls))
    for url in urls:
        time.sleep(1)
        img_down(url)



def img_down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        # "Referer": "https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
        "Host":"g-search1.alicdn.com",
    }
    res = requests.get("http:"+url,headers=headers)
    print(res.status_code)
    file_name = url.split('/')[-1]
    with open(dir_name+'\\'+file_name,'wb')as f:
        print(url,'开始下载...',end="")
        f.write(res.content)
        print('下载完成')



if __name__ == '__main__':
    # img_down(url)
    # search = input("输入想爬的商品名称")
    search = '电脑'
    if not search:
        print("输入错误，程序结束")
    search_ = parse.unquote(search)
    target = 'https://s.taobao.com/search?q='+search_+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200610&ie=utf8'
    start1()

