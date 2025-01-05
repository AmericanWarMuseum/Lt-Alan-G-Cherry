
# 🎖️ Lieutenant Alan G. Cherry Interactive Chatbot
Welcome to the **Lt. Alan G. Cherry Interactive Chatbot**, a project dedicated to bringing historical figures to life through AI-driven conversations. This chatbot is based on the life and experiences of **Lieutenant Alan G. Cherry**, an officer in the **301st Engineer Regiment** during **World War I**.

This project leverages **Flask**, **OpenAI’s GPT API**, and **GitHub** to create a unique, immersive experience for users to interact with Lt. Cherry as if they were speaking to him in person, straight from the year **1919**.

---

## 📚 Project Overview
The chatbot is designed to:
- **Educate users** about World War I through Lt. Cherry’s personal experiences.
- Provide **accurate historical insights** from a soldier’s perspective.
- **Engage users in interactive storytelling**, making history come alive.

Lt. Cherry’s profile is built using a structured **JSON dataset** containing questions and answers related to his life, military service, and historical events.

---

## ⚙️ Technologies Used
- **Python** (Flask Framework)
- **HTML, CSS, JavaScript** (Frontend)
- **OpenAI GPT API** (for conversational AI)
- **GitHub** (for version control)
- **Render** or **Heroku** (for app deployment)

---

## 📂 Project Structure
```bash
.
├── data
│   └── lt_cherry.json  # JSON file with Lt. Cherry's profile
├── static
│   └── lt_cherry.jpg   # Lt. Cherry's photo
├── templates
│   └── index.html      # Frontend chat interface
├── server.py           # Flask server
└── README.md           # Project documentation
```

---

## 🚀 How to Use the Chatbot
1. **Visit the website** where the chatbot is hosted.
2. **Type your questions** in the chatbox (e.g., “Where did you serve during the war?”).
3. **Receive answers** from Lt. Cherry in real-time.

---

## 📄 JSON Dataset
The **`lt_cherry.json` file** contains structured questions and answers for the chatbot. You can easily add more questions to expand Lt. Cherry’s knowledge base.

Example:
```json
{
  "questions": [
    {
      "question": "Where were you born?",
      "answer": "I was born in Worcester, Massachusetts, in 1891."
    },
    {
      "question": "What was your rank in the army?",
      "answer": "I was commissioned as a second lieutenant and later promoted to first lieutenant."
    }
  ]
}
```

---

## 🌐 Deployment Instructions
### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lt-cherry-profile.git
   ```
2. Navigate to the project directory:
   ```bash
   cd lt-cherry-profile
   ```
3. Run the Flask server:
   ```bash
   python server.py
   ```

### Online Deployment
For online deployment, you can use **Render** or **Heroku** to host your Flask app. Make sure to link the GitHub repository to your preferred cloud service.

---

## 🤝 Contributions
We welcome contributions to enhance Lt. Cherry’s profile and improve the chatbot’s functionality. Please submit a **pull request** with your proposed changes.

---

## 📧 Contact
For questions or support, please contact:
- **Eric Hutchison**  
- **Email:** [americanwarmuseum@gmail.com](mailto:americanwarmuseum@gmail.com)  
- **Website:** [www.americanwarmuseum.ai](http://www.americanwarmuseum.ai)  

---

## 🏛️ License
This project is open-source and available under the **MIT License**.
