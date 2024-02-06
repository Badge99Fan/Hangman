import hangman_fig,names,random
print('lets get ready')
lives=6
blanks=[]
words=""
number=random.randint(0,7)
name=names.teachers[number].values()
about=list(names.teachers[number].keys())
for i in name:
    words+=i
for i in words:
    blanks+='_'
print(hangman_fig.logo)
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
        print(hangman_fig.stages[lives])
    if '_' not in blanks:
        print('You guess it right')
        print(f"{blanks}      Your life: {lives}")
        lives=False
if lives==0:
    print('Game over')


