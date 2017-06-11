import urllib
import urllib.request

# main
if __name__ == '__main__':
	url = "http://m2.quote.eastmoney.com/h5stock/"
rl = input("请输入代码")
full_url = url + rl + "1.html"
data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
