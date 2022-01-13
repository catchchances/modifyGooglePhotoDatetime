import os
import glob
import json
from datetime import datetime
import piexif

# path = '../Photos from 2020'
path = '../'
for filename in glob.glob(os.path.join(path, '*.json')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
    print(filename)
    jsonFile = open(filename, encoding='utf-8')
    
    jsonData = json.load(jsonFile)
    relatedMediaFileName = jsonData['title']
    photoTakenTimeObj = jsonData['photoTakenTime']
    ts = photoTakenTimeObj['timestamp']
    fs = photoTakenTimeObj['formatted']
    print(relatedMediaFileName)
    print(ts)
    print(fs)
    f.close()
    relatedMediaFilePath = path + relatedMediaFileName
    exif_dict = piexif.load(relatedMediaFilePath)
    new_date = datetime.fromtimestamp(ts)
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, relatedMediaFilePath)
