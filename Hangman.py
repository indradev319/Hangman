import random

input_file_path = r'F:\Coding\Python\Python_Notess.py\list of words.txt'

with open(input_file_path, 'r') as file:
    word_lst = file.readlines()
    

max_attempt = 6

# funtion to choose a random word
def choose_word():
    word = random.choice(word_lst)
    return word.strip()


# funtion to print blank space as well as fill correctly guessed letter
def display_word(word, correctly_guesssed_letters):
    result = ""
    for letter in word:
        if letter in correctly_guesssed_letters:
            result += letter
        else:
            result += "_ "
    return result




# function to take input from user to guess a letter
def guess_letter(word):
    
    guess_a_lettter = input("Guess a letter :")
    return guess_a_lettter

# function to restart a new game again
def play_again():
    play_again = input("\nWould you like to play again? (y/n)\n")
    if play_again == "y":
        hangman()
    else:
        print("\nThanks for playing\n")
        



# funtion to initialize a hangman game
def hangman():

    print(f"\nWelcome to Hangman!\n\nYou will have {max_attempt} incorrect attempts to guess the word correctly\n\n")

    attempt = 0
    guessed_letter = ""
    guessed_letter_list = ""
    correctly_guesssed_letters = ""
    word = choose_word()
    
    while attempt < max_attempt:
        if len(set(guessed_letter_list)) > 0:
            print("\n\nYour guessed letters are : ", set(guessed_letter_list))
        if attempt == 0:
            print(f"You have {max_attempt-attempt}  attempts remaining")
        else:    
            print(f"You have {max_attempt-attempt} more attempts remaining")

        print("word : ",display_word( word ,correctly_guesssed_letters))

                
        guessed_letter = guess_letter(word)

        if guessed_letter in guessed_letter_list:
                print("You have already guessed that letter, try another letter ")
                continue
        guessed_letter_list += guessed_letter

        if guessed_letter in word:                      
            print("You guessed a letter correctly :)")
            correctly_guesssed_letters += guessed_letter
            
        else:
            attempt += 1
            if attempt < max_attempt:
                print("wrong guess!, try again \n")
            else:
                print(f"sorry! You are out of attempts. \nGame Over!!! \n\nThe word was ---{word}---")
                play_again()
                break
        
        if set(word) == set(correctly_guesssed_letters):
            print(f"\nword : {word}\nCongratualtions!!! you have guessed the word correctly\n ")
            play_again()
            break

     
hangman()


