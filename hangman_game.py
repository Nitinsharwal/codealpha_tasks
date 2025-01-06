import random

words_list = ['tomato','potato', 'apple', 'grains', 'array'] #we can also add more items by add text file 
chance = 7
word = random.choice(words_list)
word.lower()
guess = '-'*len(word)
while (chance!=0):
    print(guess)
    user = input('Guess a letter : ').lower()
    if user in word:
        for i in range(len(word)):
            if word[i]==user:
                guess = guess[:i]+ user + guess[i+1:]
        if guess == word:
            print('You Won !')
    else:
        chance -=1
        print(f'No match. You have only {chance} chance..!')
else:
    print('You loose..!')
print(f'The correct word is {word}')

