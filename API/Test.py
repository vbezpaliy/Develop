import requests

from pprint import pprint

respons = requests.get('https://stepik.org/api/search-results')
params={
    "quety": "python",
    "is_popular": False,
}

titles = []
for course in respons.json()['search-results']:
    titles.append(course['course_title'])

pprint(titles)


