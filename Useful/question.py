#Description:  Asks question to user repeatedly until they give a valid response  
#Choices:  Yes No Question, Integer Only Question
#Author:  Justin Stevens
def ask_yes_no(question, a1, a2):
	"""Ask yes no question with options a1, a2"""
	answer=raw_input(question)
	while answer not in (a1, a2):
		answer=raw_input(question)
	return answer
def ask_for_int(question):
	"""Asks yes no question until integer response"""
	while(1):
		answer=raw_input(question)
		try:
			answer=int(answer)
		except ValueError:
			pass
		else:
			return answer


