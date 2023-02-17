import requests
from bs4 import BeautifulSoup




def scrape_links():
    url = str(input("enter the link whose data need to be scrapped : "))
    markup = "<p><!-- this is a comment --></p>"
    soup2 = BeautifulSoup(markup)
    print(type(soup2.p.string))
    print(soup2.p)
    print(soup2.p.string)
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    title = soup.title
    anchors = soup.find_all('a')
    all_links = set()
    for link in anchors:
        if(link.get('href') != '#'):
            linkText= url + link.get('href')
            all_links.add(link)
            print(linkText)


