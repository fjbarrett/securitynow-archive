from bs4 import BeautifulSoup

with open("2005.html") as fp:
    soup = BeautifulSoup(fp, 'xml')
    for link in soup.find_all('a'):
        print(link.get('href'))
