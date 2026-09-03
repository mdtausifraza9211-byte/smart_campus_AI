from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

campus_info = {
    "computer lab": "The computer lab is located in CST Block, Ground floor.",
    "library": "The library is located in the main academic building.",
    "canteen": "The canteen is near the boy hostel.",
    "principal": "The Principal's office is located in the administration building.",
    "principal office": "The Principal's office is located in the administration building.",
    "administration office": "The administration office is located in the administration building.",
    "registrar office": "The Registrar office is located in the administration building.",
    "finance office": "The Finance office is located in the administration building.",
    "examination cell": "The Examination Cell is located in the administration building.",
    "basic electrical lab": "The Basic Electrical Lab is located in the CORE Block, second floor.",
    "physics lab": "The Physics Lab is located behind the central library, second floor.",
    "chemistry lab": "The Chemistry Lab is located in the CORE Block, Ground floor.",
    "engineering drawing lab": "The Engineering Drawing Lab is located in the CORE Block, second floor.",
    "analog and digital electronics lab": "The Analog and Digital Electronics Lab is located in the CORE Block, first floor.",
    "computer organization lab": "The Computer Organization Lab is located in the CORE Block, first floor.",
    "general store": "The General Store is located at the exit gate of the campus.",
    "seminar hall": "The Seminar Hall is located in CST Block, First Floor.",
    "workshop": "The Workshop is located in CORE Block, Ground Floor.",
    "ground": "The ground is located on the campus."
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
