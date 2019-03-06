clearinfo
form Parameters
  text directory C:\Users\UPF\Desktop\sentences_tobiTAG\
  text spk spk5m\
endform

fulldir$ = directory$ + spk$
Create Strings as file list: "list", fulldir$ + "/*.wav"
numberOfFiles = Get number of strings
for ifile to numberOfFiles
	selectObject: "Strings list"
	file$ = Get string: ifile
	basename$ = file$ - ".wav"
	Read from file: fulldir$ + file$
	#Convert to mono
	#Resample: 16000, 50
	Save as raw 16-bit little-endian file: directory$ + spk$ + basename$ + ".16le"
endfor

select all
Remove

appendInfoLine: "Files have been converted"
