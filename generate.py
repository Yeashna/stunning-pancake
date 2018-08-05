from nltk import pos_tag
from nltk.tokenize import word_tokenize
from mind import thought

def get_reply(igot):

	qtrigger = []
	verb = [] 
	sub = [] 
	moryou = []

	text = pos_tag(word_tokenize(igot))

	for each in text:
		if each[1] in {"WDT","WP","WP$","WRB"}:
			qtrigger.append(each[0].lower())
		if each[1] in {"VB","VBD","VBG","VBN","VBP","VBZ"}:
			verb.append(each[0].lower())
		if each[1] in {"NN","NNS","NNP","NNPS"}:
			sub.append(each[0].lower())
		if each[1] in {"PRP","PRP$"}:
			moryou.append(each[0].lower())

	print("verbs:",verb,"subjectives:",sub)

	reply = thought(qtrigger,verb,sub,moryou)

	print(reply)
	return(reply)