from flask import Flask, render_template, request, jsonify
# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    result = summation(num1, num2)
    return { "data": result }

@app.route("/sub")
def sub_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subtraction(num1, num2)
        return jsonify(data=result)
    except Exception as e:
        return {"error":str(e)}
    

@app.route("/mul", methods=["POST"])
def mul_route():
    data = request.get_json()
    if data and 'num1' in data and 'num2' in data:
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
            result = multiplication(num1, num2)
            return jsonify(data=result)
        except ValueError:
            return jsonify(error="Invalid input. num1 and num2 must be numbers."), 400
    else:
        return jsonify(error="Missing required parameters 'num1' or 'num2'"), 400

@app.route("/")
def render_index_page():
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)