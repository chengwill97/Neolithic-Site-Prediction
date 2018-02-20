from bs4 import BeautifulSoup
from time import sleep
import requests


if __name__ == '__main__':
    website = 'http://discovery.ucl.ac.uk/1469811/'
    url = requests.get('http://www.football-data.co.uk/englandm.php').text
    soup = BeautifulSoup(url)
    for link in soup.findAll("a"):
        current_link = link.get("href")
        if current_link.endswith('csv'):
            print('Found CSV: ' + current_link)
            print('Downloading %s' % current_link)
            sleep(10)
            response = requests.get('http://www.football-data.co.uk/%s' % current_link, stream=True)
            fn = current_link.split('/')[0] + '_' + current_link.split('/')[1] + '_' + current_link.split('/')[2]
            with open(fn, "wb") as handle:
                for data in response.iter_content():
                    handle.write(data)