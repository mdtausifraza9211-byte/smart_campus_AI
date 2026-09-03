from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

campus_info = {
    "computer lab": "The computer lab is located in CST Block, Ground floor.",
    "library": "The library is located in the main academic building.",
    "canteen": "The canteen is near the boy hostel.",
    "principal office": "The Principal's office is located in the administration building.",
    "Aminstration office": "The administration office is located in the administration building.",
    "Registrar office":"The Registrar office is located in the administration building",
    "Finance office":"The Finance office is located in the administration building",
    "Examination Cell":"The Examination Cell is located in the administration building",
    "Basic Electrical lab":"The Basic Electrical lab is located in the CORE block,second floor ",
    "Physics lab":"The Physics lab is located behid central library,second floor",
    "Chemistry lab":"The chemistry lab is located in the CORE Block,Ground floor",
    "Engineering Drowing lab":"The Engineering Drawing lab is located in the CORE Block, second floor",
    "Analog and Digital Electronics lab":"The Analog and Digital Electronics lab is located in the CORE Block,first floor",
    "Computer Organization lab":"The Computer Organization lab is located in CORE Block,first floor",
    "General store":"The General store is located at Exit gate of Campus",
    "Seminar Hall":"The Seminar Hall is located in CST Block, First Floor",
    "Workshop":"Workshop is located in CORE Block, Ground Floor",
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
