# -*- coding:utf-8 -*-

import urllib
import urllib.request
import re



def rePatern(webData):
    nameP = re.compile(r'<span class="name">(.*?)</span>')
    name = nameP.findall(webData)
    # xjP = re.compile(r'<span class="xj".*?>(.*?)</span>')
    # # xj = xjP.findall(webData)
    # zdfP = re.compile(r'<span class="zdf">(.*?)</span>')
    # zdf = zdfP.findall(webData)
    # hslP = re.compile(r'<span class="hsl">(.*?)</span>')
    # hsl = hslP.findall(webData)
    sylP = re.compile(r'<span class="syl">(.*?)</span>')
    syl = sylP.findall(webData)
    zszP = re.compile(r'<span class="zsz">(.*?)</span>')
    zsz = zszP.findall(webData)

    return {
        "name": name,
        # "现价": xj
        # "涨跌幅": zdf,
        # "换手率": hsl,
        "市盈率": syl,
        "总市值": zsz
    }



# main
if __name__ == '__main__':
    url = "http://m2.quote.eastmoney.com/h5stock/"

rl = input("请输入代码")
full_url = url + rl + "1.html"
data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')

ite = rePatern(data)

f=open('test.txt','w')
f.write(str(ite))
f.close()

print(ite)
