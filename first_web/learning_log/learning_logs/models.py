from django.db import models

# Create your models here.

class Topic(models.Model):
	#"""用户主题"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.text
		#"""返回模型的字符串表示"""
class Entry(models.Model):
	"""study sth and what is it"""
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		# 返回模型的字符串表示
		if len(self.text) > 50:
			return self.text[:50] + '...'
		else:
			return self.text