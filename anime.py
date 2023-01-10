from bs4 import BeautifulSoup as bs
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}

def search_anime(name):
    name = "+".join(name.strip().split())
    search_url = 'https://www.livechart.me/search?q=' + name
    search_site = requests.get(search_url, headers=headers)
    soup = bs(search_site.content, 'html.parser')

    try:
        anime_ids = soup.find_all('div', class_ = 'anime-item__body__title')
        if(len(anime_ids) == 0):
            return 'I could not find that anime'

        anime_ids = anime_ids[:min(5, len(anime_ids))]
        for i in range(len(anime_ids)):
            anime_ids[i] = anime_ids[i].find('a')['href']

        anime_details = []

        for i in anime_ids:
            url = 'https://www.livechart.me' + i
            site = requests.get(url, headers=headers)
            soup = bs(site.content, 'html.parser')

            name = soup.find('h4').text.strip()
            anime_details.append({'name':name})

        return anime_details
    except Exception as e:
        print(e)
        return 'There was a problem processing your request'

if __name__ == '__main__':
    print(search_anime('blue lock'))  