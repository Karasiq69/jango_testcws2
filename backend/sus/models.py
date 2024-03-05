from django.db import models


class Sus(models.Model):
	name = models.CharField(max_length=255)
