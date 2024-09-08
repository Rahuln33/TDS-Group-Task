def quiz():
    questions = {
        "What is the capital of France?": "a",
        "What is 2 + 2?": "b",
        "Which planet is known as the Red Planet?": "c"
    }

    options = {
        "a": ["a) Paris", "b) Rome", "c) London"],
        "b": ["a) 3", "b) 4", "c) 5"],
        "c": ["a) Earth", "b) Jupiter", "c) Mars"]
    }

    score = 0

    for question, correct_answer in questions.items():
        print(f"\n{question}")
        for option in options[correct_answer]:
            print(option)

        answer = input("Enter your answer (a/b/c): ").lower()
        if answer == correct_answer:
            score += 1

    print(f"\nYour score: {score}/{len(questions)}")

quiz()
