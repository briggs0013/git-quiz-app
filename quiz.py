questions = [
    {
        "question": "What command initializes a new Git repository?",
        "options": ["A) git start", "B) git init", "C) git new", "D) git create"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    print("Welcome to the Git Quiz!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        user_answer = input("\nYour answer: ").strip().upper()
        
        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The answer was {q['answer']}\n")
    
    print(f"Quiz complete! You scored {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz(questions)