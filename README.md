# 🧠 AI Health Assistant

A web-based **AI-powered health assistant** that helps users identify medicines and get yoga recommendations based on health conditions.
 https://ai-health-assistant-ijrp.onrender.com
---

## 📌 Project Overview

AI Health Assistant is designed to provide **basic healthcare support** through an interactive and user-friendly interface.

The application includes:

* 💊 Medicine Scanner (text-based input)
* 🧘 Yoga Recommendation System

It is built using **Flask (backend)** and **Tailwind CSS (frontend)**, and is designed to be **scalable with AI and API integrations**.

---

## 🚀 Features

### 💊 Medicine Scanner

* Users can enter a medicine name
* Displays:

  * Medicine Name
  * Uses
  * Precautions
* Data is fetched from a structured JSON dataset

---

### 🧘 Yoga Suggestion

* Users select a health issue:

  * Stress
  * Back Pain
  * Digestion
* Displays:

  * Yoga poses
  * Benefits of each pose

---

## 🛠️ Tech Stack

### 🔹 Frontend

* **HTML5** – Structure of web pages
* **Tailwind CSS** – Responsive UI design and styling
* **JavaScript** – Dynamic interaction, form handling, Fetch API

---

### 🔹 Backend

* **Python (Flask)** – Web framework for routing and logic

---

### 🔹 Data Handling

* **JSON Files**

  * `medicine.json` – Stores medicine details
  * `yoga.json` – Stores yoga recommendations

---

### 🔹 Deployment

* Hosted on **Render**
* Uses:

  * `gunicorn` as WSGI server
  * `requirements.txt` for dependencies

---

## ⚙️ How It Works

### 💊 Medicine Flow

1. User enters medicine name
2. Frontend sends request using Fetch API
3. Flask backend processes input
4. Searches data from JSON
5. Displays structured result

---

### 🧘 Yoga Flow

1. User selects a problem
2. Form is submitted
3. Flask retrieves relevant yoga data
4. Results displayed with images and benefits

---

## 📂 Project Structure

```
AI-Health-Assistant/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── data/
│   ├── medicine.json
│   └── yoga.json
│
├── templates/
│   ├── index.html
│   ├── medicine_result.html
│   └── yoga_result.html
│
├── static/
│   ├── images/
│   └── css/
│
└── README.md
```

---

## ▶️ How to Run Locally

1. Clone repository:

```bash
git clone https://github.com/your-username/AI-Health-Assistant.git
```

2. Navigate to project:

```bash
cd AI-Health-Assistant
```

3. Install dependencies:

```bash
pip install flask
```

4. Run application:

```bash
python app.py
```

5. Open browser:

```
http://127.0.0.1:5000/
```

---

## 🌐 Live Demo

👉 Add your deployed link here

```
https://your-app.onrender.com
```

---

## 🎯 Key Highlights

* Responsive UI (Mobile + Desktop)
* Clean and modern design using Tailwind CSS
* Structured backend using Flask
* Real-world healthcare use case
* Scalable for AI and API integration

---

## 🚀 Future Improvements

* 🔍 OCR integration for medicine detection
* 🤖 AI-based medicine analysis
* 🌐 Integration with medical APIs
* 📊 User history tracking
* 🎨 Advanced UI enhancements

---

## 👩‍💻 Author

* Divyanshi

---


