print('Welcome to my ITIL v4 quiz')

playing = input('Do you want to play the game? ').lower()

if playing.lower() != 'yes':
    quit()

print('Okay, the quiz will begin now')
score = 0

# Question 1
answer = input('Why is ITSM important? ')
if 'processes' and 'procedures' and 'optimise' and 'use of technology' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is ITSM consolidates processes and procedures that optimize the use of technology in services built around technology")

# Question 2
answer = input('What is Service Management? ')
if 'specialised' and 'organisational capabilities' and 'value to customers' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is A set of specialised, organisational capabilities that enable value to customers in the form of services")
    
# Question 3    
answer = input('What is value? ')
if 'importance' and 'benefits' and 'usefulness' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is importance, benefits and usefulness")

# Question 4    
answer = input('What do you need good understanding of when it comes to providing value? ')
if 'value' and 'enabled through' and 'services' and 'nature' and 'scope' and 'stakeholders' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is How value is enabled through services and the nature and scope of the stakeholders involved")

# Question 5    
answer = input('What is an organization? ')
if 'person' and 'people' and 'services' and 'own functions with responsibilities, relationships and authorities to achieve its objectives' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is A person, or group of people with its own functions with responsibilities, relationships and authorities to achieve its objectives.")

# Question 6    
answer = input('What is a user? ')
if 'uses' and 'the' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is Someone who uses the service.")

# Question 7    
answer = input('What is a sponsor? ')
if 'fund' and 'the' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is Someone who funds the service.")

# Question 8    
answer = input('What is a customer? ')
if 'set' and 'requirements' and 'for' and 'the' and 'service' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is Someone who sets the requirements for the service.")
    
# Question 9    
answer = input('Other than customers, sponsors and users, name three other possible stakeholders. ')
if 'community' and 'employees' and 'shareholders' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is Other stakeholders include the community, employees and shareholders.")

# Question 10    
answer = input('What is the meaning of the word service in ITIL?. ')
if 'value' and 'co-creation' and 'requirements' and 'satisfaction' and ' do not' and 'costs' and 'risks' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is A service enables value co-creation according to the customer's requirements for satisfaction, making sure they do not take on the associated costs or risks.")    
    
# Question 11    
answer = input('What is a product in ITIL?. ')
if 'configuration' and 'resources' and 'organisation' and 'valuable' and 'customers' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is A configuration of resources created by the organisation that could be potentially valuable to customers.") 

# Question 12    
answer = input('What are the 4 dimensions of ITSM?. ')
if 'information' and 'security' and 'people' and 'organisation' and 'partners' and 'suppliers' and 'value streams' and 'processes' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is Organisation and people, information and security, value streams and processes and partners and suppliers.")    

# Question 13    
answer = input('What is the key output in IT services?. ')
if 'information' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is Information.")   

# Question 14    
answer = input('For which services should the 4 dimensions be considered?. ')
if 'All services' in answer.lower():
    print('Correct')
    score += 1
else:
    print("Wrong. The correct answer is All of them.")       

   
        

print('You got ' + str(score) + ' questions right')
print('You got ' + str((score/14)*100) + ' percent')

 