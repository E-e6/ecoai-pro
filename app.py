from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_footprint(data):
    transport = int(data.get("transport", 0))
    food = int(data.get("food", 0))
    energy = int(data.get("energy", 0))

    score = transport * 2 + food * 1.5 + energy * 2.5

    return score

def smart_advice(score):
    if score > 50:
        return "High emissions detected. Reduce car usage, switch to renewable energy, and lower meat consumption."
    elif score > 20:
        return "Moderate impact. Try using public transport and reducing waste."
    else:
        return "Excellent sustainability habits! Keep it up."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    score = calculate_footprint(data)
    advice = smart_advice(score)
    prediction = score * 30

    return jsonify({
        "score": score,
        "prediction": prediction,
        "advice": advice
    })

if __name__ == "__main__":
    app.run(debug=True)
