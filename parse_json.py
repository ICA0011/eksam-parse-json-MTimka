import json, requests

url = 'http://upload.itcollege.ee/~aleksei/eksam.json'

def parse_json(url):

    # your code here

    course_code = 0

    for course in json.loads(requests.get(url).text)['courses']:
        if course['name'] == 'Scripting languages':
            course_code = course['code']

    return course_code


print(parse_json(url))
