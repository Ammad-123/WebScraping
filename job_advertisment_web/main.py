from bs4 import BeautifulSoup
import requests,time

print('Put some skill that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.strip().replace('\n',', ')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills: 
                with open(f'posts/{index}', 'w') as file:
                    file.write(f'Company Name : {company_name.strip()} \n')
                    file.write(f'Required Skills : {skills.strip()}  \n')
                    file.write(f'Posted days: {published_date.strip()} \n')
                    file.write(f'More Info: {more_info.strip()} \n')
                print(f'File saved:{index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 10)