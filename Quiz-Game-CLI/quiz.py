 ##Quiz Game CLI##

def start_quiz():
    score = 0

    questions = [
        {
            "question": "1. What is the capital of Ghana?",
            "options": ["A. Kumasi", "B. Accra", "C. Tamale", "D. Takoradi"],
            "answer": "B"
        },
        {
            "question": "2. What does CPU stand for?",
            "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Control Processing Unit", "D. Central Program Unit"],
            "answer": "A"
        },
        {
            "question": "3. Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
            "answer": "B"
        },
        {
            "question": "4. What is 5 + 3?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "C"
        },
        {
            "question": "5. Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        }
    ]

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is", q["answer"], "\n")

    print("Quiz Finished!")
    print("Your final score is:", score, "out of", len(questions))
    print()


def main():
    while True:
        print("===== Quiz Game =====")
        print("1. Start Quiz")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


main()