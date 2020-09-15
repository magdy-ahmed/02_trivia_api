import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "demo"#trivia_test
        self.database_path = "postgresql://postgres:987654@localhost:5432/demo"
        #"postgresql://{}/{}".format('postgres','987654','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question={
        'quetion':"whate is postgres",
        'answer':"database",
        'catogry':1,
        'difficulty':1
        } 

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        
    def tearDown(self):
        """Executed after reach test"""
        pass
    def test_get_all_categories(self):
        """Test _____________ """
        res = self.client().get('/categories')
        data=json.loads(res.data)        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))
    def test_search_questions_by_category(self):
        """Test _____________ """
        res = self.client().get('/categories/1/questions')
        data=json.loads(res.data)        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
    def test_404_search_questions_by_category(self): 
        res = self.client().get('/categories/1000000/questions') 
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")
    def test_get_all_questions(self):
        """Test _____________ """
        res = self.client().get('/questions?page=1')
        data=json.loads(res.data)        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
    def test_questions_404_bage_not_found(self): 
        res = self.client().get('/questions?page=100000') 
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")
    
    def test_404_delete_question(self):    
        res = self.client().delete('/questions/100000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")  
    def test_add_new_question(self): 
        res = self.client().post('/questions',json=self.new_question)
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
    def test_405_id_question_not_allowed(self): 
        res = self.client().post('/questions/1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)   
        self.assertEqual(data['message'], "method not allowed")  
    def test_quezze_by_category(self): 
        res = self.client().post('/quizzes',json={'id':'1'})
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question']) 
    def test_405_quezze_ctegory_not_found(self): 
        res = self.client().get('/quizzes' ,json={'id':'10000'}) 
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "method not allowed")
    def test_404_delete_question(self):       
        res = self.client().delete('/questions/100000')
        data=json.loads(res.data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found")

        """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()