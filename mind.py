import database_handler as data
def thought(question,verbs,subs,meoryou):

	mylen = len(meoryou)-1

	def subjectbasis(argument):

		for each in subs:
			if each in data.check_sub:
				if argument == "notsure":
					return(["comm checkpulse","Do you want me to check your pulse?"])
				else:
					return(["comm checkpulse",""])

			elif each in data.hello_sub:
					return(["Hi there",""])

			elif each in data.name_sub:
				if argument == "notsure":
					return(["Hi I'm Maci","Are you asking my name?"])
				elif meoryou[mylen] in {"your","you"}:
					return(["Hi I'm Maci",""])
				elif meoryou[mylen] in {"my"}:
					return("I am not interested at wasting storage.","Did you tell me your name?")

			elif each in data.help_sub:
				if argument == "notsure":
					return(["comm gethelp","Are you feeling bad? Would you like me to get help?"])
				else:
					return(["comm gethelp",""])

					


	if len(question) > 0 :
		value = subjectbasis("")
		return(value)
	
	elif len(verbs) > 0:
		value = subjectbasis("")
		return(value)

	else:
		value = subjectbasis("notsure")
		return(value)