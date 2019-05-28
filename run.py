from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Questions:
    
    question_id = count(0)
    
    
    def __init__(self, question, state, choice_1, choice_2, choice_3, choice_4):
        
        self.id = next(self.question_id)
        self.question = question
        self.state = state
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4        


#==[ Test Data ]==#



test_list = [ #             / 0 = not anwsered   1 = correct   2 = incorrect
#                          |
    Questions("Who am i?", 0, "no one", "someone", "you", "..."),
    Questions("Who are you?", 0, "no one", "someone", "me", "..."),
    Questions("what is the to anwser to life?", 0, "42", "14 x 3", "6.48074^2", "378/9")
    ]



#======[ Pages ]======#

    #--[ Index ]--#

@route("/")
@view("index")
def index():
    
    pass



    #--[ Quiz ]--#
 
@route("/quiz")
@view("quiz")
def quiz():
       
    data = dict (test=test_list)
    return data



#=====[ Images ]======#

@route('/pictures/<filename>')
def picture(filename):
    return static_file(filename, root='./images')




#=====[ Run Server ]=====#
run(host='0.0.0.0',port = 8080, reloader=True, debug=True)