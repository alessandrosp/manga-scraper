import urllib.request

def download(url, path):
    """Just a wrapper; download url in path"""
    urllib.request.urlretrieve(url, path)
    
def pad_zeros(string, final_length):
    """It adds '0' to string until it reaches final_length length."""
    while True:
        if len(string) == final_length:
            return string
        else:
            string = '0'+string