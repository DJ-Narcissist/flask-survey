from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Initialize an empty list to store survey responses
responses = []

# Survey questions and options
survey_questions = [
    {
        "question": "Do you like Python?",
        "options": ["Yes", "No"],
    },
    {
        "question": "Have you used Flask before?",
        "options": ["Yes", "No"],
    },
    {
        "question": "What is your annual income?",
        "options": ["Less than $10,000", "$10,000 - $30,000", "$30,000 - $50,000", "More than $50,000"],
    },
    {
        "question": "Would you recommend Flask to others?",
        "options": ["Yes", "No"],
    }
]

@app.route('/')
def home():
    return render_template("home.html", title="Survey", instructions="Please answer the following questions:", button_text="Start Survey")

@app.route('/questions/<int:step>', methods=['GET','POST'])
def questions(step):
    if request.method =='POST':
        answer = request.form['answer']
        responses.append(answer)

    if step + 1 < len(survey_questions):
        return redirect(url_for('questions', step=step + 1))
    else: 
        return redirect(url_for('survey_completed'))

    if step < len(survey_questions):
        question_data= survey_questions[step]
        question = question_data['question']
        options = question_data['options']

        return render_template("question.html", title="Survey", question=question, options=options, step=step)

    return redirect(url_for('questions', step =0))

@app.route('/survey_completed')
def survey_completed():
    return "Thank you for completing the survey"



if __name__ == "__main__":
    app.run(debug=True)
