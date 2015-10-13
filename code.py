import random
def Findsecretnum (num):
	#return a string that is num long, made up of unique random digits 
	numbers = list(range(10))
	random.shuffle(numbers)
	secretnum = ""
	for i in range (num):
		secretnum += str(numbers [i])
	return secretnum
def getclues(guess, num):
	#Return string w/ clues
	if guess == secretnum:
		return "You guessed right!"
	clue = []
	for i in range (len(guess)):
		if guess [i]== secretnum [i]:
			clue.append("Beyonce")
		elif guess[i] in secretnum:
			clue.append("Kelly")
	if len (clue)==0:
		return "Michelle"
	clue.sort ()
	return "".join(clue)
def OnlyDigits (num):
	#return true if num = string made up of digits else FALSE
	if num =="":
		return False
	for i in num:
		if i not in "0 1 2 3 4 5 6 7 8 9".split():
			return False
	return True 
def playAgain():
	#return true if player wants to play gain/else false
	while True:
		playAgain = raw_input ("Do you want to play again (Y/N)?")
		play = False
		if playAgain == "N" or playAgain == "n":
			print "Nobody likes a sore loser, Goodbye!"
			break
		elif playAgain == "Y" or playAgain =="y":
			print "I hope you can figure out the answer soon, It'm not getting any younger"
			play=True
			break
		else:
			print "Sorry, I couldn't understand your answer...It's either Y or N (Not too complicated for you I hope!)"
	return play 

NUMDIGITS = 2
MAXGUESS = 10 

print "I am thinking of a 2 digit number (& 0's can be included ie 08), try and guess what it is. I will give you a Destiny's Child's clues on whether you are wrong/sort of right/correct"
print "Here are some clues: "
print "Kelly:\tOne digit is correct, BUT in the wrong position"
print "Beyonce:\tOne digit is correct AND in the right position"
print "Michelle: \tNo digit is correct. Wahhh"

while True:
	secretnum = Findsecretnum(NUMDIGITS) 
	print " I have a number in mind....you have %s guesses to get it right!" %MAXGUESS
	numGuesses= 1
	while numGuesses <=MAXGUESS:
		guess= ""
		while len(guess) != NUMDIGITS or not OnlyDigits (guess):
			guess = raw_input ("Guess Number is")
		clue = getclues (guess, secretnum)
		print clue
		numGuesses += 1

		if guess == secretnum:
			break
		if numGuesses>MAXGUESS: 
			print "You LOSE MICHELLE, the answer was:" + secretnum
		if not playAgain ():
			break

		