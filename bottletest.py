from bottle import route, template, static_file
from bottle import post, request # or route
#!/usr/bin/python
from bottle import Bottle, get, run, ServerAdapter

# copied from bottle. Only changes are to import ssl and wrap the socket
class SSLWSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        import ssl
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        srv = make_server(self.host, self.port, handler, **self.options)
        srv.socket = ssl.wrap_socket (
         srv.socket,
         certfile='server.pem',  # path to certificate
         server_side=True)
        srv.serve_forever()

@get("/x")
def get_x():
 return "Hi there"

#instead of:
#run(host="0.0.0.0", port=8090)
#we use:


import sanitize
from bow_classifier import score

responses = []
grades = []
f = open('responses.txt')
for line in f:
    s = line.split(':')
    grades.append(int(s[0]))
    responses.append(s[1])
f.close()

bags = [sanitize.bag_of_words(response) for response in responses]

def ansChecker(trial):
	trial_bag = sanitize.bag_of_words(trial)
	scores = []
	for i in range(len(bags)):
		scores.append(score(bags[i], trial_bag))
	sorter = sorted(range(len(scores)), key = lambda k: scores[k])
	sorter = sorter[::-1]
	bestGuess = []
	bestGuess.append(responses[sorter[0]])
	bestGuess.append(responses[sorter[1]])
	bestGuess.append(responses[sorter[2]])
	bestGuessScores = []
	bestGuessScores.append(grades[sorter[0]])
	bestGuessScores.append(grades[sorter[1]])
	bestGuessScores.append(grades[sorter[2]])
	return (bestGuess, 	bestGuessScores)



@get('/') # or @route('/login')
def login():
    return '''
	<p>What is Entropy?</p>
    <form action="/" method="post">
        Answer: <input name="ans" type="text" />
        <input value="Check" type="submit" />
    </form>
    '''
@get('/jschannel1.js') # or @route('/login')
def jsgetter():
	return static_file("jschannel1.js",root='.')

@post('/') # or @route('/login', method='POST')
def do_login():
    ans = request.forms.get('ans')
    responses, scores=ansChecker(ans)
    return template('radio', ans=responses, scores=scores)

srv = SSLWSGIRefServer(host="0.0.0.0", port=8090)
run(server=srv)
