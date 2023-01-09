from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from price import get_price
import csv
import pandas

def scrape_page(page, version=''):
    url = 'https://www.futbin.com/players?page=' + str(page) + version
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}
    site = requests.get(url, headers=headers)
    soup = bs(site.content, 'html.parser')

    names = soup.find_all('a', class_ = 'player_name_players_table')
    chemistry = soup.find_all('span', class_ = 'players_club_nation')
    ovr_ratings = soup.find_all('span', class_ = 'form')
    pos = soup.find_all('div', class_ = 'font-weight-bold')
    base = soup.find_all('span', class_ = 'badge')
    versions = soup.findAll('td', class_ = 'mobile-hide-table-col')

    chemistry_cleaned = []
    names_cleaned = []
    ovr_ratings_cleaned = []
    pos_cleaned = []

    for i in range(len(names)):
        names_cleaned.append(names[i].text.strip())
        chemistry_cleaned.append((chemistry[i].findChildren('a')[0].get('data-original-title'), chemistry[i].findChildren('a')[1].get('data-original-title'), chemistry[i].findChildren('a')[2].get('data-original-title')))
        ovr_ratings_cleaned.append(int(ovr_ratings[i].text.strip()))
        pos_cleaned.append(pos[i].text.strip())
        versions[i] = versions[i].find('div', recursive=False).get_text()

    for i in range(len(base)):
        base[i] = int(base[i].text.strip())

    base_cleaned = [base[i:i+6] for i in range(0, len(base), 6)]

    for i in range(len(base_cleaned)):
        base_cleaned[i] = sum(base_cleaned[i])

    club = [i[0] for i in chemistry_cleaned]
    nation = [i[1] for i in chemistry_cleaned]
    league = [i[2] for i in chemistry_cleaned]

    return [names_cleaned, pos_cleaned, club, nation, league, ovr_ratings_cleaned, base_cleaned, versions]

name = []
position = []
club = []
nation = []
league = []
ovr_ratings = []
base_ratings = []
price = []

def scrape_site():

    url = 'https://www.futbin.com/players?'
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}
    site = requests.get(url, headers=headers)
    soup = bs(site.content, 'html.parser')

    pages = int(soup.find('ul', class_ = 'pagination').findAll('li')[5].get_text())

    for i in range(1, pages):
        print("Scrapping page ", i)
        page = scrape_page(i)
        for j in range(0, len(page[0])):
            name.append(page[0][j])
            position.append(page[1][j])
            club.append(page[2][j])
            nation.append(page[3][j])
            league.append(page[4][j])
            ovr_ratings.append(page[5][j])
            base_ratings.append(page[6][j])
        sleep(2)
    print("Scrapping completed")

def scrape_new_version(version):
    for i in range(1, 3):
        print("Scrapping page ", i)
        page = scrape_page(i, version)
        for j in range(0, len(page[0])):
            name.append(page[0][j])
            position.append(page[1][j])
            club.append(page[2][j])
            nation.append(page[3][j])
            league.append(page[4][j])
            ovr_ratings.append(page[5][j])
            base_ratings.append(page[6][j])
        sleep(2)
    print("Scrapping completed")

def run(option, version): 
    if(option == 1):
        scrape_site()
    elif(option == 2):
        scrape_new_version(version)

    print("Calculating price")
    for i in range(0, len(ovr_ratings)):
        price.append(get_price(ovr_ratings[i], base_ratings[i]))
    print("Calculating price completed")


    print("Writing to csv")
    with open('cards', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "position", "club", "nation", "league", "ovr_ratings", "base_ratings", "price"])
        for i in range(0, len(name)):
            csv_writer.writerow([name[i], position[i], club[i], nation[i], league[i], ovr_ratings[i], base_ratings[i], price[i]])
    print("Writing to csv completed")

def clean():
    print('Cleaning csv')
    df = pandas.read_csv('cards')
    df.drop_duplicates(inplace=True)
    df.to_csv('cards')
    print('Cleaning complete')

if __name__ == '__main__':
    print('Running Scrapper')
    run(1, ' ')
    clean()
    #run(2, '&version=winter_wildcards')