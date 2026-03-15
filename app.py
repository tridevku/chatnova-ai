from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    response = model.generate_content(user_message)

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)