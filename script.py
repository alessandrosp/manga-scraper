#/usr/bin/env python3

#-----------------------------------
# Import libraries
#-----------------------------------
import urllib.request
import os
from bs4 import BeautifulSoup
from functions import download, pad_zeros

#-----------------------------------
# Define parameters
#-----------------------------------
site = 'https://www.otakusmash.com/read-manga/'
# EITHER 'http://www.mrsmanga.com/'
# OR 'https://www.otakusmash.com/read-comics/'
# OR 'https://www.otakusmash.com/read-manga/'
manga = 'Blade_of_the_Immortal' # Use _ for spaces, e.g. The_Devil_King, case insensitive
download_from = 1 # Inclusive
download_to = 3 # Exclusive
# Note: to download the first volume download_from = 1 and download_to = 2
# Note 2: to download all the volumes just set download_to = 9999

#-----------------------------------
# Let's the download begin!
#-----------------------------------
base_path = site+manga+'/'
folder_name = manga.replace('_',' ').title() 

if not os.path.exists(folder_name):
    os.makedirs(folder_name) # Create the manga folder

is_last_volume = False # When last is reached scrips ends

for n_volume in range(download_from, download_to):
    
    # Get the volume string
    str_volume = pad_zeros(str(n_volume),3) # Ex: "001"
    folder_volume = folder_name+'/Volume '+str_volume # Ex: "Volume 001"
    
    if not os.path.exists(folder_volume):
        os.makedirs(folder_volume) # Create the volume folder
    
    # Generate the url
    url = base_path+str_volume
    
    for page in range(1,9999):
        # HTML request + souping
        html = urllib.request.urlopen(url).read() # We get the HTML of the page
        soup = BeautifulSoup(html, 'html.parser') # We cook it into a soup
        image_path = soup.find("img", class_="picture")['src'] # Image URL
        abs_image_path = site+image_path
        
        # Naming file
        str_page = pad_zeros(str(page),3)
        filename = folder_volume+'/Page '+str_page+'.jpg'
        
        # Downloading page
        download(abs_image_path.replace(" ","%20"),filename)
        print('Page '+str(page)+' of volume '
              +str(n_volume)+' has been downloaded')
        
        # Search for next page
        next_url = None
        tds = soup.find_all(["td"]) # Get all the td
        for td in tds:
            list_a = td.find_all("a")
            for a in list_a:
                if 'Next Page' in str(a):
                    next_url = a["href"]
                    break
        
        if next_url: # There's a next page        
            url = site+next_url
        else:
            break
    
print('All the volumes requested have been downloaded!')