from django.db import models

class information(models.Model):
	date=models.CharField(max_length=100)
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	gender_choices=(('male','male'),('female','female'),('other','other'))
	gender=models.CharField(max_length=10,choices=gender_choices,default='male')
	dateofbirth=models.CharField(max_length=15)
	education=models.CharField(max_length=500)
	email=models.EmailField()
	phonenumber=models.CharField(max_length=15)
	address=models.TextField()
	skills=models.CharField(max_length=200)
	total_experience=models.CharField(max_length=100)
	realtime_experience=models.CharField(max_length=100)
	current_ctc=models.CharField(max_length=10)
	expected_ctc=models.CharField(max_length=10)
	noticeperiod=models.CharField(max_length=10)
	reason=models.TextField()
	resume=models.FileField(upload_to='resume/')
	def __str__(self):
		k=self.firstname+" "+self.lastname
		return k