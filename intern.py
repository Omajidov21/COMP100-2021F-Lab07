# the given code for 3rd study question

recovered = [{'name': 'Laura', 'tested': [2, 10, 22]},
             {'name': 'Sergey', 'tested': [12, 5, 2, 14]},
             {'name': 'Thomas', 'tested': [7, 15]},
             {'name': 'Angjoo', 'tested': [12, 18, 23]}]

keep = []
for patient in recovered:
  min = min(patient['tested'])
  if min < 5:
    keep = keep.append(patient['name'])

print(keep)

# PART 2

inQuarantine = [{'name': 'Anurak', 'since': 2, 'tested': [2], 'symptoms': ['fever', 'cough', 'loss of smell']},
                {'name': 'Jonas', 'since': 4, 'tested': [6, 4], 'symptoms': ['fever', 'cough']}]

day = 0
while day <= 30:
  if day == 3:
    # add the new patient
    new_patient = {'name': 'Melanie', 'since': 0, 'tested': [0], 'symptoms': ['fever']}
    inQuarantine.add(new_patient)

  for patient in Quarantine:
    # update the number of days in quarantine
    patient['since'] += 1

    # increment the number of days passed since the patient was tested
    patient['tested'] += 1

    if day == 1:
      # update the symptoms
      if patient['name'] == 'Anurak':
        patient['symptoms'].del('fever')
      elif patient['name'] == 'Jonas':
        patient['symptoms'].extend('tiredness')

    elif day == 2:
      if patient['name'] == 'Anurak':
        # correct the typo
        patient['name'][-1] = 'g'

      elif patient['name'] == 'Jonas':
        # add a new test
        patient['tested'] += 1

    elif day == 3:
      # update the symptoms
      if patient['name'] == 'Anurak':
        patient['symptoms'].add('fever')

  if day < 3 or day == 29:
    # Show the updates
    print('Day: ', day, inQuarantine)
    print('-'*80)

    day += 1