import random
words = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop'

 'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful',
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser', 
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen', 
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower'
 'communication']

word_choosen = random.choice(words)
word_length = len(word_choosen)

guess = []

for i in range(word_length):
    guess.append("_")

print("Word to guess:")
print(" ".join(guess))
life = 6



while "_" in guess and life > 0:

    letter = input("guess a letter: ")
    letter_found = False

    for i in range(word_length):
        if letter == word_choosen[i]:
            guess[i] = letter
            letter_found = True
    if not letter_found:
        life -= 1
        print(f"You chose letter {letter}, and that letter is not in the word. You lose a life")

    print(" ".join(guess))
    print(f"Your total life is {life}/6")

if "_" not in guess:
    print("You win!")
else:
    print(f"You lose! the correct word is {word_choosen}")


