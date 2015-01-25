def game():
    print "You've just entered the Argument Room!"
    print "Do you take stone, paper or scissors?"
    answer = raw_input("Type stone, paper or scissors and hit 'Enter': ").lower()

    if answer == "stone" or answer == "paper" or answer == "scissors":
        import random
        winning = ['stone' , 'paper' , 'scissors']
        result = (random.choice(winning)) # here the computer randomly choose answer
        print result

        if result == answer:
            print "Dead heat. Let's try again!"
        else:
            if result == "scissors" and answer == "stone":
                print "You won!"
            elif result == "stone" and answer == "paper":
                print "You won!"
            elif result == "paper" and answer == "scissors":
                print "You won!"
            else:
                print "I won!"

    else:
        print "You didn't pick stone, paper or scissors. This is the Argument Room, I've told you that already! Try again."

game()
