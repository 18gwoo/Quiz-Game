def start_game():
    start = None
    print("Welcome to my quiz game!")
    while not start == "yes":
        start = input("Type yes to start: ").lower()
    while True:
        which_answer = 0
        score = 0
        for q, a in questions.items():
            x = None
            while x not in potential_answers:
                print()
                print(q)
                print(answers[which_answer])
                x = input("Answer? (A, B, C, or D): ").upper()
                if x == a:
                    print()
                    print("CORRECT!")
                    score += 5
                    which_answer += 1
                elif x not in potential_answers:
                    print()
                    print("Please choose A, B, C, or D")
                else:
                    print()
                    print("Incorrect")
                    which_answer += 1
        print()
        print("You have scored: ",end = "")
        total_score = str(score) + "/25"
        print(total_score)

        print()
        again = input("Play again?: Yes/No: ").lower()
        if not again == "yes":
            print()
            print("See you next time!")
            break

questions = {"Who was the first president of the USA?: ": "B",
             "How many moons does the earth have?: ": "A",
             "Who was the first man on the moon?: ": "C",
             "What is the number one cause of death in the USA?: ": "A",
             "What is the area between North and South Korea called?: ": "D"
             }

answers = [["A. Thomas Jefferson", "B. George Washington", "C. Alexander Hamilton", "Benjamin Franklin"],
           ["A. 1", "B. 2","C. 3","D. 4"],
           ["A. Buzz Aldrin","B. John Glenn","C. Neil Armstrong","D. Alan Shepard" ],
           ["A. Cardiovascular Disease", "B. Covid 19", "C. Medical Malpractice", "D. Cancer"],
           ["A. No mans land", "B. The red zone", "C. The Imjin line", "D. The Demilitarized Zone"]]
potential_answers = ["A","B","C","D"]

start_game()