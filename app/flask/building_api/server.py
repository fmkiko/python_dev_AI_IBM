from flask import Flask, request
from fake_data import data


app = Flask(__name__)


@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found", "data": data }
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

@app.route("/count")
def count():
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        # Replace {insert code to find length of data} with len(data) to get the length of the 'data' collection
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500


# Process input arguments -> localhost:5000/name_search?q=Abdel
@app.route('/name_search')
def find_person():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        422: If argument 'q' is missing
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')
    # Check if the query parameter 'q' is missing
    if not query:
        # Return a JSON response with a message indicating 'q' is missing and a 422 Unprocessable Entity status code
        return {"message": "Query parameter 'q' is missing"}, 422
    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person
    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code
    return {"message": "Person not found"}, 404
    
# Dynamic URLs
@app.route('/person_id/<id>')
def person(id):
    try:
        if data :
            # Iterate through the 'data' list to search for a person with a matching ID
            for person in data:
                # Check if the 'id' field of the person matches the 'var_name' parameter
                if person['id'] == str(id):
                    # Return the person as a JSON response if a match is found
                    return person
            # Return a JSON response with a message and a 404 Not Found status code if no matching person is found
            return {"message": "Person not found"}, 404
    except NameError:
        # Handle the case where 'data' is not defined
        return {"message": "Data not found"}, 404

# Validate the param <type:param_name>
@app.route('/person/<uuid:id>')
def person_uuid(id):
    try:
        if data:
            for person in data:
                if person["id"] == str(id):
                    return person
            return {"message": "Person not found"}, 404
    except NameError:
        return {"message": "Data not found"},

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_person(id):
    for person in data:
        if person["id"] == str(id):
            # Remove the person from the data list
            data.remove(person)
            # Return a JSON response with a message and HTTP status code 200 (OK)
            return {"message": "Person deleted successfully"}, 200
    # If the person is not found, return a JSON response with a message and HTTP status code 404 (Not Found
    return {"message": "Person not found"}, 404

# JSON from Request body
@app.route("/person", methods=['POST'])
def add_person():
    # Get the JSON data from the request body
    person = request.get_json()#request.json
    # Check if the person data is provided
    if person:
        # Append the new person data to the 'data' list
        data.append(person)
        # Return a JSON response with a message and HTTP status code 201 (Created)
        return {"message": "Person added successfully"}, 201
    # If the person data is not provided, return a JSON response with a message and HTTP status code 400 (Bad Request)
    return {"message": "Person data not provided"}, 400

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return {"message": "API not found"}, 404

