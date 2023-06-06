#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:19:35 2023

@author: JoseFacio1
"""

import os
import time
import urllib
import requests
from bs4 import BeautifulSoup
import magic
import progressbar
from urllib.parse import quote

            
            
def findImg(name,prod):
    keyword_to_search = [str(item).strip() for item in name.split(',')]
    things = len(keyword_to_search) * 1
    extensions = {'.jpg', '.png', '.ico', '.gif', '.jpeg'}
    i = 0
    bar = progressbar.ProgressBar(maxval=things, \
                                      widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]).start()

    end_object = -1
    

    def _download_page(url):
        response = requests.get(url)
        return response.text

    while i < len(keyword_to_search):
        
        url = 'https://www.google.com/search?q=' + quote(
            keyword_to_search[i].encode('utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
        raw_html = _download_page(url)
        google_image_seen = False
        j = 0
        while j < 1:
            while True:
                try:
                    new_line = raw_html.find('"https://', end_object + 1)
                    end_object = raw_html.find('"', new_line + 1)
                    buffor = raw_html.find('\\', new_line + 1, end_object)
                    if buffor != -1:
                        object_raw = raw_html[new_line + 1:buffor]
                    else:
                        object_raw = raw_html[new_line + 1:end_object]
                    if "https://www.google" not in object_raw and 'http' in object_raw:
                        break
                    else:
                        #print("Nombre nunca encontrado")
                        j += 1
                        break
                    
                except Exception as e:
                    break

            path = "/Users/JoseFacio1/Documents/CBN/Automatizacion Excel/imagenes"
            try:
                r = requests.get(object_raw, allow_redirects=True, timeout=1)
                if 'html' not in str(r.content):
                    mime = magic.Magic(mime=True)
                    file_type = mime.from_buffer(r.content)
                    file_extension = f'.{file_type.split("/")[1]}'
                    if file_extension not in extensions:
                        raise ValueError()
                    if file_extension == '.png' and not google_image_seen:
                        google_image_seen = True
                        raise ValueError()
                    file_name = keyword_to_search[i]
                    file_name = file_name.replace('/', '_').replace('"', '')+ file_extension
                    with open(os.path.join(path, file_name), 'wb') as file:
                        file.write(r.content)
                    url = f"http://127.0.0.1:8000/api/almacen/{prod['id']}/"
                    image_path = os.path.join(path, file_name)
                    with open(image_path, 'rb') as image_file:
                        image_data = {'image': image_file}
                        response = requests.patch(url, files=image_data, headers=headers)
                        
                    if response.status_code == 200:
                        prod['image'] = image_path
                        
                    else:
                        print("Error al actualizar la imagen en el servidor")
                    bar.update(bar.currval + 1)
                else:
                    j -= 1
            except Exception as e:
                print(" IMG MALA")
                j -= 1
            j += 1
        i += 1
    bar.finish()


url = f"http://127.0.0.1:8000/api/almacen/"
headers = {
    "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1ODI0NTQ1LCJpYXQiOjE2ODU0NTY1NDUsImp0aSI6IjI2ZDI3ZjViN2IyMTQyN2JhZjg3MjFkMDRkZDE4ODgzIiwidXNlcl9pZCI6MX0.0wfMibDco6h2jf7PDrS6eJVP5yRQHU5w5A1Zx5sEpYk"
}

response = requests.get(url, headers=headers)

current_index = 0
for i, prod in enumerate(response.json()):
    if current_index > i:
        continue
    findImg(prod['descripcion'], prod)
    current_index += 1
    print(current_index)
    
    

