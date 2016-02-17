from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.

def thumb_upload_location(self, filename):
	return "%s/%s" %(self.name, filename)

def getname(self):
	return self.Project.name

def image_upload_location(self, filename):
	return "%s/imgs/%s" %(self.project, filename)


class Project(models.Model):
	name = models.CharField(max_length = 200)
	thumb = models.ImageField(upload_to = thumb_upload_location,
		null = True)
	description = HTMLField()
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		
		super(Project, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("main:project_detail", kwargs = {"slug":self.slug})

	def __str__(self):
		return self.name

class ProjectImages(models.Model):
	project = models.ForeignKey('Project', related_name='images')
	name = getname
	image = models.ImageField(blank = True, null = True, upload_to = image_upload_location)




