"""Module to create a simple survey."""

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question: str):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the question"""
        print(self.question)

    def store_response(self, response):
        """Store a response to the survey"""
        self.responses.append(response)

    def show_results(self):
        """Show all the responses that have been given"""
        print("The survey results: ")
        for response in self.responses:
            print(f"- {response}")