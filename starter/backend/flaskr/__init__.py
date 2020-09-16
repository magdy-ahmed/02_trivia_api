import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate(page,selection):
  
  start =  (page - 1) * QUESTIONS_PER_PAGE 
  end = start + QUESTIONS_PER_PAGE
  Questions = [Question.format() for Question in selection]
  current_Questions = Questions[start:end]
  return current_Questions
def format_category(selection):
  catgories = [category.format() for category in selection]

  return catgories


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  #CORS(app)
  CORS(app,resources={r"*":{"origins":"*"}})
  app.config["CORS_HEADERS"]="Content-Type"
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
    response.headers.add('Access-Control-Allow-Credentials','true')
    return response
  @app.route('/categories')
  def get_all_categories():
    categories = Category.query.all()
    categories = format_category(categories)
    id_category=[]
    type_category=[]
    for row in categories:
      id_category.append(row['id'])
      type_category.append(row['type'])    
    all_categories = dict(zip(id_category, type_category))
    return jsonify({
      'categories':all_categories,
      'total_categories':len(all_categories),      
      'success':True,
      'total_questions':len(Question.query.all())
    })
  @app.route('/questions')
  def get_all_questions():
    questions = Question.query.order_by(Question.id).all()
    categories = Category.query.all()
    page = request.args.get('page',1,type=int)
    questions = paginate(page,questions)
    if len(questions) == 0:
      abort(404) 
    categories = format_category(categories)
    id_category=[]
    type_category=[]
    for row in categories:
      id_category.append(row['id'])
      type_category.append(row['type'])    
    all_categories = dict(zip(id_category, type_category))
    return jsonify({
      'questions':questions,
      'categories':all_categories,
      'total_categories':len(all_categories),
      'success':True,
      'total_questions':len(Question.query.all())
    })
  @app.route('/questions/<int:id_question>',methods=['DELETE'])
  def delete_question(id_question):
    question = Question.query.filter(Question.id == id_question).one_or_none()
    if question is None:
      abort(404)
    try:
      question.delete()
    except:
      abort(422)
    return jsonify({
      'success':True,
      'total_questions':len(Question.query.all()),
      'deleted':id_question
      
    })
  @app.route('/questions',methods=['POST'])
  def add_new_question():
    body = request.get_json()
    question = body.get('question','')
    answer = body.get('answer','')
    category = body.get('category','0')
    difficulty = body.get('difficulty',0)
    questions = Question.query.order_by(Question.id).all()
    try:
      question = Question(question=question,answer=answer,category=category,difficulty=difficulty)
      question.insert()
    except:
      abort(404)
    page = request.args.get('page',1,type=int)
    questions = paginate(page,questions)
    return jsonify({
      'success':True,
      'total_questions':len(Question.query.all())
    })
  @app.route('/questions/search',methods=['POST'])
  def search_question():
    body = request.get_json()
    searchTerm = body.get('searchTerm',None)
    questions = Question.query.filter(Question.question.ilike('%{}%'.format(searchTerm))).all() 
    page = request.args.get('page',1,type=int)
    questions = paginate(page,questions)

    return jsonify({
      'success':True,
      'questions':questions
    })
    

  @app.route('/categories/<int:id_category>/questions',methods=['GET'])
  def get_question_by_category(id_category):
    questions = Question.query.filter(Question.category == str(id_category)).all()
    page = request.args.get('page',1,type=int)
    questions = paginate(page,questions)
    if len(questions)==0:
      abort(404)
    return jsonify({
      'questions':questions,
      'success':True,
      'total_questions':len(Question.query.all())
    })
  @app.route('/quizzes',methods=['POST'])
  def get_quizzes():
    body = request.get_json()
    id_category = body.get('quiz_category',{'id':0})
    previousQuestions=body.get('previous_questions',[])
    previousQuestions=previousQuestions+[0,0,0,0]
    questions = Question.query
    if id_category['id'] == 0:
      for previousQuestion in previousQuestions:
        questions = questions.filter(Question.id != int(previousQuestion))
    else:
      questions = Question.query.filter(Question.category == id_category['id'])
      for previousQuestion in previousQuestions:
        questions = questions.filter(Question.id != int(previousQuestion))
    questions = paginate(1,questions) 
    question = random.choice(questions)
    return jsonify({
        'success':True,
        'question': question,

    })

  @app.errorhandler(404)
  def not_fond(error):
    return jsonify({
      "success" : False,
      "error" : 404,
      "message": "resource not found"
    }),404
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success" : False,
      "error" : 422,
      "message": "unprocessable"
    }),422
  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      "success" : False,
      "error" : 405,
      "message": "method not allowed"
    }), 405  
    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    
