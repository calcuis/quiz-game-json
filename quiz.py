import json

def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

def display_question(question):
    print(question['question'])
    print('a. ' + question['a'])
    print('b. ' + question['b'])
    print('c. ' + question['c'])
    print('d. ' + question['d'])

def get_user_answer():
    while True:
        user_answer = input('Your answer (a/b/c/d): ').lower()
        if user_answer in ['a', 'b', 'c', 'd']:
            return user_answer
        else:
            print('Invalid choice. Please choose a valid option (a, b, c, or d).')

def evaluate_quiz(questions, user_answers):
    score = 0
    for question, user_answer in zip(questions, user_answers):
        if user_answer == question['answer']:
            score += 1
    return score

def main():
    # Load questions from the JSON file
    questions = load_questions('data.json')

    # Display questions and get user answers
    user_answers = []
    for i, question in enumerate(questions, start=1):
        print(f'\nQuestion {i}:')
        display_question(question)
        user_answer = get_user_answer()
        user_answers.append(user_answer)

    # Evaluate the quiz and display the score
    score = evaluate_quiz(questions, user_answers)
    print(f'\nYour score: {score}/{len(questions)}')

if __name__ == '__main__':
    main()
