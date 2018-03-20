# Scrape_X
The web app is deployed at the following url:
https://frozen-waters-22551.herokuapp.com/

Who am I
==
- Hii, Myself Scrape_X, I am built on `django` and was made as a part of code.fun.do conducted by Microsoft.
- I can do analyze sentiments of audience on public posts on facebook and youtube.
- But, I am quite different from normal sentiment analyzers. I can also do sentiment analysis using timestamp on facebook videos which had been live earlier providing you sentiment analysis of different durations of video.

Where to choose me
==
- I can help in extracting most significant part from a long live video by reading the comments. Simply I will find which duration had mad greater influence on audience.
- One can make my use in extracting breaking news from a long video.

Resources Used
==
- ## Microsoft Text Analytics :
> + Although sentiment analysis was a major part in development of our app, and 6 days was not sufficient to wrote our own code for that which may give us good accuracy.
> + So we thought of using [Text Analytics API][text_api] which is one of the best available sources for sentiment analysis and own a user friendly documentation
> + In our project the file ` myapp/lib/sentiment.py` contains the `module` to call the Text Analysis API

- ## Facebook Graph API :
> + We needed to extract comments from facebook comments, so we used [Facebook Graph API][graph api] to achieve that.
> + In our project, `module` contained by `myapp/lib/fb_comments.py` does that task for us.

- ## Youtube Comment API : 
> + Similar to facebook, we tried to expand our idea to youtube also .
> + To extract comments from youtube we used [Youtube Comment API][comment api].
> + `module` contained by `myapp/lib/yt_comments.py` extracts the comments from any youtube video.
> + **Note :** Although `Youtube Comment API` is sufficient enough to extract the comments form youtube videos, but it uses `Oauth2` authentication to authenticate users and that uses terminal console. So till now it works in localhost only but we are trying to figure out an alternative for it.

Deploying Locally
==
- First make sure you have python3.x installed.

- To run the app make sure you are in the Project2 directory.

- To install the dependencies for python3.x run:

``` pip3 install -r requirements.txt ```

- Then run the following command (for python3.x) :

``` python3 manage.py runserver ```
<!-- Add the doc. here -->
## Possible Errors
#### Wrong Url :
> May return an error in case of wrong url

#### No comments
> May return an error if there are no comments on your video,so use video with comments only.

#### Analysis on Youtube
> Due to some Oauth2 errors with youtube API, right now our app supports youtube analysis on localhost only.
> Deployed version doesn't support youtube analysis


[text_api]: https://azure.microsoft.com/en-in/services/cognitive-services/text-analytics/
[graph api]: https://developers.facebook.com/docs/graph-api/
[comment api]: https://developers.google.com/youtube/v3/docs/commentThreads
