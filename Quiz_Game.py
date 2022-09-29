
def check_answer(score=0):
    if x == a:
        print("CORRECT!")
        score += 5
        print()
    else:
        play_again()


def score():
    total_score = str(score) + "/20"
    print(total_score)


def play_again():
    again = input(print("Play again?: Yes/No")).lower()



def start_game():
    score = 0
    which_answer = 0
    while True:
        breakk = 0
        print("Welcome to my quiz game!")
        start = input(print("Would you like to start? Yes/No: ")).lower()
        if not start == "yes":
            break
        for q, a in questions.items():
            x = None
            if breakk == 1:
                break
            while x not in potential_answers:
                if breakk == 1:
                    break
                print(q)
                print(answers[which_answer])
                x = input("Answer? (A, B, C, or D): ").upper()
                if x == a:
                    print("CORRECT!")
                    score += 5
                    which_answer += 1
                else:
                    print("You lose :((((")
                    breakk = 1
                    if breakk == 1:
                        break

        again = input(print("Play again?: Yes/No")).lower()
        if not again == "yes":
            break

questions = {"Who was the first president of the USA?: ": "B",
             "How many moons does the earth have?: ": "A",
             "Who was the first man on the moon?: ": "C",
             "What is the number one cause of death in the USA?: ": "A"
             }

answers = [["A. Thomas Jefferson", "B. George Washington", "C. Alexander Hamilton", "Benjamin Franklin"],
           ["A. 1", "B. 2","C. 3","D. 4"],
           ["A. Buzz Aldrin","B. John Glenn","C. Neil Armstrong","D. Alan Shepard" ],
           ["A. Cardiovascular Disease", "Covid 19", "Medical Malpractice", "Cancer"]]
potential_answers = ["A","B","C","D"]

start_game()