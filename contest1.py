from contest2 import Question

question_prompts = [
    "How many eyes do people have?:\n a) 1\n b) 2\n c) 3\n\n",
    "How many fingers do people have in one hand?:\n a) 3\n b) 4\n c) 5\n\n",
    "How many letters are there in the word 'book'\n a) 4\n b) 3\n c) 2\n\n"
]
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print()
    print("You got", str(score), "/", str(len(questions)), "correct answers")

run_test(questions)

