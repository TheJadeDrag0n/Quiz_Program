from bottle import run, route, view, get, post, request, static_file



#==[ Pages ]==#


#--[ index ]--#
@route("/")
@view("index")
def index():
    
    pass



run(host='0.0.0.0',port = 8080, reloader=True, debug=True)