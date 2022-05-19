import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)
## Client ID: 2dc31ef084eb324
## Client Secret: b8bea5b05cde97daeb5d989c5bc31a1e740777d2

def get_links(client_id):

   headers = {'Authorization': 'Client-ID {}'.format(client_id)}
   req = Request('https://api.imgur.com/3/gallery/', headers=headers, method='GET')
   with urlopen(req) as resp:
       data = json.loads(resp.readall().decode('utf-8'))
   return map(lambda item: item['link'], data['data'])

def download_link(directory, link):
   logger.info('Downloading %s', link)
   download_path = directory / os.path.basename(link)
   with urlopen(link) as image, download_path.open('wb') as f:
       f.write(image.readall())

def setup_download_dir():
   download_dir = Path('images')
   if not download_dir.exists():
       download_dir.mkdir()
   return download_dir

