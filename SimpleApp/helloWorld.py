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


# Define a route for the movie search page
@app.route('/movie', methods=['GET', 'POST'])
def movie():
    OMDB_API_KEY = 'xxxxxxx'
    movie_data = None  # Initialize the variable to store movie details
    error_message = None

    if request.method == 'POST':
        movie_title = request.form.get('title', '').strip()

        if not movie_title:
            error_message = "Please enter a movie title."
        else:
            # Call the OMDB API
            url = f'https://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={movie_title}'
            response = requests.get(url)
            data = response.json()

            if data.get('Response') == 'True':
                movie_data = data
            else:
                error_message = "Movie not found. Please try again."

    return render_template('movie.html', movie_data=movie_data, error_message=error_message)


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
