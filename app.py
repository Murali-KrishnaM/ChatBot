from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from gemini_bot import gemini_response
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        bot_reply = gemini_response(user_message)
        #print("✅ Gemini used")
    except Exception as e:
        #print("❌ Gemini failed:", e)
        bot_reply = get_response(user_message)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_logs (user_message, bot_reply) VALUES (%s, %s)",
        (user_message, bot_reply)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"reply": bot_reply})



@app.route("/logs")
def logs():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM chat_logs ORDER BY created_at DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
