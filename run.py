from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Questions:
    
    question_id = count(0)
    
    
    def __init__(self, choice_1, choice_2, choice_3, choice_4, name, correct):
        
        self.id = next(self.question_id)
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4      
        self.name = name
        self.correct = correct
        self.answer = answer



#==[ Test Data ]==#
test_list = [     # the test is layed out a : Choice 1 - 4, Question, Correct, Answer 
                  #                                                      \__ a value of 0 means it's wrong and 1 is correct. 0 is default
    Questions("no one", "someone", "you", "...", "Question 1", 0, "no one"), 
    Questions("1", "2", "4", "8", "Question 2", 0, "1"), 
    Questions("42", "14 x 3", "6.48074^2", "378/9", "Question 3", 0, "42")
    ]



#======[ Pages ]======#




@route("/test")
@view("test")
def test():
    
    pass


    #--[ Index ]--#

@route("/")
@view("index")
def index():
    
    pass



    #--[ Quiz ]--#
 
@route("/quiz")
@view("quiz")
def quiz():
    
    
    data = dict (website_questions=test_list)  # send the question list to quiz.html
    return data



@route("/quiz_completed", method="POST")
@view("quiz_completed")
def quiz_completed():
    
    
    
    
    user_choice1 = request.forms.get(0)  # grabs the input form quiz.html for question 1,2,3, etc
    user_choice2 = request.forms.get(1)
    user_choice3 = request.forms.get(2)

    for answer in Questions:
        
        if user_choice1 == Questions.choice_1: # checks if user's choice is equal to the answer
            
            Question.correct = 1        

    data = dict (website_answers = test_list)
    return data
        
      
    


#=====[ Images ]======#

@route('/pictures/<filename>') # able to use images of the website
def picture(filename):
    return static_file(filename, root='./images')




#=====[ Run Server ]=====#     # take a wild guess what this does 
run(host='0.0.0.0',port = 8080, reloader=True, debug=True)