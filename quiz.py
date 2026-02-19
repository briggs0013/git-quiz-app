questions = [
  {
        "question": "What command initializes a new Git repository?",
        "options": ["A) git start", "B) git init", "C) git new", "D) git create"],
        "answer": "B"
    },
    {
        "question": "What command stages a file?",
        "options": ["A) git commit", "B) git push", "C) git add", "D) git stage"],
        "answer": "C"
    },
    {
        "question": "What command saves a snapshot of staged files?",
        "options": ["A) git save", "B) git commit", "C) git push", "D) git log"],
        "answer": "B"
    },
    {
        "question": "What command shows your commit history?",
        "options": ["A) git history", "B) git status", "C) git log", "D) git show"],
        "answer": "C"
    },
    {
        "question": "What command shows unstaged changes?",
        "options": ["A) git diff", "B) git log", "C) git status", "D) git show"],
        "answer": "A"
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