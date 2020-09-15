# Full Stack API Final Project

## Full Stack Trivia

 the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category.  show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 
## nots
1)Categories must be entered before starting to use

## Use Curl
1) /categories
Displays all categories and questions
2) /questions
It displays all the questions and you can pass the page number
3) /questions/<int:id> method['DELETE']<br>
It removes the question in terms of id<br>
4) /questions mehtods['POST'] json={<br>
'id' : <int:new_id> ,<br>
'question' : <str:new_question> ,<br>
'answer' : <str:new_answer> ,<br>
'difficulty': <int:new_difficulty> ,<br>
'category' :<str:new_category><br>
}<br>
it adds a new question using Jason<br>
5) /categories/<id:category>/questions<br>
Searches for questions using the category or the query word search<br>
if id_category==0 it will return all questions
6)/quezzes
The game begins by returning five questions





