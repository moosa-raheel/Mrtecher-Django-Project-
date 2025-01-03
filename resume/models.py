from django.db import models

# Choices 
states = (('Sindh','Sindh'),('Punjab','Punjab'),('Balochistan','Balochistan'),('KPK','KPK'))
job_city = (('Karachi','Karachi'),('Lahore','Lahore'),('Islamabad','Islamabad'),('Quetta','Quetta'),('Peshawar','Peshawar'),('Hyderabad','Hyderabad'),('Sukkur','Sukkur'),('Multan','Multan'),('Faisalabad','Faisalabad'),('Rawalpindi','Rawalpindi'),('Gujranwala','Gujranwala'),('Sialkot','Sialkot'),('Bahawalpur','Bahawalpur'),('Sargodha','Sargodha'),('Sahiwal','Sahiwal'),('Okara','Okara'),('Wah','Wah'),('Dera Ghazi Khan','Dera Ghazi Khan'),('Mirpur Khas','Mirpur Khas'),('Nawabshah','Nawabshah'),('Mardan','Mardan'),('Kasur','Kasur'),('Sheikhupura','Sheikhupura'),('Rahim Yar Khan','Rahim Yar Khan'),('Gujrat','Gujrat'),('Larkana','Larkana'),('Jhang','Jhang'),('Mingora','Mingora'),('Narowal','Narowal'),('Chiniot','Chiniot'),('Kamoke','Kamoke'),('Sukheke','Sukheke'),('Hyderabad','Hyderabad'),('Muzaffarabad','Muzaffarabad'),('Mandi Bahauddin','Mandi Bahauddin'),('Jhelum','Jhelum'),('Khanpur','Khanpur'),('Hafizabad','Hafizabad'),('Kohat','Kohat'),('Khuzdar','Khuzdar'),('Dadu','Dadu'),('Gojra','Gojra'),('Muridke','Muridke'),('Kohlu','Kohlu'),('Jacobabad','Jacobabad'),('Shikarpur','Shikarpur'),('Kandhkot','Kandhkot'),('Tando Allahyar','Tando Allahyar'),('Dera Ismail Khan','Dera Ismail Khan'),('Chaman','Chaman'),('Hub','Hub'),('Umerkot','Umerkot'),('Dera Murad Jamali','Dera Murad Jamali'),('Kotli','Kotli'),('Dera Allah Yar','Dera Allah Yar'),('Bhakkar','Bhakkar'),('Turbat','Turbat'),('Mianwali','Mianwali'),('Chaman','Chaman'),('Kharan','Kharan'),('Wazirabad','Wazirabad'))
gender = (('M','Male'),('F','Female'),('O','Other'))

# Model For Resume
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11,help_text='Enter 11 digits Phone Number')
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=1,choices=gender)
    state = models.CharField(max_length=50,choices=states)
    prefered_location = models.CharField(max_length=250,choices=job_city)
    profile_image = models.ImageField(upload_to='images/profile/',blank=True)
    resume_file = models.FileField(upload_to='doc/resumes/',blank=True)
    def __str__(self):
        return self.name