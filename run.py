from bottle import run, route, view, get, post, request, static_file 
from itertools import count



class Questions:
    
    question_id = count(0)
    
    
    def __init__(self, choice_1, choice_2, choice_3, choice_4, name, correct, answer): # 
        
        self.id = next(self.question_id)
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4      
        self.name = name
        self.correct = correct
        self.answer = answer



#==[ Test Data ]==#
test_list = [# the test is layed out a : Choice 1 - 4, Question, Correct, Answer 
                  #                                                      \__ a value of 0 means it's wrong or unanswered and 1 is correct. 0 is default
    Questions("System Software", "Application Software", "Utility Software", "Malware", "The Operating System is a :", 0, "System Software"), 
    Questions("RAM", "Cache", "Directories", "None of the above", "Files are Organized in :", 0, "Directories"), 
    Questions("Fetching", "Controlling", "Storing", "Executing", "The process of carrying out a command is called :", 0, "Executing"),
    Questions("Rewrite","Read","Readable","Random","What does the R in RAM stands for?", 0, "Random")
    ]


#======[ Pages ]======#

#--[ Index ]--#

@route("/")
@view("index")
def index():   # will only have a link to the quiz page saying "Start the Quiz"
    
    pass



    #--[ Quiz ]--#
 
@route("/quiz")
@view("quiz")
def quiz(): # 
    
    
    data = dict (website_questions=test_list)  
    return data # returns the data to be able to show the questions and choices on the HTML page



@route("/quiz_completed", method="POST")
@view("quiz_completed")
def quiz_completed(): # will display the correct answers and number cf correct answers from the user
    

    for Questions in test_list:

        user_choice = request.forms.get(Questions.id)  # grabs the input form quiz.html for question 1,2,3, etc
        
        if user_choice == Questions.answer: # checks if user's choice is equal to the answer
            
            Questions.correct = 1    # if the user's choice correct, it adds one to the score    

    data = dict (website_answers = test_list)
    return data



#=====[ Images ]======#

@route('/pictures/<filename>') # able to use images of the website
def picture(filename):
    return static_file(filename, root='./images')




#=====[ Run Server ]=====#     # take a wild guess what this does 
run(host='0.0.0.0',port = 8080, reloader=True, debug=True)