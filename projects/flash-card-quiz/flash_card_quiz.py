import random
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardQuizzer:
    def __init__(self):
        self.flashcards = []
        self.score = 0

    def add_flashcard(self, question, answer):
        self.flashcards.append(Flashcard(question, answer))

    def quiz(self):
        if not self.flashcards:
            print("No flashcards available.")
            return

        random.shuffle(self.flashcards)
        self.score = 0

        for flashcard in self.flashcards:
            user_answer = input(f"Q: {flashcard.question} ")
            if user_answer.strip().lower() == flashcard.answer.strip().lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {flashcard.answer}")

        print(f"Quiz finished! Your score: {self.score}/{len(self.flashcards)}")


def main():
    quizzer = FlashcardQuizzer()

    while True:
        print("\nFlashcard Quizzer")
        print("1. Add Flashcard")
        print("2. Start Quiz")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            quizzer.add_flashcard(question, answer)
            print("Flashcard added!")
        elif choice == '2':
            quizzer.quiz()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
