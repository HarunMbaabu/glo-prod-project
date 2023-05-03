import pandas as pd 
from flask import Flask, request 

data = pd.read_csv("data/clean-houses-for-rent.csv")

app = Flask(__name__) 

# Define a function to search for apartments within a certain budget and city
def search_apartments(budget, city):
    available_apartments = data[(data['price'] <= budget) & (data['location'] == city)]
    return available_apartments


# Define a function to format the apartment information as a string
def format_apartment(apartment):
    title = apartment['title']
    location = apartment['location']
    size = apartment['size']
    price = apartment['price']
    return f"{title}\nlocation: {location}\nsize: {size} sq ft\nprice: ${price} per month" 


# Define a Flask route to handle user input and generate responses
@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        city = request.form['city']
        budget = float(request.form['budget'])

        available_apartments = search_apartments(budget, city)
        if available_apartments.empty:
            response = "Sorry, we couldn't find any apartments within your budget."
        else:
            response = "Here are some apartments that fit your budget:<br>"
            for index, apartment in available_apartments.iterrows():
                response += format_apartment(apartment) + "<br>"
        return response
    else:
        return '''
            <form method="post">
                <label for="city">What city are you looking in?</label>
                <input type="text" id="city" name="city"><br>
                <label for="budget">What is your budget per month?</label>
                <input type="text" id="budget" name="budget"><br>
                <input type="submit" value="Submit">
            </form>
        '''  

if __name__ == '__main__':
    app.run(debug=True)




