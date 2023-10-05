import random
import words
import art


end_of_game=False

chosen_index=random.randint(0,2)
chosen_word=words.word_list[chosen_index]


print(art.logo)

your_ans=[]
for i in range(0,len(chosen_word)):
    your_ans+="_"

   
              
    
lives=6
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess in your_ans:
        print(f"you have already guessed {guess},try another one!")
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            your_ans[i] = guess
            print(your_ans)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"the letter {guess} is not in the word,try another one. YOU HAVE {lives} LIVES!")
        print(your_ans)
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!!!.")
          
        
    if "_" not in your_ans:
        end_of_game = True
        print("You win")

    print(art.stages[lives])  
    
 



            
