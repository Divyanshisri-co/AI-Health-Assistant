# AI-Health-Assistant
📌 About the Project

AI Health Assistant is a web-based application designed to help users with basic healthcare support using intelligent features.
The system provides two main functionalities:

💊 Medicine Scanner

Users can:

Upload an image of a medicine (future-ready for OCR)

OR manually enter the medicine name

The system processes the input and returns:

Medicine name

Uses

Precautions

🧘 Yoga Recommendation System

Users select a health issue such as:

Stress

Back Pain

Digestion

The system suggests:

Relevant yoga poses

Benefits of each pose

🛠️ Tech Stack (Detailed)
🔹 Frontend

HTML5

Structure of the web pages

Tailwind CSS

Utility-first CSS framework for fast UI design

Used for responsive layout, gradients, cards, buttons

JavaScript

Handles user interaction

Used for:

Dynamic UI switching (Medicine / Yoga)

Form submission using Fetch API

Validation (input checking)

🔹 Backend

Python (Flask)

Lightweight web framework

Handles routing and server logic

Processes form data from frontend

🔹 Data Handling

JSON (medicine.json)

Stores medicine-related information

Used for quick lookup of:

Name

Use

Precaution

🔹 API / AI Integration (Extendable)

Designed to support:

OpenFDA API (medicine data)

OCR tools (like Tesseract / EasyOCR)

LLM APIs (like Groq / OpenAI) for summarization

🔹 File Handling

FormData (JavaScript)

Used to send image + text data to backend

⚙️ Project Workflow (Very Important)
💊 Medicine Flow
User Input (Image / Text)
        ↓
Frontend (JS + FormData)
        ↓
Flask Backend (/medicine route)
        ↓
Process Input
   → If text → search JSON
   → If image → (future OCR)
        ↓
Fetch Data
        ↓
Render Result Page
🧘 Yoga Flow
User selects problem
        ↓
Form submit (/yoga)
        ↓
Flask processes input
        ↓
Fetch yoga data
        ↓
Render yoga_result.html
🎨 UI/UX Features

Responsive design (Mobile + Desktop)

Gradient backgrounds

Card-based layout

Interactive UI (clickable options)

Dynamic content rendering

Clean and minimal design

🎯 Key Highlights

Combines web development + AI-ready architecture

Supports image + text input handling

Designed for scalability (API + ML integration)

Beginner-friendly but extendable to advanced AI system

🚀 Future Enhancements

📊 User history tracking

🧠 Personalized health suggestions

author : Divyanshisri-co
