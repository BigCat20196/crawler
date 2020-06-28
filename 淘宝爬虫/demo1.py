# -*- coding: utf-8 -*-#
# Author: cjf
import re
import os

import requests
import time
from urllib import parse

cookies = {"_samesite_flag_":"true","_tb_token_":"5fbe314b3eed","alitrackid":"www.taobao.com","cna":"zDYvF/cMYhgCAWVdQYIM0Og2","cookie2":"1e6bf57baa6dd1b20ed4d099449ef401","enc":"IwiJ3lt+jvzUQ8ChUAzkOyVnM7M835Pb//JRWipFNi4FELOf4Tzz/h3NYf/iZxJrV1Ky0hRCTK9CQhWteUBo0Q==","hng":"CN|zh-CN|CNY|156","isg":"BK-vc9nDLcYMmynV6M-53JMHPcO5VAN2sYgNScE8TZ4lEM8SySXaxmtCkoAuc9vu","JSESSIONID":"2CFC77D50381E399FD32A85A65FC8409","l":"eBLBsd-4QDdSTGF2BOfChurza779SIOYYuPzaNbMiOCP9_5p5yzCWZxYcB89Cn1VhsZ9R3yblDgJBeYBqS24n5U62j-laskmn","lastalitrackid":"www.taobao.com","sgcookie":"ELof2dZBpiDBPHKZOV+lS","t":"900748a1e21a05857257ec54966062fc","tfstk":"cY0hBROA9DrCuTxakeaIZACFH2ylactUd4uZ72GbjUzK5pu3_sVlbi7N8C2KFyS5.","thw":"cn","tracknick":"","v":"0"}

headers = {
    "Host": "s.taobao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101",
    "Referer": "https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
 }

target = ''

try:
    dir_name = 'tb_img'
    os.mkdir(dir_name)
except:
    pass

def img_url():
    res = requests.get(url=target,headers=headers,cookies=cookies)
    # print(res.status_code)
    urls = re.findall('"pic_url":"(.*?)"', res.text)
    print(urls)
    # print(len(urls))
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
    search = input("输入想爬的商品名称")
    if not search:
        print("输入错误，程序结束")
    search_ = parse.unquote(search)
    target = 'https://s.taobao.com/search?q='+search_+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200610&ie=utf8'
    img_url()




'''

https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200610&ie=utf8

https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200610&ie=utf8&bcoffset=1&ntoffset=1&p4ppushleft=2%2C48&s=44

https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200610&ie=utf8&bcoffset=-2&ntoffset=-2&p4ppushleft=2%2C48&s=88

https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200610&ie=utf8&bcoffset=-5&ntoffset=-5&p4ppushleft=2%2C48&s=132
'''
'''
实现过程：
1.使用bp挂代理，实现绕过淘宝登录，进行搜索
2.采集cookies和headers信息
3.使用request库进行连接，获取图片url
4.根据url下载图片
'''