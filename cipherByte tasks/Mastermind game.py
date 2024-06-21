import random

def generate_random_number(length):
    """Generate a random multi-digit number of given length."""
    return random.randint(10**(length-1), 10**length - 1)

def get_matching_digits(secret_number, guess):
    """Compare the digits of secret_number and guess to find matches."""
    secret_digits = list(str(secret_number))
    guess_digits = list(str(guess))
    
    exact_matches = sum(1 for i in range(len(secret_digits)) if secret_digits[i] == guess_digits[i])
    common_digits = sum(min(secret_digits.count(digit), guess_digits.count(digit)) for digit in set(secret_digits))
    
    return exact_matches, common_digits - exact_matches

def play_mastermind():
    print("Welcome to the Mastermind Game!")
    print("Player 1 will set a multi-digit number.")
    print("Player 2 will try to guess the number.")
    print("Let's begin!")
    
    # Player 1 sets the number
    secret_number_player1 = int(input("Player 1, enter your secret number (4 digits): "))  # Change length as per preference
    
    attempts_player2 = 0
    
    while True:
        guess_player2 = int(input("Player 2, enter your guess: "))
        attempts_player2 += 1
        
        if guess_player2 == secret_number_player1:
            print(f"Player 2 guessed the number {secret_number_player1} correctly in {attempts_player2} attempts!")
            print("Player 2 wins and is crowned Mastermind!")
            break
        
        exact_matches, partial_matches = get_matching_digits(secret_number_player1, guess_player2)
        
        print(f"Player 2, your guess {guess_player2} has:")
        print(f"Exact matches: {exact_matches}")
        print(f"Partial matches: {partial_matches}")
        print("Try again!")
    
    # Player 2 wins, now Player 2 sets the number and Player 1 guesses
    print("\nNow it's Player 2's turn to set the number.")
    secret_number_player2 = int(input("Player 2, enter your secret number (4 digits): "))  # Change length as per preference
    
    attempts_player1 = 0
    
    while True:
        guess_player1 = int(input("Player 1, enter your guess: "))
        attempts_player1 += 1
        
        if guess_player1 == secret_number_player2:
            print(f"Player 1 guessed the number {secret_number_player2} correctly in {attempts_player1} attempts!")
            if attempts_player1 < attempts_player2:
                print("Player 1 wins and is crowned Mastermind!")
        
            else:
                print("Player 2 wins the game!")
            break
        
        exact_matches, partial_matches = get_matching_digits(secret_number_player2, guess_player1)
        
        print(f"Player 1, your guess {guess_player1} has:")
        print(f"Exact matches: {exact_matches}")
        print(f"Partial matches: {partial_matches}")
        print("Try again!")

# Start the game
play_mastermind()
