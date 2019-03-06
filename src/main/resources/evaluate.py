import numpy as np
import os

pathResults = "C:\\Users\\U96153\\Documents\\NetBeansProjects\\Sphinx\\src\\main\\resources\\results\\en\\"
goldResults = "C:\\Users\\U96153\\Documents\\NetBeansProjects\\Sphinx\\src\\main\\resources\\transcriptions\\en\\"
#comment
dictRes = {}

for f in os.listdir(goldResults):
	fd = open(goldResults+f,"r")
	goldTrans = fd.read().strip().lower().replace("\n"," ").split()
	dictRes[f] = goldTrans

accuracies = []
accuraciesM = []
accuraciesF = []

accuracyPerUtterance = {}
accuracyPerSpeaker = {}

for tf in os.listdir(pathResults):
	fd = open(pathResults+tf,"r")

	if tf.startswith("spk1m2"):
		idSpk = tf.split("_")[0][:-2]
		gender = tf.split("_")[0][-2]
		idRes = tf.split("_")[1]
	else:
		idSpk = tf.split("_")[0][:-1]
		gender = tf.split("_")[0][-1]
		idRes = tf.split("_")[1]


	trans = fd.read().strip().lower().replace("\n"," ").split()
	gold = dictRes[idRes]

	intersection=[i for i in gold if i in trans]
	accuracy = len(intersection)/len(gold)
	if idRes not in accuracyPerUtterance:
		accuracyPerUtterance[idRes] = []
	accuracyPerUtterance[idRes].append(accuracy)

	spkGen = idSpk+gender
	if spkGen not in accuracyPerSpeaker:
		accuracyPerSpeaker[spkGen] = []
	accuracyPerSpeaker[spkGen].append(accuracy)

	accuracies.append(accuracy)

	if gender == "f":
		accuraciesF.append(accuracy)
	else:
		accuraciesM.append(accuracy)

	print(tf+"\t"+ str(accuracy))

print("-------\nAccuracy")
print("General Accuracy"+"\t"+str(np.mean(accuracies)))
print("Male"+"\t"+str(np.mean(accuraciesM)))
print("Female"+"\t"+str(np.mean(accuraciesF)))

print("-------\nAccuracy per utterance")
for idx, accuracyV in accuracyPerUtterance.items():
	print(idx+"\t"+str(np.mean(accuracyV)))

print("-------\nAccuracy per speaker")
for idx, accuracyV in accuracyPerSpeaker.items():
	print(idx+"\t"+str(np.mean(accuracyV)))

