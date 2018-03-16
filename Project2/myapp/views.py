
from django.shortcuts import render, redirect
from django.http import HttpResponse
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from django.core.mail import send_mail
import myapp.lib.output_fb as fb
import myapp.lib.yt_output as youtube
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import myapp.lib.output_fb as fb
import myapp.lib.yt_output as youtube
import myapp.lib.output_fb_nonlive as fb_NL
#import urllib2
# Create your views here.
def hello(request) :
	alph = 110
	return render(request, "hello.html", {"alpha" : alph})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return redirect("https://www.facebook.com")	

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "sainiabhi7734@gmail.com", [emailto])
   return HttpResponse('%s'%res)

def alphaFn(request, var) :
	return redirect(sendSimpleEmail,"abhisni@iitk.ac.in")

@csrf_exempt
def index(request):
  fb_live_form = fb_url_live()
  fb_non_live_form = fb_url_nonlive()
  yt_form = yt_url()

  if request.method == 'POST':
    print("post")
    fb_live_form = fb_url_live(request.POST)
    fb_non_live_form = fb_url_nonlive(request.POST)
    yt_form = yt_url(request.POST)
    if(fb_live_form.is_valid()):
      fb_live_url = fb_live_form.cleaned_data['url1']
      print(fb_live_url)
    if(fb_non_live_form.is_valid()):  
      fb_non_live_url = fb_non_live_form.cleaned_data['url2']
      print(fb_non_live_url)
    if(yt_form.is_valid()):  
      youtube_url = yt_form.cleaned_data['url3']
      print(youtube_url)

    if(fb_live_form.is_valid() and fb_live_url):  
      print("live = ",fb_live_url)
      fb_live_url = str(fb_live_url)
      output0 = fb.main(fb_live_url)
      output = fb_NL.init(fb_live_url)
      print(output0)
      return render(request, "fb_live_analysis.html", {"times" : output0["time_break_list"], "scores" : output0["scores"], "total" : output["total_responses"],"url" : fb_live_url, "neg_score" : output["negative_score"],"pos_score" : output["positive_score"],"neg_perc" : output["percentage_neg"],"pos_perc" : output["percentage_pos"]})
      #return  redirect(request, fb_video,fb_live_url)
    
    if(fb_non_live_form.is_valid() and fb_non_live_url):  
      fb_non_live_url = str(fb_non_live_url)
      print("non-live = ",fb_non_live_url)
      output = fb_NL.init(fb_non_live_url)
      print(output)
      return render(request, "facebook_analysis_nonlive.html", {"total" : output["total_responses"],"url" : fb_non_live_url, "neg_score" : output["negative_score"],"pos_score" : output["positive_score"],"neg_perc" : output["percentage_neg"],"pos_perc" : output["percentage_pos"]})
      #return  redirect(request, fb_video_nonlive,fb_non_live_url)
    
    if(yt_form.is_valid() and youtube_url):  
      youtube_url = str(youtube_url)
      print("youtube = ",youtube_url)
      output = youtube.main(youtube_url)
      print(output)
      return render(request, "youtube_analysed.html", {"total" : output["total_responses"],"url" : youtube_url, "neg_score" : output["negative_score"],"pos_score" : output["positive_score"],"neg_perc" : output["percentage_neg"],"pos_perc" : output["percentage_pos"]})      
      #return  redirect(request, youtube_video,youtube_url)

  return render(request,'index.html', context={'fb_live_form':fb_live_form,'fb_non_live_form':fb_non_live_form,'yt_form':yt_form})   


	
def fb_video(request) :
    video_url = "https://www.facebook.com/election.commission.iitk/videos/597396273797338/"
    output0 = fb.main(video_url)
    output = fb_NL.init(video_url)
    print(output0)
    return render(request, "fb_live_analysis.html", {"times" : output0["time_break_list"], "scores" : output0["scores"], "total" : output["total_responses"],"url" : video_url, "neg_score" : output["negative_score"],"pos_score" : output["positive_score"],"neg_perc" : output["percentage_neg"],"pos_perc" : output["percentage_pos"]})

def youtube_video(request) :
    video_url = "https://www.youtube.com/watch?v=3KenEVty7gg"
    output = youtube.main(video_url)
    print(output)
    return render(request, "youtube_analysed.html", {"total" : output["total_responses"],"url" : video_url, "neg_score" : output["negative_score"],"pos_score" : output["positive_score"],"neg_perc" : output["percentage_neg"],"pos_perc" : output["percentage_pos"]})

def fb_video_nonlive(request) :
    video_url = "https://www.facebook.com/theindianviner/videos/1989026828090683/"
    output = fb_NL.init(video_url)
    print(output)
    return render(request, "facebook_analysis_nonlive.html", {"total" : output["total_responses"],"url" : video_url, "neg_score" : output["negative_score"],"pos_score" : output["positive_score"],"neg_perc" : output["percentage_neg"],"pos_perc" : output["percentage_pos"]})

def team(request) :
    return render(request,"team.html")


# # # # # # # # # # # # # # # # # # # # # # # # 
