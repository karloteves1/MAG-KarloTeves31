from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(gunicorn)

# Define the main route to handle GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():

    # Initialize a variable to store the calculated woman's age
    result_age = None
    
    if request.method == 'POST':
        try:
            # Get the man's age from the form
            age = int(request.form['age'])
            # Calculate the woman's age using the provided formula
            result_age = age / 2 + 7
        except ValueError:
            # Handle invalid input (non-integer input)
            result_age = ""
            
    # Render the index.html template and pass the calculated age to it
    return render_template("index.html", result=result_age)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
