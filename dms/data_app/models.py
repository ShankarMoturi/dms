from django.db import models
from django.contrib.auth.models import User

def generate_path(self, fileName):
	url = "files/users/%s/%s/%s" % (self.docid, self.typeOfFile, fileName)
	return url


class FileDetails(models.Model):
	docid=models.ForeignKey('auth.User')
	fileName = models.CharField(max_length = 30)
	typeOfFile = models.CharField(max_length=30)
	# keyWords = models.CharField(max_length = 30)
	docfile = models.FileField(upload_to= generate_path)
	def __str__(self):
		return self.fileName
