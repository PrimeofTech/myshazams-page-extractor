from bs4 import BeautifulSoup as bs

with open('My Shazam - Shazam.html', 'r', encoding='UTF-8') as file:
    content = file.read()

soup = bs(content, 'html.parser')

def list_cleaner(lst):
    new_lst = []
    for i in lst:
        i = " ".join(i.split())
        if i != '':
            new_lst.append(i)
    return new_lst

with open('shazam.csv', 'a+') as f:

    print('no, name, artist')
    f.write('no, name, artist \n')
    for item in soup.find_all('article', {'data-screenname': 'charts'}):
        no = ' '.join(item.find_all('div', class_='number')[0].text.split())
        title = ' '.join(item.find_all('div', class_='title')[0].text.split())
        artist = ' '.join(item.find_all('div', class_='artist')[0].text.split())
        if ',' in title:
            title = f'"{title}"'
        if ',' in artist:
            artist = f'"{artist}"'
        print(f'{no}, {title}, {artist}')
        f.write(f'{no}, {title}, {artist} \n')
