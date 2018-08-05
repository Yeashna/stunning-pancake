from nltk.tokenize import regexp_tokenize, word_tokenize

positive = {"yes","course","affirmative","fine","okay","right","definitely","do","yup","ya","ok"}
negetive = {"n't","no","not","negetive","never","nope"}


def get_sense(base):	#define if positive or negetive
	sense = ""
	#words = regexp_tokenize(reply,"[\w']+")
	words = word_tokenize(base)

	for each in words:
		if each.lower() in positive:
			sense = "positive"
	for each in words:
		if each.lower() in negetive:
			sense = "negetive"

	print(sense)
	return(sense)

def get_ans(negpos,attire,memorys):

	if (negpos == "positive") and (attire == None):
		return([memorys,""])
	elif (negpos == "negetive") and (attire != None):
		return(["ok i won't do that",""])
	else:
		return(attire)