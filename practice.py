from urllib import request, urlopen
from urllib import urlencode, quote_plus

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'BKuHZJ8L9XAchad4FpWJRKdC7Se202%2B4Kz318LRfX0Vpdz3Kp3aH7nq1Hu49yXajvS%2BuWKADnJMcrpLW1a9tmA%3D%3D', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'XML', quote_plus('base_date') : '20151201', quote_plus('base_time') : '0600', quote_plus('nx') : '18', quote_plus('ny') : '1' })

request = request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)