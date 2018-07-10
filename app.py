from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return """
        <h1>The test worked</h1>
    """

@app.route('/')
def index():
    return """
    <h1>Welcome to the home of my micro apps!</h1>
    <p>On this webpage I will be creating and linking to small python applications that I've made.</p>
    <a href="/test">Click here to go to test page</a>
    """
if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)