# Testing & Debugging Study Questions

1. 
```
StarkSiblings = ['Arya', 'Robb', 'Jon', 'Bran', 'Sansa', 'Rickon']
StarkParents = ['Ned', 'Catlyn']
LannisterSiblings = ['Tyrion', 'Jamie', 'Cersei']
LannisterParents = ['Tywin', 'Joanna']
TargaryenSiblings = ['Rhaegar', 'Viserys', 'Daenerys']
TargaryenParents = ['Aerys', 'Rhaella']
```

Given the three most famous families from the GoT universe, write a match-making function to randomly pick two people to marry from the universe, and print a judgement either by:

* printing a message approving their union
* warning if at least one of them is already married
* asking "why again" if they are married as a couple
* disapproving if they are siblings, or if they have a child-parent relationship with separate messages
* (bonus) a cynical disapproval if the couple is Jamie and Cersei
* (bonus) a special warning if the couple is Jon and Daenerys

**Hint:** You can use assertions for very strong disapprovals.

2. Let's say we are collecting information from a user by asking them basic questions such as their name, age, profession, telephone number, and address. By using a try block and appropriate exceptions, make sure that user enters a valid input for each, e.g. string for the name, the profession, and the address; and integer for the age and the telephone number. Persistently ask for the input in the right format by properly informing the user, as long as they enter it wrong.

* Take care of the cases (by accepting and converting them to the int format) where the user puts space or dash in the phone number or enters parantheses for the area code.
* Reject the entry if the user is older than 100 or younger than 10.
* Try to format the address in a more fine-grained way by asking the street name, house number, zip code, city etc. separately with proper types for each.

3. In this question, there is a story. The aim is that finding the mistakes/bugs in the given code. 

The university health center hires an intern to keep track of people with COVID at the university. 
The intern decides to store and update the information in a list of dictionaries:
```
recovered = [{'name': 'Laura', 'tested': [2, 10, 22]}, 
             {'name': 'Sergey', 'tested': [12, 5, 2, 14]}, 
             {'name': 'Thomas', 'tested': [7, 15]}, 
             {'name': 'Angjoo', 'tested': [12, 18, 23]}]
```

In addition to the names of patients, the intern stores the information about how many days ago they were tested.

1. The health center asks the intern to find everyone recovered if the last time they were tested is more than 5 days ago to test them again. The intern writes the code below but he cannot manage to produce the expected result on the small test set above. The returned list needs to include two names only, `['Thomas', 'Angjoo']`, but the intern cannot even manage to run the program properly.

Can you help them fix their error(s) in the program?

```
keep = []
for patient in recovered:
  min = min(patient['tested'])
  if min < 5:
    keep = keep.append(patient['name'])

print(keep)
```

2. Then, the health center asks the intern to keep track of people in quarantine. In addition to their name and test days, they have additional information showing since how many days the patient has been in quarantine and what kind of symptoms they show.
Every day for a month during the internship, i.e. 30 days, the intern is supposed to update the data according to phone calls to people in quarantine. 

```
inQuarantine = [{'name': 'Anurak', 'since': 2, 'tested': [2], 'symptoms': ['fever', 'cough', 'loss of smell']},
                {'name': 'Jonas', 'since': 4, 'tested': [6, 4], 'symptoms': ['fever', 'cough']}]
```

Through the phone calls on the first day, the intern is given these notes:
  * remove 'fever' from Anurak's symptoms
  * add 'tiredness' to Jonas's symptoms

The second day:
  * we made a typo in a patient's name, it is supposed to be 'Anurag', not 'Anurak'.
  * add a new test to Jonas

The third day:
  * add a new patient named 'Melanie' due to fever, tested today
  * add fever back to Anurag's symptoms

Please find the intern's code looks on the fourth day in "intern.py". Unfortunately, nothing works as expected. There are more than 10 instances of common mistakes in the code. Can you help the intern by correcting the code to do the right updates according to the notes?

After correcting all the problems in the code, the output should look as follows:

```
Day:  0 [{'name': 'Anurak', 'since': 3, 'tested': [3], 'symptoms': ['cough', 'loss of smell']}, {'name': 'Jonas', 'since': 5, 'tested': [7, 5], 'symptoms': ['fever', 'cough', 'tiredness']}]
--------------------------------------------------------------------------------
Day:  1 [{'name': 'Anurag', 'since': 4, 'tested': [4], 'symptoms': ['cough', 'loss of smell']}, {'name': 'Jonas', 'since': 6, 'tested': [8, 6, 0], 'symptoms': ['fever', 'cough', 'tiredness']}]
--------------------------------------------------------------------------------
Day:  2 [{'name': 'Anurag', 'since': 5, 'tested': [5], 'symptoms': ['cough', 'loss of smell', 'fever']}, {'name': 'Jonas', 'since': 7, 'tested': [9, 7, 1], 'symptoms': ['fever', 'cough', 'tiredness']}, {'name': 'Melanie', 'since': 1, 'tested': [1], 'symptoms': ['fever']}]
--------------------------------------------------------------------------------
Day:  29 [{'name': 'Anurag', 'since': 32, 'tested': [32], 'symptoms': ['cough', 'loss of smell', 'fever']}, {'name': 'Jonas', 'since': 34, 'tested': [36, 34, 28], 'symptoms': ['fever', 'cough', 'tiredness']}, {'name': 'Melanie', 'since': 28, 'tested': [28], 'symptoms': ['fever']}]
--------------------------------------------------------------------------------
```