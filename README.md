# Manga Downloader (Otaku Smash)

## Description

A simple script to download manga scans from [Otaku Smash](https://www.otakusmash.com/). The script has been written then 7th of February 2016 and the author (me) offers no guarantees that it'll work in the future. Quite the contrary: I can offer almost complete certainty that it won't.

Read the disclaimer (see below) before using the script!

## How it works

Open the script.py file. There are few parameters to tweak:

    manga = 'Shamo' # Use _ for spaces, e.g. The_Devil_King, case insensitive
    download_from = 34 # Inclusive 
    download_to = 35 # Exclusive

I think it's pretty intuitive, but just in case: *manga* is the name of the manga you want to download (check on [Otaku Smash](https://www.otakusmash.com/) they have the manga you're looking for), *download_from* and *download_to* tell the script which volumes you want to download; in pure Python spirit, *download_from* is inclusive and *download_to* is exclusive.

For example to download volumes 3, 4 and 5 of Shamo you'll have to set the parameters to be:

    manga = 'Shamo'
    download_from = 3
    download_to = 6

When you have set up the parameters you are ready to run the script. A new folder with the name of the manga will be created in the same folder where the *script.py* file was placed. Within this folder a new folder for each volume will be created. The structure is:

    script.py
    Shamo
    	Volume 003
    		Page 001
    		Page 002
    		...
		Volume 004
			Page 001
			Page 002
			...
		Volume 005
			Page 001
			Page 002
			...

## Disclaimer

Few considerations: (1) Always check the robots.txt file of a site before scraping content from it, as not everyone is happy to have his or her server hit by multiple consecutive requests; (2) Some mangas uploaded on Otaku Smash may be covered by copyright: please, do make sure what you're doing is legal before doing it. I provide with you the tool, what you do with it it's your sole responsibility. 

And remember, **don't be evil**.