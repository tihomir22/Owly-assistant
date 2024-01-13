import g4f
from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route("/",methods=['GET'])
def version():
    return '1.0.0'

@app.route('/generate', methods=['POST'])
def generate():
    # Extract the prompt from the request body
    data = request.json
    prompt = data.get('prompt')

    # Generate the response using the model
    response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    response = response.replace("\n", "<br>")

    # Return the model's response
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)