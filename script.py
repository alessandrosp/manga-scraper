# Written for Python 3!

import urllib.request
import os

# Parameters
manga = 'Shamo' # Use _ for spaces, e.g. The_Devil_King, case insensitive
download_from = 35 # Inclusive
download_to = 36 # Exclusive
# Note: to download the first volume download_from = 1 and download_to = 2
# Note 2: to download all the volumes just set download_to = 9999

base_path = 'https://www.otakusmash.com/read-manga/mangas/'+manga+'/'
folder = manga.replace('_',' ').title()
last_volume = False # When last is reached scrips ends

if not os.path.exists(folder):
    os.makedirs(folder)

def download(url, path):
    '''Just a wrapper; download url in path'''
    urllib.request.urlretrieve(url, path)
    
def pad_zeros(string, final_length):
    '''It adds '0' to string until it reaches final_length length.'''
    while True:
        if len(string) == final_length:
            return string
        else:
            string = '0'+string
 
for vol in range(download_from, download_to):
    
    # Get the volume string
    str_vol = pad_zeros(str(vol),3)
    folder_volume = folder+'/Volume '+str_vol
    
    if not os.path.exists(folder_volume):
        os.makedirs(folder_volume)    
    
    # Generate the url, part 1
    url = base_path+str_vol+'/Read-Shamo-Manga-Online-Free-'
    
    for page in range(1,999):
        str_page = pad_zeros(str(page),3)
        filename = folder_volume+'/Page '+str_page+'.jpg'
        
        try:
            download(url+str_page+'.jpg',filename)
            print('Page '+str(page)+' of volume '
                  +str(vol)+' has been downloaded')
        except:
            try: # The last volume's url is different
                url = base_path+str_vol+'%20-%20THE%20END/Read-Shamo-Manga-Online-Free-'
                download(url+str_page+'.jpg',filename)
                print('Page '+str(page)+' of volume '
                      +str(vol)+' has been downloaded')   
            except:
                if page == 1:
                    # If no page 1 then last volume has been reached
                    last_volume = True
                    os.rmdir(folder_volume) # To avoid empty folders
                    break
                
                print('Page '+str(page-1)
                      +' was the last page of volume '+str(vol)+'\n')
                break
    
    if last_volume == True:
        break
    
print('All the volumes requested have been downloaded!')