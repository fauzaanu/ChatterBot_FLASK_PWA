

# make a flask app that processes a get requests and replaces the template
# with the response from the chatbot
#
# make a flask app that processes a post request and trains the chatbot
# with the data from the post request
#

# make a flask app that processes a get requests and replaces the template
# with the response from the chatbot
#

from flask import Flask, render_template, request
from chatter import asksage
from controller import main, pwa

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET'])
def chat():
    if request.method == 'GET':
        # process the values from get request
        # get the question from the get request

        question = request.args.get('question')
        print(question)

        # get the answer from the chatbot

        answer = asksage(question)

        # render the template with the answer

        return render_template('chat_template.html', question=str(question), answer=str(answer))


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':

    app.register_blueprint(main.bp)
    app.register_blueprint(pwa.bp)
    

    app.run(debug=True)

