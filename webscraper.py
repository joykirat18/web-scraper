import sys
import requests
from bs4 import BeautifulSoup
import wikipedia
import plotly.graph_objects as go
number = input("Number Of Movies ")
inp = []
ans = []
for i in range(int(number)):
	query = input()
	inp.append(query)
for i in range(0, int(number)):
	inr = inp[i]
	a = wikipedia.suggest(inr)
	if(a == None):
		URL = wikipedia.page(inr).url
	else:
		URL = wikipedia.page(inr).url
	print(URL)
	res = requests.get(URL)
	res.raise_for_status()
	wiki = BeautifulSoup(res.text, "html.parser")
	contenttable = wiki.find('table', {"class": "infobox vevent"})
	rows = contenttable.find_all('tr')
	
	for row in rows:
		table = row.find('th')
		if(table != None):
			if(table.text == 'Starring'):
				lis = row.find_all('a')
				temp = []
				for i in lis:
					print(i.text)
					temp.append(i.text)
				ans.append(temp)
dic = {}
for i in range(0, len(ans)):
	for j in range(0,len(ans[i])):
		dic[ans[i][j]] = 0
for i in range(0, len(ans)):
	for j in range(0,len(ans[i])):
		dic[ans[i][j]] = dic[ans[i][j]] + 1
    
label = []
value= []
for x in  dic:
	label.append(x)
	value.append(dic[x])

fig = go.Figure(data=[go.Pie(labels=label, values=value)])
fig.show()
