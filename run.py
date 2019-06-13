from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Questions:
    
    question_id = count(0)
    
    
    def __init__(self, choice_1, choice_2, choice_3, choice_4, name):
        
        self.id = next(self.question_id)
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4      
        self.name = name



#==[ Test Data ]==#
test_list = [ 

    Questions("no one", "someone", "you", "...", "Question 1"), 
    Questions("1", "2", "4", "8", "Question 2"), 
    Questions("42", "14 x 3", "6.48074^2", "378/9", "Question 3")
    ]


answers = [
    
    "no one",
    "1",
    "42"
    
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
    
    
    data = dict (website_questions=test_list)
    return data



@route("/quiz_completed", method="POST")
@view("quiz_completed")
def quiz_completed():
    
    
    correct = 0    
    wrong = 0
    
    
    user_choice1 = request.forms.get(0)
    user_choice2 = request.forms.get(1)
    user_choice3 = request.forms.get(2)
    user_choice4 = request.forms.get(3)



    data = dict (website_answers = answers)
    return data
        
      
    


#=====[ Images ]======#

@route('/pictures/<filename>')
def picture(filename):
    return static_file(filename, root='./images')




#=====[ Run Server ]=====#
run(host='0.0.0.0',port = 8080, reloader=True, debug=True)