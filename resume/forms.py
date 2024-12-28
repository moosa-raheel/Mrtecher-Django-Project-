from django import forms
from .models import Resume

gender = (('M','Male'),('F','Female'),('O','Other'))
states = (('Sindh','Sindh'),('Punjab','Punjab'),('Balochistan','Balochistan'),('KPK','KPK'))
job_city = (('Karachi','Karachi'),('Lahore','Lahore'),('Islamabad','Islamabad'),('Quetta','Quetta'),('Peshawar','Peshawar'),('Hyderabad','Hyderabad'),('Sukkur','Sukkur'),('Multan','Multan'),('Faisalabad','Faisalabad'),('Rawalpindi','Rawalpindi'),('Gujranwala','Gujranwala'),('Sialkot','Sialkot'),('Bahawalpur','Bahawalpur'),('Sargodha','Sargodha'),('Sahiwal','Sahiwal'),('Okara','Okara'),('Wah','Wah'),('Dera Ghazi Khan','Dera Ghazi Khan'),('Mirpur Khas','Mirpur Khas'),('Nawabshah','Nawabshah'),('Mardan','Mardan'),('Kasur','Kasur'),('Sheikhupura','Sheikhupura'),('Rahim Yar Khan','Rahim Yar Khan'),('Gujrat','Gujrat'),('Larkana','Larkana'),('Jhang','Jhang'),('Mingora','Mingora'),('Narowal','Narowal'),('Chiniot','Chiniot'),('Kamoke','Kamoke'),('Sukheke','Sukheke'),('Hyderabad','Hyderabad'),('Muzaffarabad','Muzaffarabad'),('Mandi Bahauddin','Mandi Bahauddin'),('Jhelum','Jhelum'),('Khanpur','Khanpur'),('Hafizabad','Hafizabad'),('Kohat','Kohat'),('Khuzdar','Khuzdar'),('Dadu','Dadu'),('Gojra','Gojra'),('Muridke','Muridke'),('Kohlu','Kohlu'),('Jacobabad','Jacobabad'),('Shikarpur','Shikarpur'),('Kandhkot','Kandhkot'),('Tando Allahyar','Tando Allahyar'),('Dera Ismail Khan','Dera Ismail Khan'),('Chaman','Chaman'),('Hub','Hub'),('Umerkot','Umerkot'),('Dera Murad Jamali','Dera Murad Jamali'),('Kotli','Kotli'),('Dera Allah Yar','Dera Allah Yar'),('Bhakkar','Bhakkar'),('Turbat','Turbat'),('Mianwali','Mianwali'),('Chaman','Chaman'),('Kharan','Kharan'),('Wazirabad','Wazirabad'))
class ResumeForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.RadioSelect(choices=gender),max_length=1)
    state = forms.CharField(widget=forms.Select(choices=states, attrs={'class':'w-full p-3 border border-gray-300 rounded-md my-3'}))
    prefered_location = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=job_city))
    class Meta:
        model = Resume
        fields = "__all__"
        widgets = {
            "gender":forms.RadioSelect(),
        }