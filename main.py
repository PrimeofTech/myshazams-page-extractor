from bs4 import BeautifulSoup as bs

print('='*95)

with open('shazam-html-files/shazam.html', 'r', encoding='UTF-8') as file:
    content = file.read()

soup = bs(content, 'html.parser')

# for item in soup.find_all('li'):
#     if len(list(item.text)) > 10:
#         print(item, '<br>')

def list_cleaner(lst):
    new_lst = []
    for i in lst:
        i = " ".join(i.split())
        if i != '':
            new_lst.append(i)
    return new_lst

with open('shazam-html-files/shazam.csv', 'a+') as f:

    print('no, name, artist')
    f.write('no, name, artist \n')
    for item in soup.find_all('article', {'data-screenname': 'myshazams '}):
        tag = bs(item.text, 'html.parser')
        li = tag.text.split('   ')
        li = list_cleaner(li)
        print(f'{li[0]}, {li[1]}, {li[2]}')
        f.write(f'{li[0]}, {li[1]}, {li[2]} \n')
