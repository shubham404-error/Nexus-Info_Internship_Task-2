from flask import Flask, render_template, request, session
from flask_session import Session
import json

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

knowledge_base = {
    "What are the admission requirements?": "The admission requirements include having a high school diploma, providing recommendation letters, and demonstrating involvement in extracurricular activities.",
    
    "How can I apply for admission?": "To apply for admission, you need to submit an online application through our official website. Make sure to provide accurate information and complete all required sections.",
    
    "What is the application deadline?": "The application deadline is [insert date]. Please ensure that you submit all required documents and complete your application before this date.",
    
    "Are there any standardized tests required?": "Yes, standardized tests such as the SAT or ACT may be required. Please check the specific admission requirements for details.",
    
    "Can I transfer credits from another institution?": "Yes, we accept transfer credits from accredited institutions. You will need to submit your transcripts and go through our credit transfer evaluation process.",
    
    "What is the admission interview process like?": "The admission interview is an opportunity for us to learn more about you. It may be conducted in-person or virtually, and it typically covers your academic background, extracurricular activities, and career goals.",
    
    "Is financial aid available?": "Yes, we offer various financial aid options. You can explore scholarships, grants, and loans. Be sure to fill out the Free Application for Federal Student Aid (FAFSA) to determine your eligibility for financial assistance.",
    
    "Can international students apply?": "Yes, we welcome international students. International applicants may need to provide additional documentation, such as English language proficiency test scores and a copy of their passport.",
    
    "How can I check the status of my application?": "You can check the status of your application by logging into your online application portal. Updates on your admission status and any required documents will be available there.",
    
    "What is the acceptance rate?": "The acceptance rate varies each year and depends on various factors. It is recommended to check our official website or contact the admission office for the most up-to-date information.",
    
    "Can I apply for early decision or early action?": "Yes, we offer early decision and early action options. Early decision is binding, while early action is non-binding. Please review the specific deadlines and requirements for each.",
    
    "What majors or programs do you offer?": "We offer a wide range of majors and programs. You can explore our academic catalog on the official website to see the complete list and details about each program.",
    
    "Are there any specific GPA requirements?": "While there is no strict GPA cutoff, a competitive GPA is typically required. Admissions decisions take into account various factors, including academic performance, extracurricular activities, and test scores.",
    
    "What documents are required for the application?": "The required documents may include your high school transcripts, recommendation letters, standardized test scores, and a personal statement or essay. Be sure to check the application instructions for the complete list.",
    
    "Is there an application fee?": "Yes, there is an application fee. The fee amount and payment details can be found on the application portal. Fee waivers may be available for eligible students.",
    
    "Can I submit additional materials to support my application?": "Yes, you can submit additional materials, such as a portfolio or a resume, to strengthen your application. Make sure to follow the guidelines provided in the application instructions.",
    
    "What is the policy on deferring admission?": "We may consider requests for deferring admission on a case-by-case basis. You will need to submit a formal request explaining the reason for deferral.",
    
    "How can I schedule a campus tour?": "You can schedule a campus tour through our official website. Campus tours are a great way to explore our facilities and get a feel for the campus environment.",
    
    "Are there specific requirements for certain programs, such as the honors program?": "Yes, some programs, like the honors program, may have additional admission requirements. Check the program-specific information on our website for details.",
    
    "What opportunities are there for student involvement on campus?": "We offer various student organizations, clubs, and activities. You can explore opportunities for involvement to enhance your college experience. Check our student life page for more information.",
    
    "How does the waitlist process work?": "If you find yourself on the waitlist, it means that we have reached our initial capacity. We may admit students from the waitlist as spots become available. You will be notified if a spot becomes available for you.",
    
    "Hi": "Hello! Welcome to our college admission chat. How can I assist you?",
    "Hello": "Hi there! How can I help you with your college admission questions?",
    "Hey": "Hey! I'm here to provide information about our college admission process. Feel free to ask any questions.",
    "Greetings": "Greetings! I'm here to help with any questions you may have about college admission.",
    "Howdy": "Howdy! Welcome to our college admission chat. What can I do for you?",
    "Goodbye": "Goodbye! If you have any more questions in the future, feel free to reach out. Have a great day!",
    "Thank you": "You're welcome! If you have any more questions or need assistance, feel free to ask. Goodbye!",
    "Bye": "Bye! If you need further assistance, don't hesitate to ask. Take care!",
    "Adios": "Adios! If you ever have more questions, feel free to return. Hasta luego!",
    "See you": "See you! If there's anything else you'd like to know, feel free to come back anytime.",
    "hi": "Hello! Welcome to our college admission chat. How can I assist you?",
}


@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    session['history'] = session.get('history', []) + [question]
    answer = knowledge_base.get(question, "I'm sorry, I don't know the answer to that.")
    return answer

if __name__ == '__main__':
    app.run(debug=True)