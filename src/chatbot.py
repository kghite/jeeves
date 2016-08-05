import random
import datetime

# User input keywords and responses
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["Good morning.", "Good afternoon.", "Good evening."]

def check_for_greeting(sentence):
	"""If any of the words in the user's input was a greeting, return a greeting response"""
	for word in sentence.split():
		if word.lower() in GREETING_KEYWORDS:

			time = datetime.datetime.now().time().hour

			if time >= 3 and time < 12: 
				greeting = 0
			elif time >=12 and time < 6:
				greeting = 1
			else:
				greeting = 2
 			
 			return GREETING_RESPONSES[greeting]

 	return ""

def check_for_empty(sentence):
	if not sentence:
		return "How may I be of service?"
	return ""

def respond_to_input(sentence):
	empty = check_for_empty(sentence)
	greeting = check_for_greeting(sentence)
	return empty + greeting

