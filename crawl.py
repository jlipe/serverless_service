import boto3
import requests
import datetime

from bs4 import BeautifulSoup

def lambda_handler(event, context):
  dynamodb = boto3.resource("dynamodb")
  table = dynamodb.Table('361_headlines')
  
  fox_header = get_fox_news_header()
  put_headline(table, fox_header, "Fox News")
  
  cnn_header = get_cnn_header()
  put_headline(table, cnn_header, "CNN")
  
  breitbart_header = get_breitbart_header()
  put_headline(table, breitbart_header, "Breitbart")
  
  mother_jones_header = get_mother_jones_header()
  put_headline(table, mother_jones_header, "Mother Jones")
  
  nytimes_header = get_nytimes_header()
  put_headline(table, nytimes_header, "NY Times")
  
  daily_fx_header = get_daily_fx_header()
  put_headline(table, daily_fx_header, "DailyFX")
  
  cnbc_header = get_cnbc_header()
  put_headline(table, cnbc_header, "CNBC")
  
  ft_header = get_ft_header()
  put_headline(table, ft_header, "Financial Times")
  
  crypto_news_header = get_crypto_news_header()
  put_headline(table, crypto_news_header, "Crypto News")
  
  pc_gamer_header = get_pc_gamer_header()
  put_headline(table, pc_gamer_header, "PC Gamer")
  
  kotaku_header = get_kotaku_header()
  put_headline(table, kotaku_header, "Kotaku")
  

def get_fox_news_header():
  try:
    url = "https://foxnews.com"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    div = soup.find("div", {"class":"collection collection-spotlight has-hero"})
    header = div.findChildren("h2")
    title = header[0]
    
    return title.get_text().strip()
  except:
    return ""
    
def get_cnn_header():
  try:
    url = "https://www.cnn.com/data/ocs/section/index.html:homepage1-zone-1/views/zones/common/zone-manager.izl"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    headlines = soup.find_all("h2")
    headline = headlines[0]
    return headline.text.strip()
  except:
    return ""
    
def get_cnbc_header():
  try:
    url = "https://www.cnbc.com/"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    section = soup.find_all("div", {"class":"FeaturedCard-imageContainer"})[0]
    link = section.find("a")
    return link["title"].strip()
  except:
    return ""
  
def get_breitbart_header():
  try:
    url = "https://breitbart.com"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    sections = soup.find_all("section", {"class":"top_article_main"})[0]
    headline = sections.find("a")
    return headline["title"]
  except:
    return ""
  
def get_mother_jones_header():
  try:
    url = "https://motherjones.com"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    header = soup.find_all("h1", {"class":"hed"})[0]
    return header.text
  except:
    return ""
  
def get_nytimes_header():
  try:
    url = "http://nytimes.com"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    headlines = soup.find_all("h3")
    headline = headlines[0]
    return headline.text
  except:
    return ""
  
def get_daily_fx_header():
  try:
    url = "http://dailyfx.com"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    headlines = soup.find_all("p", {"class": "dfx-articleHero__text"})
    headline = headlines[0]
    return headline.text.strip()
  except: 
    return ""

def get_ft_header():
  try:
    url = "https://www.ft.com/"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    section = soup.find_all("div", {"class":"headline js-teaser-headline headline--scale-7"})[0]
    title = section.find("span")
    return title.text.strip()
  except:
    return ""
    
def get_crypto_news_header():
  try:
    url = "https://cryptonews.com/"
    req = requests.get(url, timeout=6) 
    soup = BeautifulSoup(req.content, 'html.parser')
    section = soup.find_all("a", {"class":"article__title article__title--main mb-20"})[1]
    return section.text.strip()
  except:
    return ""
    
def get_pc_gamer_header():
  try:
    url = "https://www.pcgamer.com/news/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    section = soup.find_all("figure", {"class":"feature-block-item"})[0]
    span = section.find("span", {"class", "article-name"})
    return span.text.strip()
  except:
    return ""
    
def get_kotaku_header():
  try:
    url = "https://kotaku.com/culture/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    headlines = soup.find_all("h2")
    return headlines[0].text.strip()
  except:
    return ""

  
def put_headline(table, headline, source):
  if headline == "":
    return
  time = str(datetime.datetime.now().isoformat())
  table.put_item(
    Item={'headline':headline,
        'time':time,
        'source':source
    })