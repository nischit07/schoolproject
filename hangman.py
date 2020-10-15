#TO DO: Add a word generator instead of list
import random
#from RandomWordGenerator import RandomWord
#words=RandomWord(max_word_size=5)
#words.generate()
words= ["Nischit", "Rocket", "Testing", "Planning" ]
selection= random.choice(words)
right=['_']*len(selection)
wrong=[]
print("The number has ", len(selection), "letters")
def update():
    for i in right:
        print(i, end = ' ')
    print()
update()
while True:
    print("=====================================================")
    guess=input("Enter a letter: ")
    if guess in selection:
        index=0
        for i in selection:
            if i==guess:
                right[index]=guess
            index+=1
        update()
    else:
        if guess not in wrong:
            wrong.append(guess)
            print("Letters used so far: ", " ".join(wrong))
        else:
            print("You've already guessed that letter!!!")
        print("wrong")
    if len(wrong)>2:
        print("You lose")
        print("The selected word is", selection)
        break
    if '_' not in right:
        print("TASK COMPLETED!!!!")
        break