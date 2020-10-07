import requests as r
import shutil
import ctypes
import os

    
# Specifies URL to download image from and file name. 
url = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/latest.jpg"
filename = url.split("/")[-1]

# Change user folder name below to matrch your account.
img_path = "C:\\PySpaceWall"
img = f"{img_path}\{filename}"

# Test for path and create it if it doesn't exist
if os.path.exists(img_path) == False: 
    os.mkdir("C:\\PySpaceWall")

# Retrieve data with request module.
data = r.get(url, stream=True)
data.raw.decode_content = True

with open(img, 'wb') as f:
    shutil.copyfileobj(data.raw, f)

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img, 0)