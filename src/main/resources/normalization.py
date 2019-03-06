import os
import re
from num2words import num2words
#https://pypi.org/project/num2words/

goldResults = "C:\\Users\\UPF\\Desktop\\sentences_tobiTAG\\preprocess\\docs\\file\\"

acronyms = ["SEC", "UN"]

for f in os.listdir(goldResults):
	fd = open(goldResults+f,"r")
	rs = open(goldResults+f[:-4]+"_norm.txt","w+")
	sent = fd.read().strip()
	#Before removing punctuation look for acronyms, dates, abbreviatons.
	
	# Search for years
	### There is a need to tokenize into word in this case
	new_text = []
	pre_word = ""
	for word in sent.split(" "):
		date_list = ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		year_match = re.search(r'[0-9]{4}', word)
		num_match = re.search(r'[0-9]*\,?[0-9]+', word)
		date_match = 0
		if pre_word != "":
			for item in date_list:
				date = re.search(item, pre_word)
				if date:
					date_match = 1
		if date_match == 1:
			date = re.search(r'[0-9][0-9]', word)
			if date:
				number = date.group()
				day = "the " + num2words(int(number), to='ordinal')
				full_date = re.sub(r'[0-9][0-9]',day,word)
				new_text.append(full_date)
		elif year_match:
			number = year_match.group()
			year = num2words(int(number), to='year')
			letters = re.sub(r'[0-9]{4}',year,word)
			new_text.append(letters)
		## insert condition to detect dates, currency symbols
		elif num_match:
			number = num_match.group()
			int_n = re.sub(r'\,','',number)
			money = num2words(int(int_n))
			letters = re.sub(r'[0-9]*\,?[0-9]+',money,word)
			# condition on currency symbols
			currency = re.search(r'\$',letters)
			if currency:
				letters = letters[1:] + " dollars"
			new_text.append(letters)
		else:
			new_text.append(word)
		pre_word = word

#### Simple substitutions
	#sent_hyphen = re.sub(r'[\-]',' ',sent)
	#sent_percent = re.sub(r'\%',' percent',sent)

##################
	# Code to group together strings and perform substitutions
#	acro_match = re.search(r'([A-Z])\.([A-Z])\.',sent)
#	sent_acro = ""
#	if acro_match:
#		word_acro = acro_match.group(1) + " " + acro_match.group(2) + " "
#		sent_acro = re.sub(r'[A-Z]\.[A-Z]\.',word_acro,sent)
##############

	## Final subtitution for unused puntuation marks
	#sent_punt = re.sub(r'[\.\,\:\;\"\?\!\_]','',sent)
	rs.write(" ".join(new_text))
	#rs.write(sent_year.lower())