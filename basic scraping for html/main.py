from bs4 import BeautifulSoup

import json

data = {'courses': []}


with open('basic scraping for html/home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for card in course_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        data['courses'].append({
            'course_name': course_name,
            'course_price': course_price
        })

    with open('data.json', 'w') as file:
        json.dump(data, file)