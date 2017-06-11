import urllib
import urllib.request


url = "http://m2.quote.eastmoney.com/h5stock/6017661.html"
full_url = url

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')


print(data)
