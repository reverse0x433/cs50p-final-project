# Quiz Game – A Timed Multiple Choice Python Project

### 🎥 Video Demo:
[Watch here](https://youtu.be/tMK0AV_yoxE?si=9G_1sgvUQi0leyal)


### 📌 Overview

This project is my final submission for Harvard’s CS50P – Introduction to Programming with Python.
It is a *timed multiple-choice quiz game* built using Python that challenges the user with 10 randomly shuffled computer-related questions. Users have a limited amount of time (10 seconds) to answer each question using the inputimeout library. The game provides feedback after each question and displays the final score and percentage.


### 🧠 Features

- ⏱ **Timed Input**: Users must answer each question within 10 seconds using the `inputimeout` module.
- 🔄 **Random Question Order**: Questions are shuffled using Python’s `random.shuffle` to keep each game unique.
- ✅ **Input Validation**: Only accepts answers 'a', 'b', 'c', or 'd'—invalid inputs are handled gracefully.
- 📊 **Final Results**: Displays total correct answers and calculates the percentage score.
- 🧪 **Testing Support**: Includes basic automated tests using `pytest` to validate functionality.
- 💻 **Terminal-Based Game**: The game runs entirely in the terminal and uses minimal external dependencies.


### 🧾 File Descriptions

#### project.py
Contains the main logic:
- `main()`: Sets everything in motion.
- `store()`: Stores all questions and shuffles them.
- `run()`: Displays each question, handles the timeout, validates answers, and gives feedback.
- `result()`: Shows how many questions were answered correctly and computes the score percentage.
- `Questions` class: Defines each question using a simple class structure with prompt, options, and correct answer.


#### test_project.py
Contains simple tests:
- Checks that the `Questions` class initializes properly.
- Uses `capsys` from `pytest` to verify output from the `result()` function.
- Optionally mocks the `run()` function to test flow without real-time input.


#### requirements.txt
This file lists the external dependency required for the project


### 🛠 Design Decisions

- I used a custom Questions class to cleanly structure each question and its data.
- The inputimeout module was chosen to introduce a sense of pressure, similar to real-time quizzes or game shows.
- Randomizing the question order ensures replayability.
- I intentionally kept the UI simple and terminal-based to focus on logic, flow control, and user experience without any GUI complexity.


### 🔍 How to Run

Install required module

pip install -r requirements.txt
python project.py
