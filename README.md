# AI Chatbot Management System

## Overview

The AI Chatbot Management System is a web-based application for creating and managing AI-powered chatbots with a modern chat interface. It integrates a Large Language Model (Google Gemini) for intelligent responses, along with a rule-based NLP fallback to ensure reliability and uninterrupted service.

This project demonstrates full-stack development concepts including backend APIs, AI integration, database logging, and frontend UI design using only free and open-source tools.

---

## Features

- Modern chat-based UI (dark theme, ChatGPT-style layout)
- Integration with Google Gemini for natural language responses
- Hybrid response system with rule-based NLP fallback (TF-IDF + cosine similarity)
- Secure handling of environment variables for API keys and database credentials
- MySQL database for logging chatbot conversations
- RESTful API built using Flask
- Cost-efficient, free-tier friendly architecture

---

## Tech Stack

### Backend
- Python
- Flask

### AI / NLP
- Google Gemini (Google Generative AI API)
- TF-IDF + Cosine Similarity (fallback NLP model)

### Frontend
- HTML
- CSS
- JavaScript

### Database
- MySQL

### Tools & Libraries
- google-generativeai
- scikit-learn
- mysql-connector-python
- python-dotenv

---

## Project Architecture

```
Frontend (HTML / CSS / JS)
        ↓
    Flask REST API
        ↓
 Google Gemini (Primary)
        ↓
 TF-IDF NLP (Fallback)
        ↓
 MySQL Database (Chat Logs)
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repository-url>
cd <project-folder>
```

### 2. Create and Activate Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=chatbot_db
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Create Database and Table

```
CREATE DATABASE chatbot_db;
USE chatbot_db;

CREATE TABLE chat_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_message TEXT NOT NULL,
    bot_reply TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 6. Run the Application

```
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## How It Works

1. User messages are sent from the frontend to the Flask backend.
2. The backend attempts to generate a response using Google Gemini.
3. If the LLM is unavailable or usage limits are exceeded, a TF-IDF-based NLP model is used as a fallback.
4. All conversations are logged into a MySQL database for monitoring and analysis.

---

## Future Enhancements

- User authentication and role-based access control
- Multilingual chatbot support
- Analytics dashboard for conversation insights
- Deployment using Docker and cloud platforms
- Integration with messaging platforms (WhatsApp, Slack, etc.)

---

##Author

By Murali Krishna M 
Developed for the sake of learning and understanding the working of API calls and working of basic chatbots

---

## License

This project is intended for educational purposes and is open-sourced for anyone who needs to implement and learn.

