import random
turns = 0
correct_digits_and_position = 0
correct_digits_only = 0
def random_digits():
    """
    random_digits selects random digits for the four digit code 
    and stops the code from have dublicates.
    """
    code = [0, 0, 0, 0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8.\
 You have 12 turns to break it.')
    return code


def input_and_length(code,turns):
    """
    input_and_length only accepts the input if the length is 4 digits
    and if its only digits.
    the correct position and code from the input with be counted
    and if the input is correct it will break the loop and print out
    that you won and what the selected code was. 
    """
    correct = False
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue

        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1
        if correct_digits_and_position == 4:
            print('Congratulations! You are a codebreaker!')
            print('The code was: '+str(code))
            break
        else:
            print('Turns left: '+str(12 - turns))
    return correct_digits_and_position and correct_digits_only


def run_game():
    code = random_digits()   
    input_and_length(code, turns)


if __name__ == "__main__":
    run_game()