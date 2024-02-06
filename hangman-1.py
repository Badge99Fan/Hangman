##### Figures ####
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

#####


#### NAMES #################################

teachers=[
    {"chuchi mam of the class":"durga" },
    {"Gafadi sir":"prashant"},
    {"Kahlai na padhaunai sir":"yubraj"},
    {"alxi lagnai class":"social"},
    {"khatra avaj vako sir":"account"},
    {"class ko most wanted students":"sonita"},
    {"class ko gafadi student":"sajid"},
    {"bhibishan ko crush":"anjita"}



]
#############################################


import random
print('lets get ready')


lives=6
blanks=[]
words=""
number=random.randint(0,7)
name=teachers[number].values()
about=list(teachers[number].keys())
for i in name:
    words+=i
for i in words:
    blanks+='_'
print(logo)
print(about)

while lives>0:
    print(f"{blanks}      Your life: {lives}")
    user = input('enter the name')

    for position in range(len(words)):
        letters=words[position]
        if user in letters:
            blanks[position]=letters

    if user not in words:
        lives-=1
        print(stages[lives])
    if '_' not in blanks:
        print('You guess it right')
        print(f"{blanks}      Your life: {lives}")
        lives=False
if lives==0:
    print('Game over')


