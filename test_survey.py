import unittest
from .survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the `AnonymousSurvey` class"""
    def setUp(self):
        """
        Create a survey
        & a set of responses for use in
        ALL test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Marathi', 'Hindi']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_3_responses(self):
        """Test that 3 responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()