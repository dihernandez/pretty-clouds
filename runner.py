import subprocess
import pull_picture_stream as ps

''' here I will call the scraper (pull highly ranked pics with keyword cloud from imgur)
	and pass on to initialize metadata assignments
	run learning algorithms
	and based on their output populate criteria for picture generation
	The scraper/learning stuff will run depending on a switch (boolean var)
	afterwards output will generate image
'''
class Runner:
	def __init__(self):
		self.image_stream = ps.ImageStream()
		self.images_to_process = self.image_stream.getImageLinks()

	def trainingMain(self):
		def retrieveNextImage():
			if (not self.images_to_process):
				self.image_stream.updatePageUrl();
				self.images_to_process = self.image_stream.getImageLinks()
			return self.images_to_process.pop()		

		def callAnalyzer():
			analyzer = subprocess.Popen("pictureAnalyzerMain.cpp")
			analyzer.wait()
			print analyzer.stdout.read()

		while (self.images_to_process):
			next_image = retrieveNextImage()
			self.image_stream.populateQueue(next_image)
			callAnalyzer()

		

''' Dummy function for now, but will eventually
	check if n images have been checked,
	n is my goal sample size and decided by me
'''
def proccessComplete():
	return True

runner = Runner()
runner.trainingMain()