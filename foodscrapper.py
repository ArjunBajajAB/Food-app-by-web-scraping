import requests
from bs4 import BeautifulSoup

class FoodItems:
	def __init__(self,title,info,imgtag):
		self.title=title
		self.info=info
		self.imgtag=imgtag

def scrapinfo(search_item):
	url="https://www.calories.info/food/"
	url=url+search_item
	r=requests.get(url)
	soup=BeautifulSoup(r.content)
	food_items=soup.findAll('div',attrs={"class":"entry-content"})
	results=[]
	for f in food_items:
		title=search_item
		info=f.find('div',attrs={"class":"content-col content-col-1"}).text
		imgtag=f.find('img')
		p=FoodItems(title,info,imgtag.attrs['data-src'])
		results.append(p)
	return results
