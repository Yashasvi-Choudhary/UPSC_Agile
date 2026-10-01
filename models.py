from extensions import db
from flask_login import UserMixin
from datetime import datetime



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    session_token = db.Column(db.String(255), nullable=True)
    quiz_streak = db.Column(db.Integer, default=0)
    last_quiz_date = db.Column(db.Date, nullable=True)
    last_quiz_score = db.Column(db.Integer, default=0)
    total_quizzes_played = db.Column(db.Integer, default=0)

class UPSCPaper(db.Model):
    __tablename__ = 'upsc_papers'
    id = db.Column(db.Integer, primary_key=True)
    exam_type = db.Column(db.String(50))
    paper_type = db.Column(db.String(100))
    sub_paper_type = db.Column(db.String(50))
    year = db.Column(db.Integer)
    pdf_link = db.Column(db.Text)




class Syllabus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_type = db.Column(db.String(100), nullable=False)
    paper_type = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 




class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)


class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(500), nullable=False)
    option_b = db.Column(db.String(500), nullable=False)
    option_c = db.Column(db.String(500), nullable=False)
    option_d = db.Column(db.String(500), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)  # 'A', 'B', 'C', or 'D'
    explanation = db.Column(db.Text, nullable=True)
    topic = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class StudyTask(db.Model):
    __tablename__ = 'study_tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_text = db.Column(db.String(500), nullable=False)
    task_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('study_tasks', lazy=True))