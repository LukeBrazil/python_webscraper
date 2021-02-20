from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for card in course_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        print(f"Course Name: {course_name} -- Course Price: {course_price}")