from flask import Flask, render_template
import requests

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define a route to render the atheism page
@app.route('/atheism')
def atheism():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()["value"]
    return render_template('atheism.html', text=joke)

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)