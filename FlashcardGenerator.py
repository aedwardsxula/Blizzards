#Implement FlashcardGenerator Class
#Attributes: syllabus
#Method: generate(start_date, end_date)
#Output: list of flashcards for the study session
#Note: Flashcards should be generated only for topics between DATE1..DATE2 before the session.
class FlashcardGenerator:
    def __init__(self, syllabus):
        self.syllabus = syllabus  # syllabus is expected to be a list of topics with associated dates

    def generate(self, start_date, end_date):
        flashcards = []
        for topic in self.syllabus:
            topic_date = topic.get('date')
            if start_date <= topic_date <= end_date:
                flashcards.append(topic.get('flashcards', []))
        # Flatten the list of flashcards
        flat_flashcards = [card for sublist in flashcards for card in sublist]
        return flat_flashcards