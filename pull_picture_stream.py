import requests
import urllib2
import time
import json
from bs4 import BeautifulSoup
import copy
import imagequeue as imQ

REDDIT_SEARCH_URL = 'http://www.reddit.com/r/EarthPorn/search?q=cloud&restrict_sr=on/'
gallery_url = '{page_number}'
GALLERY_KEY = 'GALLERY'
#Do not change eaa798b45a9adeb
CLIENT_ID = 'eaa798b45a9adeb'

class ImageStream:
	def __init__(self):
		self.image_urls = []
		self.image_queue = imQ.ImageQueue()
		self.num_page_updates = 0
		try:
			page_json = json.loads(requests.get(GALLERY_URL.format(page_number = self.num_page_updates)))
		except:
			page_json = {}

	def updatePageUrl():
		self.num_page_updates += 1
		updated_url = GALLERY_URL
		updated_url.format(page_number = self.num_page_updates)
		self.page_json = json.loads(requests.get())

	def getImageLinks(self):
		page = requests.get(REDDIT_SEARCH_URL)
		content = BeautifulSoup(page.content)
		thumbnail_container = content.select('a.thumbnail')
		
		for reference in thumbnail_container:
			extracted_url = reference['href']
			self.image_urls.append(extracted_url)
		return self.image_urls


	''' extract urls from imgur gallery 
		adapted from Tankor Smash's Blog post http://blog.tankorsmash.com/?p=266
	'''
	def getImageLinksFromImgurGallery(self):
		IMAGE_NAME_KEY = 'hash'		
		IMAGE_EXTENSION_KEY = 'ext'
		BASE_URL = r'http://imgur.com/{name}{ext}'
		image_list = self.page_json[GALLERY_KEY]
		
		for image in image_list:
			image_name = image[IMAGE_NAME_KEY]
			image_ext = image[IMAGE_EXTENSION_KEY]
			image_url = BASE_URL.format(name=name, ext=ext)
			self.image_urls.append(image_url)
		return copy.copy(self.image_urls)

	def populateQueue(self, image_url):
		try:
			self.image_queue.pushImage(image_url)
		except:
			#give time for processing to finish
			time.sleep(5)
			#now force next one through
			self.image_queue.clearImage()
			self.image_queue.pushImage(image_url)


