
import urllib
import wikipedia

def get_readable_results(search_term):
	try:
		response = wikipedia.summary(search_term, sentences=4)
	except wikipedia.exceptions.DisambiguationError:
		response = "That is an ambiguous search term. Can you be more specific?" 

	return response
