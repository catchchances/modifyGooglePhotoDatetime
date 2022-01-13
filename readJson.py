# Python program to read
# json file


import json

# Opening JSON file
fileName = r'D:\Users\lzhang53\Downloads\takeout-20220112T165437Z-001\Takeout\Google 相册\Photos from 2020/IMG_3044.MOV.json'
f = open(fileName, encoding='utf-8')

# returns JSON object as
# a dictionary
data = json.load(f)

relatedMedia = data['title']

photoTakenTimeObj = data['photoTakenTime']

ts = photoTakenTimeObj['timestamp']
fs = photoTakenTimeObj['formatted']

print(relatedMedia)
print(ts)
print(fs)

# Iterating through the json
# list
# for i in data['emp_details']:
#     print(i)

# Closing file
f.close()
