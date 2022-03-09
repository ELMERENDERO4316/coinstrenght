import math,requests,json,sys
from io import StringIO
apikey = ""
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headerss = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': apikey}
parameterss = {'start':'1','limit':'5000','convert':'USD'}
data = requests.get(url, headers=headerss).json()
databella = json.dumps(data,indent=4)
listabella = databella.split()
i=0
symbols = []
percent = []
price = []
rank = []
while (i<len(listabella)):
    if(listabella[i]=='"platform":' and listabella[i+1]=='{'):
        listabella[i+1:i+15] = "void"

    elif(listabella[i]=='"percent_change_24h":' and listabella[i+1]!='null,' ):
        percent.append(listabella[i+1])
        i=i+1
    elif(listabella[i]=='"name":' and listabella[i+1]!='null,' ):
        symbols.append(listabella[i+1])
        i=i+1
    elif(listabella[i]=='"price":' and listabella[i+1]!='null,' ):
        price.append(float(listabella[i+1].strip(',')))
        i=i+1
    elif(listabella[i]=='"cmc_rank":' and listabella[i+1]!='null,' ):
        rank.append(listabella[i+1])
        i=i+1
    else:
        i=i+1

compiledData = list(zip(symbols, price, percent))
compiledData.sort(key=lambda x:x[2])

print(compiledData)
compileddatabella = json.dumps(compiledData,indent=4)
print(type(compileddatabella))
with open("output.txt","w+") as o:
    o.write(compileddatabella)
    print("linea scritta!")






