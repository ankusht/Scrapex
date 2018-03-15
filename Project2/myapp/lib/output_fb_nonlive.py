import myapp.lib.sentiment as sentiment
import myapp.lib.fb_comments as fb_comments


def get_output(sentiments_arr):
	positive_score = 0
	negative_score = 0
	positive_responses = 0
	negative_responses = 0
	for sentiment in sentiments_arr:
		if(sentiment>=0):
			positive_score+= sentiment
			positive_responses+=1
		else:
			negative_score+= sentiment
			negative_responses+=1
	total_responses = positive_responses + negative_responses
	precentage_pos = (positive_responses/total_responses)*100
	precentage_neg = (negative_responses/total_responses)*100
	output = {"positive_score":positive_score * 200 / total_responses,"negative_score":negative_score * 200 / total_responses,
			 "positive_responses":positive_responses,"negative_responses":negative_responses,
			"percentage_pos":precentage_pos,"percentage_neg":precentage_neg, "total_responses" : total_responses}

	return output		 


def init(video_url):
	response = fb_comments.init(video_url)
	print("response is :")
	print(1000*"X")
	# print(response)
	sentiments_arr = sentiment.init(response["message_list"])

	output = get_output(sentiments_arr)

	return output

