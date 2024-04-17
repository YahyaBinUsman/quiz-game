import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def take_quiz(self):
        score = 0
        for question, options, correct_option in self.questions:
            random.shuffle(options)  # Randomize the order of options
            # Map correct_option to the shuffled index
            correct_idx = options.index(correct_option) + 1
            print(question)
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")
            user_answer = input("Enter your answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                if int(user_answer) == correct_idx:
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")
            else:
                print("Invalid input! Please enter a valid option number.")
        print(f"Your score: {score}/{len(self.questions)}")

questions = [
    ("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
    ("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Lysosome"], "Mitochondria"),
    ("Who wrote 'Hamlet'?", ["William Shakespeare", "Charles Dickens", "Leo Tolstoy", "Jane Austen"], "William Shakespeare"),
    ("What is the chemical symbol for water?", ["H2O", "CO2", "O2", "NaCl"], "H2O"),
    ("Which country is known as the 'Land of the Rising Sun'?", ["China", "Japan", "India", "South Korea"], "Japan"),
    ("What is the currency of Japan?", ["Dollar", "Pound", "Yen", "Euro"], "Yen"),
    ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "Leonardo da Vinci"),
    ("What is the largest mammal?", ["Elephant", "Blue whale", "Giraffe", "Hippopotamus"], "Blue whale"),
    ("What is the tallest mountain in the world?", ["K2", "Mount Everest", "Kangchenjunga", "Makalu"], "Mount Everest"),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Cu"], "Au"),
    ("What is the longest river in the world?", ["Nile", "Amazon", "Yangtze", "Mississippi"], "Nile"),
    ("Who discovered penicillin?", ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Robert Koch"], "Alexander Fleming"),
    ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], "Canberra"),
    ("What is the chemical symbol for nitrogen?", ["N", "Ni", "Na", "Ne"], "N"),
    ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], "William Shakespeare")
]

quiz = Quiz(questions)
quiz.take_quiz()
