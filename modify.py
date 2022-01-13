from datetime import datetime
import piexif

filename = 'image.jpg'
exif_dict = piexif.load(filename)
new_date = datetime(2018, 1, 1, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, filename)