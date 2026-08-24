from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Resume Data
resume_data = {
    "name": "Lalit Kumar Mohanta",
    "title": "Software Developer",
    "email": "lalitmohantacse@gmail.com",
    "phone": "+91 7853015114",
    "address": "Joginuagan, Betnoti, Mayurbhanj, Odisha, India",
    "languages": ["Hindi", "English"],
    "interests": ["Full Stack Development", "Java (DSA)", "Machine Learning", "Generative AI", "Drone Technology"],
    "skills": ["C", "Python", "Java", "HTML", "CSS", "SQL"],
    "education": [
        {
            "degree": "B.Tech in Computer Science and Engineering",
            "institution": "NIST University, Berhampur, Odisha",
            "year": "2024 – 2028 | CGPA: 7.8"
        },
        {
            "degree": "Intermediate – Science (PCM)",
            "institution": "MPC Higher Secondary School, Baripada",
            "year": "2022 – 2024 | 74%"
        }
    ],
    "experience": [
        {
            "title": "Web Development Intern",
            "company": "Uptricks Services Pvt. Ltd., Pune",
            "year": "1 Month",
            "description": "Gained practical exposure to web development through hands-on tasks and real-world development practices. Worked on developing and improving web-based interfaces with a focus on structured and user-friendly design. Strengthened practical understanding of web development, problem-solving, and implementation through project-based learning."
        }
    ],
    "projects": [
        {
            "name": "CineVault — Movie Discovery & Management Platform",
            "tech": "HTML, CSS, JS",
            "description": "A modern web-based movie discovery platform allowing users to browse, search, and explore a wide range of movies through an interactive and categorized interface.",
            "image": "project_thumbnail_1_1778266223422.png",
            "url": "https://project-xbqg.onrender.com",
            "status": "live"
        },
        {
            "name": "Project 2",
            "tech": "Python, LLM, Flask",
            "description": "An intelligent resume screening system powered by large language models that automatically ranks candidates based on job descriptions and skill compatibility.",
            "image": "",
            "url": "#",
            "status": "coming_soon"
        },
        {
            "name": "Project 3",
            "tech": "Python, OpenCV, IoT",
            "description": "A real-time drone-based surveillance platform integrating computer vision for object detection, tracking, and alert generation in restricted zones.",
            "image": "",
            "url": "#",
            "status": "coming_soon"
        }
    ],
    "services": [
        {
            "name": "Full Stack Development",
            "description": "Building scalable, high-performance web applications using modern stacks like Python, Java, and frontend technologies.",
            "icon": "fas fa-code"
        },
        {
            "name": "AI Integration",
            "description": "Embedding LLMs, resume screening models, and intelligent agents to automate complex workflows.",
            "icon": "fas fa-brain"
        },
        {
            "name": "UI/UX Design",
            "description": "Crafting futuristic, user-centric interfaces with a focus on neon aesthetics and smooth interactions.",
            "icon": "fas fa-paint-brush"
        }
    ],
    "testimonials": [
        {
            "name": "Sarah Chen",
            "role": "CTO, TechNova",
            "quote": "Lalit's ability to blend complex logic with stunning aesthetics is truly futuristic. A rare talent in the modern development landscape."
        },
        {
            "name": "Mark Grayson",
            "role": "Lead Architect, Nexus Labs",
            "quote": "The Cyber Sentinel project Lalit built revolutionized our internal monitoring. His vision for AI integration is second to none."
        }
    ],
    "social_links": [
        {"name": "GitHub", "url": "https://github.com/lalitkumar24-28", "icon": "fab fa-github"},
        {"name": "LinkedIn", "url": "https://www.linkedin.com/in/lalit-kumar-mohanta-b94805333", "icon": "fab fa-linkedin"}
    ],
    "profile_image": "profile_gmail.png",
    "metrics": [
        {"label": "MISSIONS COMPLETED", "value": "12+", "icon": "fas fa-check-double"},
        {"label": "LINES OF CODE", "value": "45K+", "icon": "fas fa-terminal"},
        {"label": "SYSTEM UPTIME", "value": "99.9%", "icon": "fas fa-bolt"},
        {"label": "AI AGENTS", "value": "4", "icon": "fas fa-robot"}
    ]
}

@app.route("/")
def index():
    return render_template("index.html", data=resume_data)

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    data = request.json
    # Simulate saving to database or sending email
    name = data.get("name")
    print(f"DEBUG: Contact request received from {name}")
    return jsonify({"status": "success", "message": "Mission coordinates received. We will connect shortly."})

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    system_prompt = f"""
    You are an AI assistant for Lalit Kumar's portfolio website.
    Your goal is to answer questions about Lalit based on his resume data.
    
    Resume Data:
    {resume_data}
    
    Answer concisely and professionally. If the answer is not in the resume, say you don't know but suggest contacting Lalit at {resume_data['email']}.
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama-3.1-8b-instant",
        )
        response_message = chat_completion.choices[0].message.content
        return jsonify({"response": response_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(">>> SYSTEM INITIATED: Portfolio Dashboard starting on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
