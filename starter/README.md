# Full Stack API Final Project

## Full Stack Trivia

 the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category.  show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 
# API Referance
## Gettig Started
Base url:At present this app can be run locally and is not hosted an a base URL . The backend
app is hosted at default , http://127.0.0.1:5000/ , which is set as a proxy in the frontend configuration
## Error Handling
Errors are returned as JSON objects in the following format:
<pre>{
	'success':false,
	'error':404,
	'message':'resource not found'
}</pre>
The API will return three errors types when request fail:
<ul>
<li>404: 'resource not found'</li>
<li>422: 'unprocessable'</li>
<li>405: 'method not allowed'</li>
</ul>
	
## Endpoints
## GET /categories
	Genrals:
		 returns a list of categories and total number of categories
	sample: curl http://127.0.0.1:5000/categories
	
<pre>	{
  "categories": {
    "1": "genral", 
    "2": "frontend", 
    "3": "backend"
  }, 
  "success": true, 
  "total_categories": 3, 
  "total_questions": 18
}</pre>
## GET /questions
	Genrals:
		 returns a list of questions , list of categories, total number of categories and  total number of questions
		 Result are pageinated in groups of 10 , include request arrgument to choess page number, starting from 1 
	sample: curl http://127.0.0.1:5000/questions
<pre>	
{
  "categories": {
    "1": "genral", 
    "2": "frontend", 
    "3": "backend"
  }, 
  "questions": [
    {
      "answer": "........", 
      "category": null, 
      "difficulty": null, 
      "id": 2, 
      "question": "what is ....."
    }, 
    {
      "answer": "......", 
      "category": "2", 
      "difficulty": 4, 
      "id": 3, 
      "question": "what is ......"
    }, 
    {
      "answer": ".........", 
      "category": "1", 
      "difficulty": 1, 
      "id": 4, 
      "question": "where is ...."
    }, 
    {
      "answer": ".......", 
      "category": "1", 
      "difficulty": 1, 
      "id": 5, 
      "question": "where is ....."
    }, 
    {
      "answer": ".........", 
      "category": "1", 
      "difficulty": 1, 
      "id": 6, 
      "question": "how are ......"
    }, 
    {
      "answer": ".......", 
      "category": "3", 
      "difficulty": 3, 
      "id": 8, 
      "question": "what is ........."
    }, 
    {
      "answer": ".........", 
      "category": "2", 
      "difficulty": 5, 
      "id": 9, 
      "question": "waht is .........."
    }, 
    {
      "answer": ".....", 
      "category": "2", 
      "difficulty": 4, 
      "id": 10, 
      "question": "how are ......."
    }, 
    {
      "answer": ".......", 
      "category": "2", 
      "difficulty": 4, 
      "id": 11, 
      "question": "what is ..........."
    }, 
    {
      "answer": "......", 
      "category": "3", 
      "difficulty": 3, 
      "id": 12, 
      "question": "what is ......."
    }
  ], 
  "success": true, 
  "total_categories": 3, 
  "total_questions": 19
}
</pre>
## POST /questions
	Genrals:
		* great a new question using a submitted quetion,answer,catogry and difficulty returns success value and total number of questions
        
	sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d   '{"quetion":"whate is postgres","answer":"database","catogry":"1","difficulty":1}'
	
	{
  "success": true, 
  "total_questions": 23
}
## DELETE /questions/(question_id)
	Genrals:
		* Deletes the book of given ID if it exists , Returns ID of deleted book , success value and  total number of questions
        
	sample: curl -X DELETE http://127.0.0.1:5000/questions/15
	
{
  "deleted": 15, 
  "success": true, 
  "total_questions": 17
}
## POST /questions/search
	Genrals:
		* search a questions using a submitted searchTerm returns success value and list of questions
        
	sample: curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d   '{"searchTerm":"what"}'
	{
  "questions": [
    {
      "answer": "python", 
      "category": "2", 
      "difficulty": 4, 
      "id": 11, 
      "question": "what is laguage the site"
    }, 
        {
      "answer": "nodejs", 
      "category": "3", 
      "difficulty": 3, 
      "id": 12, 
      "question": "what is frontend"
    }
      ], 
  "success": true
}

## GET /categories/(gategory_id)/questions
Genrals:
		* search a questions using category id returns success value, total number of questions, and list of questions
		* Result are pageinated in groups of 10 , include request arrgument to choess page number, starting from 1 
sample: curl http://127.0.0.1:5000/categories/3/questions
{
  "questions": [
    {
      "answer": "nodejs", 
      "category": "3", 
      "difficulty": 3, 
      "id": 12, 
      "question": "what is frontend"
    }, 
    {
      "answer": "yes", 
      "category": "3", 
      "difficulty": 3, 
      "id": 13, 
      "question": "are you want play"
    }, 
    {
      "answer": "yas", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "are you want "
    }
  ], 
  "success": true, 
  "total_questions": 17
}

## POST /quizzes
	Genrals:
		* start a game  using a submitted quiz_category and previous_questions returns success value and A new random question

	sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d   '{"quiz_category ":{"id":0},"previous_questions":[1,4,5,10]}'
{
  "question":    {
      "answer": "yes", 
      "category": "3", 
      "difficulty": 3, 
      "id": 13, 
      "question": "are you want play a game"
    } , 
  "success": true
}



