from django import forms

class fb_url_live(forms.Form):
	url1 = forms.CharField()

class fb_url_nonlive(forms.Form):
	url2 = forms.CharField()

class yt_url(forms.Form):
	url3 = forms.CharField()	