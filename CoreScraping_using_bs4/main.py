from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    ## creating instance of BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify)
    

    ## Searching for specific tag
    # tags = soup.find('h5')
    
    ## Searching for all specific tags
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    ## iterating all courses
    # for course in courses_html_tags:
    #     print(course.text)

    ## Searching for course cards
    course_cards = soup.find_all('div', class_='card' )
    for course in course_cards:
        # print(course)
        # print(course.h5.text)

        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f"{course_name} costs {course_price}")


