# Write your solution here
import urllib.request
import json
import certifi

def retrieve_course(course_name: str) -> list:
    req = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats").read()
    req = json.loads(req)
    hasil = {}
    siswa = 0
    jam = 0
    totalLatihan = 0
    for data in req:
        if req[data]["students"] > siswa:
            siswa = req[data]["students"]
        jam += req[data]["hour_total"]
        totalLatihan += req[data]["exercise_total"]
    rataJam = jam // siswa
    rataLatihan = totalLatihan // siswa
    hasil["weeks"] = len(req)
    hasil["students"] = siswa
    hasil["hours"] = jam
    hasil["hours_average"] = rataJam
    hasil["exercises"] = totalLatihan
    hasil["exercises_average"] = rataLatihan

    return hasil


def retrieve_all() -> list:
    response = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses").read()
    data = json.loads(response)
    result = []
    for x in data:
        if x['enabled'] == True:
            result.append((x['fullName'], x['name'], x['year'], sum(x['exercises'])))
    return result
if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))