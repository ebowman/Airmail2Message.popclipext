import os
import urllib.parse
import subprocess

def convert_url(url):
    parsed_url = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed_url.query)
    
    mail = params.get('mail', [''])[0]
    messageid = params.get('messageid', [''])[0]
    
    new_url = f"message:%3C{messageid}%3E"
    
    return new_url

def open_url(url):
    subprocess.run(['open', url])


url = os.environ['POPCLIP_TEXT']
new_url = convert_url(url)
open_url(new_url)
