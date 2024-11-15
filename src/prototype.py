import requests
# Right now ignore _____ here, IDE doesn't know about local dependencies/python version

# CONFIG
# Your unique access code can be gotten from Canvas and put here.
# Canvas Course ID
COURSE_ID = "34865"
# ID for the "late tokens left" assignment.
TOKEN_ASSIGNMENT_ID = "178107"
# ID for current assignments being checked.
# If any/all of these is late, deduct a late token for the week.
# Usually, you'll have one first try, one second try, and one self-eval.
# NOTE: I don't think this can do the worksheets; do those manually
# TODO take these as command-line args instead of hard-coding
ASSIGNMENT_IDS = ["TODO", "TODO", "TODO"]

HEADERS = {"Authorization": "Bearer " + ACCESS_TOKEN}
LATE_STUDENTS = dict()

for ASSIGNMENT_ID in ASSIGNMENT_IDS:
    URI_ASSIGNMENT = 'https://canvas.northwestern.edu/api/v1/courses/' + COURSE_ID + '/assignments/' + ASSIGNMENT_ID
    n = requests.request('GET', URI_ASSIGNMENT, headers = HEADERS)
    MESSAGE = n.json()['name'] + " Late. "
    print(MESSAGE)
    URI = 'https://canvas.northwestern.edu/api/v1/courses/' + COURSE_ID + '/assignments/' + ASSIGNMENT_ID + '/submissions?page=' + str(1)  
    while True:
        r = requests.request('GET', URI, headers = HEADERS)
        for x in r.json():
            if x['late']:
                u_id = x['user_id']
                if u_id not in LATE_STUDENTS:
                    LATE_STUDENTS[u_id] = MESSAGE
                else:
                    LATE_STUDENTS[u_id] += MESSAGE
        if 'next' in r.links:
            URI = r.links['next']['url']
        else:
            break
for ID in LATE_STUDENTS:
    URI = 'https://canvas.northwestern.edu/api/v1/courses/' + COURSE_ID + '/assignments/' + TOKEN_ASSIGNMENT_ID + '/submissions/' + str(ID)
    k = requests.request('GET', URI, headers = HEADERS)
    URI = 'https://canvas.northwestern.edu/api/v1/users/' + str(ID) + '/profile'
    l = requests.request('GET', URI, headers = HEADERS)
    print(l.json()['name'] + " has " + str(k.json()['score'] - 1) + " late tokens left: " + LATE_STUDENTS[ID].strip())
    d = {
        "comment": { "text_comment" : LATE_STUDENTS[ID].strip()},
        "submission" : {"posted_grade" : (k.json()['score'] - 1)}
    }
    URI = 'https://canvas.northwestern.edu/api/v1/courses/' + COURSE_ID + '/assignments/' + TOKEN_ASSIGNMENT_ID + '/submissions/' + str(ID)
    j = requests.request('PUT', URI, headers = HEADERS, json = d)
    print(j)
