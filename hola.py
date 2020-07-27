'''
Usage: python scrape_imagelinks.py --url <url of the race album you want to scrape>
'''


# import the necessary packages
from selenium import webdriver
import datetime
import time
import argparse
import os


#Define the argument parser to read in the URL
parser = argparse.ArgumentParser()
parser.add_argument('-url', '--url', help='URL to the online repository of images')
args = vars(parser.parse_args())
url = args['url']
url = "https://www.google.com.au/search?hl=en&imgsz=small|medium|large|xlarge&q=Q2612A&btnG=Search+Images&gbv=2&tbm=isch"


# Extract the album name
#album_name = url.split('/')[-2]


# Define Chrome options to open the window in maximized mode
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize the Chrome webdriver and open the URL
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

# Define a pause time in between scrolls
pause_time = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

# Record the starting time
start = datetime.datetime.now()

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # wait to load page
    time.sleep(pause_time)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # which means end of page
        break
    # update the last height
    last_height = new_height

# Record the end time, then calculate and print the total time
end = datetime.datetime.now()
delta = end-start
print("[INFO] Total time taken to scroll till the end {}".format(delta))

# Extract all anchor tags
link_tags = driver.find_elements_by_tag_name('img')

# Create an emply list to hold all the urls for the images
srcs = []

# Extract the urls of only the images from each of the tag WebElements
for tag in link_tags:
    if "rg_i Q4LuWd" not in tag.get_attribute('class'):
        continue
    srcs.append(tag.get_attribute('src'))


#Create the directory after checking if it already exists or not
dir_name = 'Angular'
if not os.path.exists(dir_name):
    try:
        os.mkdir(dir_name)
    except OSError:
        print ("[INFO] Creation of the directory {} failed".format(os.path.abspath(dir_name)))
    else:
        print ("[INFO] Successfully created the directory {} ".format(os.path.abspath(dir_name)))
print(srcs)
# Write the links to the image pages to a file
f = open("{}/{}.csv".format(dir_name, dir_name),'w')
f.write(",\n".join(srcs))
print ("[INFO] Successfully created the file {}.csv with {} links".format(dir_name, len(srcs)))
