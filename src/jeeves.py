import chatbot
import web_search

ACTION_KEYWORDS = ("search", "play")
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "jeeves")

def respond_to_command(command):
	action_response = complete_action(command)
	return chatbot.respond_to_input(command) + " " + action_response

def complete_action(command):
	action, terms = get_keywords(command)

	if action == "search":
		return web_search.get_readable_results(terms)
	else:
		return "How may I be of service?"

def get_keywords(command):
	
	for word in command.split():
		if word.lower() in ACTION_KEYWORDS:
			action = word
			terms = command.replace(action, "")
 			return word, terms

 	return None, None
