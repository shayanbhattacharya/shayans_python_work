print('Welcome to my ITIL v4 quiz')

playing = input('Do you want to play the game? ').lower()

if playing.lower() != 'yes':
    quit()

print('Okay, the quiz will begin now')
score = 0

answer = input('Why is ITSM important? ')
if 'processes' and 'procedures' and 'optimise' and 'use of technology' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is ITSM consolidates processes and procedures that optimize the use of technology in services built around technology")

answer = input('What is Service Management? ')
if 'specialised' and 'organisational capabilities' and 'value to customers' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is A set of specialised, organisational capabilities that enable value to customers in the form of services")


print('You got ' + str(score) + ' questions right')
##print('You got ' + str((score/2)*100) + ' percent')