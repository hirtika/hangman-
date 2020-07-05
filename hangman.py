import random

def play_again():
	answer=input('do you wanna play again? yes/no    ').lower()
	if answer=='yes' or 'y':
		play_game()
	else:
		pass

def get_word():
	words=['apple','mango','banana','strawberry','grapes','litchi']
	return random.choice(words)
	
def play_game():
	alphabet='abcdefghijklmnopqrstuvwxyz'
	word=get_word()
	letters_guessed=[]
	tries=5
	guess=False
	
	
	print('the word contains',len(word),'letters.')
	print(len(word)*'-')
	while guess==False and tries > 0:
		print('you have '+str(tries)+' tries')
		guessed=input('please enter one letter or a word    ').lower()
#if user ne letter dala
		if len(guessed)==1:
			if guessed not in alphabet:
				print('you have not entered a letter')
			elif guessed in letters_guessed:
				print('you have already guessed this letter')
			elif guessed not in word:
				print('wrong letter')
				letters_guessed.append(guessed)
				tries=tries-1
			else:
				print('congratulations')
				letters_guessed.append(guessed)
#if user ne pura word dala at a time
		elif len(guessed)==len(word):
			if guessed==word:
				print('congrats you have guessed the correct word')
				guess=True
			else:
				print('incorrect word')
				tries=tries-1
		else:
			print('length does not match')
			
		status=''
		if guess==False:
			for i in word:
				if i in letters_guessed:
					status=status+i
				else:
					status=status+'-'
		print(status)
		   
		if status==word:
			print('well done')
			guess=True
		elif tries==0:
			print('your tries are over')
	play_again()
	