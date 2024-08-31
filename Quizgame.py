print("********************")
print("welcome to my quiz game !!!")

# firs for qustion bank having list and in this we have dictionary
# in that we have key and value pair
# like in the text the question is a pair and answer and A is pair

question_bank = [
    {"text": "the ability of one class to aquire methds and attributes from another class is called.____?", "answer": "A"},
    {"text": "which of the following is a type of inheritence?", "answer": "D"},
    {"text": "what type of inheritence  has multiple subclasses to a single super class?.", "answer": "C"},
    {"text": "what is the depth of multilevel inheritence in python?", "answer": "C"},
    {"text": "what does MRO stand for?", "answer": "B"}

]

# for answer options we create another list and iam having sub list


options = [["A.Inheritence", "B.abstraction", "C.polymorphism", "D.objects"],
           ["A.single", "B.double", "C.multiple", "D.both A and C"],
           ["A. multiple Inheritence", "B.multilevel Inheritence", "C.Hierarchical Inheritence", "D.none of these"],
           ["A.two level", "B.three level", "C.any level", "D.none of these"],
           ["A.method recursive object", "B.method resolution order", "C.mair resolution order",
            "D.method resolution object"]

           ]

score = 0

def check_answer(guess, correct_answer):
    if guess == correct_answer:
        return True
    else:
        return False


# for printing questions we take the range of question question_bank
for question_num in range(len(question_bank)):  # 0 1 2 3 4
    # print the questions in question question_bank

    print("****************************")
    print(question_bank[question_num]["text"])
    # for printing options we use for loop and print using question_num index
    for i in options[question_num]:
        print(i)

    guess = input("enter your answer(A/B/C/D):").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("correct answer")
        score += 1
    else:
        print("incorrect answer")
        print(f"the correct answer is {question_bank[question_num]['answer']}")
        # after every answer we print the current score
    print(f"your current score is {score}/{question_num + 1}")
print(f"your final score is {score} correct answers")
print(f"your score is {(score / len(question_bank)) * 100}%")



