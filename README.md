## Quiz Game (extract items from a JSON file)

This Python code defines a simple quiz application that reads questions from a JSON file, presents them to the user, collects their answers, evaluates the quiz, and displays the user's score.

Here's a step-by-step explanation of the code:

**Importing Libraries:**

The code starts by importing the json module, which is used to work with JSON data in Python.

`load_questions(filename)` Function:
- This function takes a filename as an argument, opens the specified file in read mode, and uses `json.load()` to parse the JSON data from the file into a Python object (a list of questions). It then returns the list of questions.

`display_question(question)` Function:
- This function takes a question dictionary as an argument and displays the question and its options (a, b, c, d) to the user.

`get_user_answer()` Function:
- This function prompts the user to enter their answer (a, b, c, or d) and ensures that the input is valid. It continues to prompt the user until they enter a valid answer.

`evaluate_quiz(questions, user_answers)` Function:
- This function takes the list of questions and the user's answers as arguments. It compares each user answer to the correct answer (stored in the question dictionary) and calculates the user's score.

`main()` Function:
- This is the main function that orchestrates the entire quiz application.
- It calls `load_questions()` to load the questions from the 'data.json' file.
- It iterates over each question, displaying it and collecting the user's answer using `display_question()` and `get_user_answer()`.
- It then calls `evaluate_quiz()` to calculate the user's score based on their answers.
- Finally, it displays the user's score out of the total number of questions.

`if __name__ == '__main__'`: Block:
- This block ensures that the `main()` function is executed when the script is run directly (as opposed to being imported as a module).

Overall, this code allows a user to take a quiz by interacting with the program through the console, providing answers to questions and receiving a score at the end. The questions and correct answers are read from a JSON file named 'data.json'.
