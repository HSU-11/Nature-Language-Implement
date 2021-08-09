import requests
from bs4 import BeautifulSoup
 
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
response = requests.get(url=url)
 
soup = BeautifulSoup(response.text, 'lxml')

info_items = soup.find_all('div', 'release_info')
 
for item in info_items:
    name = item.find('div', 'release_movie_name').a.text.strip()
    english_name = item.find('div', 'en').a.text.strip()
    release_text = item.find('div', 'release_text').text.split('：')[-1].strip()
    level = item.find('div', 'leveltext').span.text.strip()
     
    print('{}({}) 上映日：{} 期待度：{}'.format(name, english_name, release_text, level))
