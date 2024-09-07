Flashcard Quizzer is a simple Python application designed to help users study and memorize information using flashcards. The application allows users to create flashcards with questions and answers, and then quiz themselves on the flashcards. It provides a straightforward command-line interface for managing and using flashcards.

## Features

- Add new flashcards with questions and answers.
- Quiz yourself using the flashcards.

## Installation

1. **Clone the repository** (or download the script file):

    ```bash
    git clone 
    cd <your_folder>
    ```

2. **Run the script**:

    ```bash
    python flash_card_quiz.py
    ```

## Usage

Upon running the script, you'll be presented with a menu offering three options:

1. **Add Flashcard**: 
   - Input a question and its corresponding answer to create a new flashcard.
   
2. **Start Quiz**: 
   - Begin a quiz session where you will be prompted with questions from the flashcards you've added. Your answers will be checked, and you'll receive feedback on each response.

3. **Exit**: 
   - Exit the application.

### Example


```bash
Flashcard Quizzer
1. Add Flashcard
2. Start Quiz
3. Exit
Choose an option: 1
Enter the question: What is capital of India?
Enter the answer: New Delhi
Flashcard added!

Flashcard Quizzer
1. Add Flashcard
2. Start Quiz
3. Exit
Choose an option: 2
Q: What is capital of India? New Delhi
Correct!
Quiz finished! Your score: 1/1

Flashcard Quizzer
1. Add Flashcard
2. Start Quiz
3. Exit
Choose an option: 3
Goodbye!
```