from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("http://www.laokaoya.com/11357.html").read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")
all_href = soup.find_all('a')
# all_href = [l['href'] for l in all_href]
for l in all_href:
    if l.find("雅思写作小作文范文 雅思写作") != -1:
        print('\n', l['href'])
