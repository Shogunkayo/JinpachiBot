from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.futbin.com/players'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}

site = requests.get(url, headers=headers)

soup = bs(site.content, 'html.parser')

names = soup.find_all('a', class_ = 'player_name_players_table')
chemistry = soup.find_all('span', class_ = 'players_club_nation')
ovr_ratings = soup.find_all('span', class_ = '')

chemistry_cleaned = []
names_cleaned = []
for i in range(len(names)):
    names_cleaned.append(names[i].text.strip())
    chemistry_cleaned.append((chemistry[i].findChildren('a')[0].get('data-original-title'), chemistry[i].findChildren('a')[1].get('data-original-title'), chemistry[i].findChildren('a')[2].get('data-original-title')))


'''
print(names_cleaned)
print(chemistry_cleaned)
'''