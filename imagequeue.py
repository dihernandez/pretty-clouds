import urllib2

#may only load one image at a time
class ImageQueue:
	def __init__(self):
		self.isPopulated = False
		self.content = ""

	def isPopulated(self):
		return self.isPopulated
	
	def clearImage(self):
		self.isPopulated = False
		self.content = ""
	
	def pushImage(self, image_url):
		print image_url
		if (not self.isPopulated):
			self.content = image_url
			image_holder = open("image_holder.jpg",'w')
			image_holder.write(urllib2.urlopen(image_url).read())
			image_holder.close()
			self.isPopulated = True
		else:
			raise Exception("image already loaded")
