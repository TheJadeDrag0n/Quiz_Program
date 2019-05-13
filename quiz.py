from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Questions:
    
    question_num = count(0)
    
    
    def __init__(self, image, question, choice_1, choice_2, choice_3, choice_4):
        
        self.id = next(self.question_num)
        self.cover = image
        self.question = question
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4        


#==[ Test Data ]==#

question_list = [
    
    Questions("logo.png", "test_question", "test_question_1", "test_question_2", "test_question_3", "test_question_4"),
    Questions("logo.png", "test_question", "test_question_1", "test_question_2", "test_question_3", "test_question_4"),
    Questions("logo.png", "test_question", "test_question_1", "test_question_2", "test_question_3", "test_question_4")
    
    ]




#===[ Pages ]===#

 #--[ Index ]--#

@route("/")
@view("index")
def index():
    
    pass


 #--[ Quiz ]--#
 
@route("/quiz")
@view("quiz")
def quiz():
    
    data = dict (questions=question_list)
    return data     


#===[ Images ]===#

@route('/pictures/<filename>')
def picture(filename):
    return static_file(filename, root='./images')


#Run Server
run(host='0.0.0.0',port = 8080, reloader=True, debug=True)