import sys

list = sys.argv
if len(list)==3:
	if (not int(list[1])%7) and (not int(list[2])%7):
		print("True")
	else:
		print("False")
else:
	print("2 argument gir")
