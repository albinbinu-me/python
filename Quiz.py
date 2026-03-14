questions = (
    "how many elements are in periodic table",
    "which animal lays largest eggs",
    "what is the abundant gas in the atmosphere",
    "how many bones are in human body",
    "which planet in the solar system is the hottest"
)

options = (
("A. 116","B. 117","C. 118","D. 119"),
("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
("A. 206","B. 207","C. 208","D. 209"),
("A. Mercury","B. Venus","C. Earth","D. Mars")
)

answer = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("-----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    user_input = input("enter your guesses: ").upper()
    guesses.append(user_input)
    if user_input == answer[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
    question_num += 1

print(f"total score is {score}")