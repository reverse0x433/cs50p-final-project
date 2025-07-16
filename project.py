from inputimeout import inputimeout, TimeoutOccurred
import random
class Questions:
    def __init__(self,prompt,answer,correct):
        self.prompt=prompt
        self.answer=answer
        self.correct=correct
def main():
    question_prompt=[
        ("What does CPU stand for?",
         ["(a) Central Program Unit", "(b) Central Processing Unit", "(c) Central Processor Utility",
          "(d) Computer Program Unit"],
         "b"),
        ("Which language is used for web development?",
         ["(a) C++", "(b) Java", "(c) Python", "(d) HTML"],
         "d"),
        ("What does HTML stand for?",
         ["(a) HighText Machine Language", "(b) HyperText and Links Markup Language", "(c) HyperText Markup Language",
          "(d) None of these"],
         "c"),
        ("What is the function of RAM in a computer?",
         ["(a) Store permanent data", "(b) Run the operating system", "(c) Temporarily store data for active tasks",
          "(d) Store user passwords"],
         "c"),
        ("Which of these is a Python data type?",
         ["(a) Folder", "(b) Integer", "(c) Window", "(d) Node"],
         "b"),
        ("Who is known as the father of computer?",
         ["(a) Alan Turing", "(b) Charles Babbage", "(c) Bill Gates", "(d) Tim Berners-Lee"],
         "b"),
        ("What does SQL stand for?",
         ["(a) Structured Query Language", "(b) Sequential Query Logic", "(c) Simple Query List",
          "(d) Simple Question Logic"],
         "a"),
        ("Which sorting algorithm has the best average time complexity?",
         ["(a) Bubble sort", "(b) Selection sort", "(c) Insertion sort", "(d) Merge sort"],
         "d"),
        ("Which data structure uses FIFO (First In First Out)?",
         ["(a) Queue", "(b) Array", "(c) Stack", "(d) Linked list"],
         "a"),
        ("What is the time complexity of binary search in a sorted array?",
         ["(a) O(n)", "(b) O(1)", "(c) O(nlog n)", "(d) O(log n)"],
         "d")
    ]
    store(question_prompt)

def store(question_prompt):
    questions = []
    for q, opts, ans in question_prompt:
        questions.append(Questions(q, opts, ans))

    random.shuffle(questions)
    run(questions)

def run(questions, timeout=10):
    print("Welcome to the Quiz")
    print(f"You have {timeout} seconds to answer each question")
    print("Let's go\n")

    score = 0
    for question in questions:
        prompt_text = question.prompt + "\n" + "\n".join(question.answer) + "\nYour answer: "
        try:
            a = inputimeout(prompt=prompt_text, timeout=timeout).lower().strip()

        except TimeoutOccurred:
            print("Time's up!")
            a = ''

        if a not in ['a', 'b', 'c', 'd']:
            print("Invalid or no answer.\n")
        elif a == question.correct:
            print("Correct!\n")
            score += 1
        else:
            correct_text = question.answer[ord(question.correct) - ord('a')]
            print(f"Incorrect. Correct answer: {correct_text}\n")
    b=len(questions)
    result(score,b)

def result(score,b):
    print(f"\nYou got {score}/{b} questions correct!")
    print(f"You have scored {round(int(score)/int(b)*100)}%")

if __name__=="__main__":
    main()

