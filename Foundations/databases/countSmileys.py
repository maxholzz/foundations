#-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
#-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
#-Every smiling face must have a smiling mouth that should be marked with either ) or D.
#No additional characters are allowed except for those mentioned.
#Valid smiley face examples:
#:) :D ;-D :~)
#Invalid smiley faces:
#;( :> :} :] 


arr = [':)', ';(', ';}', ':-D']
eyes = [";", ":"]
nose = ["-", "~"]
mouth = [")", "D"]


def count_smileys(arr):

	eyes = [";", ":"]
	nose = ["-", "~"]
	mouth = [")", "D"]

	smiley_count = 0 

	
	for smiley in arr:
		if len(smiley) == 2 and smiley[0] in eyes and smiley[1] in mouth:
			smiley_count +=1
		if len(smiley) == 3 and smiley[0] in eyes and smiley[1] in nose and smiley[2] in mouth:
			smiley_count +=1
		else:
			print("0")

	print(smiley_count)

count_smileys(arr)


