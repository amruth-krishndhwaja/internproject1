def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(options):
                return answer == correct_answer
            else:
                print("Please enter a valid option number.")
        except ValueError:
            print("Please enter a number.")

def quiz_game():
    questions = [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct_answer": 2
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
            "correct_answer": 1
        },
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Rome"],
            "correct_answer": 3
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Osmium", "Gold", "Oganesson"],
            "correct_answer": 1
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_answer": 2
        }
    ]

    score = 0

    for i, question_info in enumerate(questions):
        print(f"\nQuestion {i + 1}:")
        correct = ask_question(question_info["question"], question_info["options"], question_info["correct_answer"])
        
        if correct:
            print("Correct!")
            score += 1
        else:
            correct_answer = question_info["options"][question_info["correct_answer"] - 1]
            print(f"Incorrect! The correct answer was: {correct_answer}")

    print(f"\nYour final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    quiz_game()

