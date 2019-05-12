from bottle import run, route, view, get, post, request, static_file



#==[ Pages ]==#


#--[ Index ]--#

@route("/")
@view("index")
def index():
    
    pass


#--[ Quiz ]--#
@route("/quiz")
@view("quiz")
def quiz():
    
    pass



#==[ Images ]==#
@route('/pictures/<filename>')
def picture(filename):
    return static_file(filename, root='./images')



run(host='0.0.0.0',port = 8080, reloader=True, debug=True)