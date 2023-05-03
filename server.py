import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# Read the JSON file into a Pandas dataframe
data = pd.read_json('data/clean-houses-for-rent.csv')

# Define a route to display the search form
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle the search form submission
@app.route('/search', methods=['POST'])
def search():
    # Get the form inputs for location, size, and price
    location = request.form['location']
    size = request.form['size']
    price = request.form['price']

    # Filter the dataframe based on the input values
    filtered_data = data[(data['location'] == location) & (data['size'] == size) & (data['price'] == price)]

    # Get the titles of the matching records
    titles = filtered_data['title'].tolist()

    # Render the search results template with the titles
    return render_template('search_results.html', titles=titles)

if __name__ == '__main__':
    app.run(debug=True)
