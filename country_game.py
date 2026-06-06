import random
options = ['italy','australia','usa','japan','france','england','canada','china','germany']
pc = random.choice(options)
print("let's start the game ")
you = input('please enter your guess:   ')
print ('pc choice is',pc)
print("you're choice is",you)
if pc == you:
    print('win :)')
else:
    print('sorry you lost')
