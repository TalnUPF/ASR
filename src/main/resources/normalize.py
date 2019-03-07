from __future__ import print_function
import os
import re
from num2words import num2words

class Normalization:

	month_dict = {"Jan": "January","Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}

	def __init__(self, path):
		self.abb_dict = self.loadDict("dictSubstitutions.txt")
		self.path = path

	def loadDict(self,path):
		abb_dict = {}
		fd = open(path,"r")
		lines = fd.readlines()
		for line in lines:
			key,value = line.split(":")
			abb_dict[key] = value

		return abb_dict

	def normalize(self):

		for f in os.listdir(self.path):
			fd = open(self.path+f,"r")
			rs = open(self.path+f[:-4]+"_norm.txt","w+")
			sent = fd.read()
			sent = sent.replace('%',' percent')
			sent = self.acronym_punct_sub(sent)
			
			new_text = []
			date_match = False

			prev = None
			for word in sent.split(" "):
				abb_match = re.search(r'[A-Z][a-z]{2}\.?',word)
				nElemsInit = len(new_text)
				if word in self.abb_dict:
					new_text.append(self.abb_dict[word])
					
				if abb_match:			
					keyDict = word.replace(".","")

					if keyDict in self.month_dict.keys():
						date_match = True
						sub = self.month_dict[keyDict]
						new_text.append(sub)

				self.number_sub(word, prev,new_text)
				nElemsFinal = len(new_text)
				if nElemsFinal == nElemsInit:
					new_text.append(word)
					
				prev = word

			new_file = " ".join(new_text)
			## Final subtitution for unused puntuation marks
			sent_punt = re.sub(r'[\.\,\:\;\"\?\!\_]','',new_file)
			sent_punt = sent_punt.replace('-',' ')
			rs.write(sent_punt.lower())
			rs.close()
			fd.close()

	def acronym_punct_sub(self, sent):
		# Code to group together strings and perform substitutions. Acronyms with punctuation
		acro_match = re.search(r'([A-Z])\.([A-Z])\.',sent)
		if acro_match:
			word_acro = acro_match.group(1) + " " + acro_match.group(2)
			sent = re.sub(r'[A-Z]\.[A-Z]\.',word_acro,sent)
		return sent

	def number_sub(self, word, prev, new_text):
		year_match = re.search(r'[0-9]{4}', word)
		num_match = re.search(r'[0-9]*\,?[0-9]+', word)

		# Date with ordinal number
		if prev in self.month_dict.values() or prev in self.month_dict.keys():
			date = re.search(r'[0-9][0-9]', word)
			if date:
				number = date.group()
				day = num2words(int(number), to='ordinal')
				full_date = re.sub(r'[0-9][0-9]',day,word)
				new_text.append("the")
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
				letters = letters[1:]
			new_text.append(letters)
			new_text.append("dollars")


	

if __name__ == '__main__':
	path = "C:\\Users\\UPF\\Desktop\\sentences_tobiTAG\\preprocess\\docs\\file\\"
	iN = Normalization(path)
	iN.normalize()