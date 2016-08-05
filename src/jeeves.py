import chatbot
import web_search

def respond_to_command(command):
	action_response = complete_action(command)
	return chatbot.respond_to_input(command) + action_response

def complete_action(command):
	action, terms = get_keywords(command)

	if action = "search":
		web_search.get_readable_results(terms)
