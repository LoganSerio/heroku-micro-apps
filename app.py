from flask import Flask

app = Flask(__name__)

@app.route('/twittersearch')
def twittersearch():
    return """
        <form method="POST">
            First name:<br>
            <input type="text" name="firstname" value="test"><br>
            Last name:<br>
            <input type="text" name="lastname" value="test"><br><br>
            <input type="submit" value="Submit">
        </form>
    """

@app.route('/')
def index():
    return """
    <h1>Welcome to the home of my micro apps!</h1>
    <p>On this webpage I will be creating and linking to small python applications that I've made.</p>
    <a href="/twittersearch">Click here to go to test page</a>
    """
if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)