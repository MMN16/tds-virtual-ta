from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "TDS Virtual TA API is running. Use the /api/ endpoint with POST method."}

@app.route("/api/", methods=["POST"])
def answer_question():
    try:
        data = request.get_json(force=True)
        question = data.get("question", "")

        # Dummy answer logic for now
        if "GA5" in question.upper():
            answer = "You must use `gpt-3.5-turbo-0125` as instructed in GA5."
            links = [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                    "text": "Use the model that’s mentioned in the question."
                },
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                    "text": "Use a tokenizer to calculate number of tokens and multiply by rate."
                }
            ]
        else:
            answer = "I'm not sure. Please check the Discourse forum or ask a TA."
            links = []

        return jsonify({
            "answer": answer,
            "links": links
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)