from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

campus_info = {
    "computer lab": "The computer lab is located in Block A, first floor.",
    "library": "The library is located in the main academic building.",
    "canteen": "The canteen is near the boy hostel.",
    "principal": "The Principal's office is located in the administration building.",
    "office": "The administration office is located in the main building."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"].lower()

    answer = "Sorry, I don't have information about that yet."

    for keyword, information in campus_info.items():
        if keyword in question:
            answer = information
            break

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)