from quiz import Quiz

if __name__ == "__main__":
    quiz = Quiz("questions")
    quiz.load_questions()
    quiz.run_quiz()
    quiz.print_stat()
