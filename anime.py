from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={headers["User-Agent"]}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=options)

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
            driver.get(url)
            countdown_soup = bs(driver.page_source, features="lxml")

            name = countdown_soup.find('h4').text.strip()
            description = "\n".join([i.text.strip() for i in countdown_soup.find('div', class_ = 'expandable-text-body').find_all('p')])
            genre = ",".join([i.text.strip() for i in countdown_soup.find('div', class_ = 'inline-list').find_all('a')])
            studio = countdown_soup.find_all('div', class_ = 'column medium-6')[1].find('a').text.strip()
            details = countdown_soup.find_all('div', class_='section-body')
            original_title = details[0].find('small').text.strip()
            status = details[1].find('small').text.strip()
            premiere = details[2].find('a').text.strip()
            season = details[3].find('a').text.strip()
            episodes = countdown_soup.find('div', class_ = 'anime-meta-bar').find_all('div', class_='info-bar-cell-value')[2].text.strip()

            if(status == 'Releasing'):
                new_ep = [i.text.strip() for i in countdown_soup.find('div', class_='countdown-bar').find_all('div', class_='info-bar-cell')]
            else:
                new_ep = []

            anime_details.append({'name':name, 'description':description, 'genre':genre, 'studio':studio, 'original_title':original_title, 'status':status, 'premiere':premiere, 'season':season, 'episodes':episodes, 'new_ep':new_ep})

        return anime_details
    except Exception as e:
        print(e)
        return 'There was a problem processing your request'

if __name__ == '__main__':
    start_time = time.time()
    print(search_anime('naruto'))  
    print("--- %s seconds ---" % (time.time() - start_time))
