Weight = input('Enter your weight: ')
Weight_measurement = input('(K)g or (L)bs: ')

if Weight_measurement.upper() == 'K':
    converted = Weight / 0.45
    print('weight in lbs ' + str(converted))
else:
    converted = Weight * 0.45
    print('weight in kgs ' + str(converted))
