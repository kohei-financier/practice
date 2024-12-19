import unittest
from survey import AnnoymousSurvey

class TestAnnoymousSurvey(unittest.TestCase):
    # AnnoymousSurveyクラスのテスト

    def setUp(self):
        question = "最初に勉強した言語は何ですか？"
        self.my_survey = AnnoymousSurvey(question)
        self.responses = ['英語', 'スペイン語', '中国語']

    def test_store_single_response(self):
        # 1件の回答が正しく保存されているかをテストする
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_thress_response(self):
        # 3件の回答が正しく保存されているかをテストする
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()