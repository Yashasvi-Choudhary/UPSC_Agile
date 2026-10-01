from flask import Blueprint, render_template, redirect, url_for, request, session, flash, jsonify
from functools import wraps
from extensions import db
from models import User, UPSCPaper
from sqlalchemy import or_
from models import Syllabus, Feedback, QuizQuestion

admin_bp = Blueprint('admin', __name__)

def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Please login as admin to access this page.', 'warning')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@admin_bp.route('/dashboard')
@admin_login_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('admin.login'))   

@admin_bp.route('/manage_users')
@admin_login_required
def manage_users():
    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

@admin_bp.route('/delete-user/<int:user_id>', methods=['POST'])
@admin_login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
     
        return jsonify({'success': True, 'message': 'User deleted successfully.'})
    else:
 
        flash("User deleted successfully.", "success")
        return redirect(url_for('admin.manage_users'))
    

@admin_bp.route('/manage_pyqs')
@admin_login_required
def manage_pyqs():
    exam_type = request.args.get('exam_type', '').strip()
    paper_type = request.args.get('paper_type', '').strip()
    sub_paper_type = request.args.get('sub_paper_type', '').strip()
    year = request.args.get('year', '').strip()

    query = UPSCPaper.query

    if exam_type:
        query = query.filter(UPSCPaper.exam_type.ilike(f"%{exam_type}%"))
    if paper_type:
        query = query.filter(UPSCPaper.paper_type.ilike(f"%{paper_type}%"))
    if sub_paper_type:
        query = query.filter(UPSCPaper.sub_paper_type.ilike(f"%{sub_paper_type}%"))
    if year:
        if year.isdigit():
            query = query.filter(UPSCPaper.year == int(year))

    pyqs = query.all()
    return render_template('admin/manage_pyqs.html', pyqs=pyqs)

@admin_bp.route('/add_pyq', methods=['POST'])
@admin_login_required
def add_pyq():
    exam_type = request.form['exam_type'].strip().lower()
    paper_type = request.form['paper_type'].strip().lower()
    sub_paper_type = request.form.get('sub_paper_type', '').strip().lower() or None
    year = request.form['year']
    pdf_link = request.form['pdf_link']

    existing_pyq = UPSCPaper.query.filter_by(
        exam_type=exam_type,
        paper_type=paper_type,
        sub_paper_type=sub_paper_type,
        year=int(year)
    ).first()

    if existing_pyq:
        existing_pyq.pdf_link = pdf_link
        db.session.commit()
        flash("PDF updated in existing row.", "info")
    else:
        new_pyq = UPSCPaper(
            exam_type=exam_type,
            paper_type=paper_type,
            sub_paper_type=sub_paper_type,
            year=int(year),
            pdf_link=pdf_link
        )
        db.session.add(new_pyq)
        db.session.commit()
        flash("PYQ added successfully!", "success")

    return redirect(url_for('admin.manage_pyqs'))

@admin_bp.route('/edit-pyq/<int:pyq_id>', methods=['POST'])
@admin_login_required
def edit_pyq(pyq_id):
    pyq = UPSCPaper.query.get_or_404(pyq_id)
    data = request.form

    if 'pdf_link' in data:
        pyq.pdf_link = data['pdf_link']
    if 'year' in data and data['year'].isdigit():
        pyq.year = int(data['year'])

    db.session.commit()
    return '', 204

@admin_bp.route('/delete-pyq/<int:pyq_id>', methods=['POST'])
@admin_login_required
def delete_pyq(pyq_id):
    pyq = UPSCPaper.query.get_or_404(pyq_id)
    db.session.delete(pyq)
    db.session.commit()
    flash("PYQ deleted successfully!", "success")
    return redirect(url_for('admin.manage_pyqs'))

@admin_bp.route('/manage_syllabus', methods=['GET'])
@admin_login_required
def manage_syllabus():
    syllabi = Syllabus.query.order_by(Syllabus.year.desc()).all()
    return render_template('admin/manage_syllabus.html', syllabi=syllabi)

@admin_bp.route('/add_syllabus', methods=['POST'])
@admin_login_required
def add_syllabus():
    data = request.form
    exam_type = data.get('exam_type', '').strip()
    paper_type = data.get('paper_type', '').strip()
    year = data.get('year', '').strip()
    link = data.get('link', '').strip()

    if not (exam_type and paper_type and year.isdigit() and link):
        flash("Please fill all fields correctly to add syllabus.", "error")
        return redirect(url_for('admin.manage_syllabus'))

    new_syllabus = Syllabus(
        exam_type=exam_type,
        paper_type=paper_type,
        year=int(year),
        link=link
    )
    db.session.add(new_syllabus)
    db.session.commit()
    flash("Syllabus added successfully!", "success")
    return redirect(url_for('admin.manage_syllabus'))

@admin_bp.route('/edit_syllabus/<int:syllabus_id>', methods=['POST'])
@admin_login_required
def edit_syllabus(syllabus_id):
    syllabus = Syllabus.query.get_or_404(syllabus_id)
    data = request.form

    exam_type = data.get('exam_type', '').strip()
    paper_type = data.get('paper_type', '').strip()
    year = data.get('year', '').strip()
    link = data.get('link', '').strip()

    if not (exam_type and paper_type and year.isdigit() and link):
        flash("Please fill all fields correctly to update syllabus.", "error")
        return redirect(url_for('admin.manage_syllabus'))

    syllabus.exam_type = exam_type
    syllabus.paper_type = paper_type
    syllabus.year = int(year)
    syllabus.link = link

    db.session.commit()
    flash("Syllabus updated successfully!", "success")
    return redirect(url_for('admin.manage_syllabus'))

@admin_bp.route('/delete_syllabus/<int:syllabus_id>', methods=['POST'])
@admin_login_required
def delete_syllabus(syllabus_id):
    syllabus = Syllabus.query.get_or_404(syllabus_id)
    db.session.delete(syllabus)
    db.session.commit()
    flash("Syllabus deleted successfully!", "success")
    return redirect(url_for('admin.manage_syllabus'))


@admin_bp.route('/manage_feedbacks')
@admin_login_required
def manage_feedbacks():
    feedbacks = Feedback.query.order_by(Feedback.submitted_at.desc()).all()
    return render_template('admin/manage_feedbacks.html', feedbacks=feedbacks)


# ─── QUIZ MANAGEMENT ─────────────────────────────────────────────────────────

@admin_bp.route('/manage_quiz')
@admin_login_required
def manage_quiz():
    topic_filter = request.args.get('topic', '').strip()
    query = QuizQuestion.query
    if topic_filter:
        query = query.filter(QuizQuestion.topic.ilike(f'%{topic_filter}%'))
    questions = query.order_by(QuizQuestion.id.desc()).all()
    topics = db.session.query(QuizQuestion.topic).distinct().all()
    topics = [t[0] for t in topics if t[0]]
    return render_template('admin/manage_quiz.html', questions=questions, topics=topics, topic_filter=topic_filter)


@admin_bp.route('/add_quiz_question', methods=['POST'])
@admin_login_required
def add_quiz_question():
    data = request.form
    question_text = data.get('question', '').strip()
    option_a = data.get('option_a', '').strip()
    option_b = data.get('option_b', '').strip()
    option_c = data.get('option_c', '').strip()
    option_d = data.get('option_d', '').strip()
    correct_option = data.get('correct_option', '').strip().upper()
    explanation = data.get('explanation', '').strip()
    topic = data.get('topic', '').strip()

    if not all([question_text, option_a, option_b, option_c, option_d, correct_option]):
        flash('Please fill all required fields.', 'error')
        return redirect(url_for('admin.manage_quiz'))

    if correct_option not in ['A', 'B', 'C', 'D']:
        flash('Correct option must be A, B, C, or D.', 'error')
        return redirect(url_for('admin.manage_quiz'))

    new_q = QuizQuestion(
        question=question_text,
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
        correct_option=correct_option,
        explanation=explanation or None,
        topic=topic or None
    )
    db.session.add(new_q)
    db.session.commit()
    flash('Question added successfully!', 'success')
    return redirect(url_for('admin.manage_quiz'))


@admin_bp.route('/edit_quiz_question/<int:q_id>', methods=['POST'])
@admin_login_required
def edit_quiz_question(q_id):
    q = QuizQuestion.query.get_or_404(q_id)
    data = request.form

    q.question = data.get('question', q.question).strip()
    q.option_a = data.get('option_a', q.option_a).strip()
    q.option_b = data.get('option_b', q.option_b).strip()
    q.option_c = data.get('option_c', q.option_c).strip()
    q.option_d = data.get('option_d', q.option_d).strip()
    correct = data.get('correct_option', q.correct_option).strip().upper()
    if correct in ['A', 'B', 'C', 'D']:
        q.correct_option = correct
    q.explanation = data.get('explanation', q.explanation or '').strip() or None
    q.topic = data.get('topic', q.topic or '').strip() or None

    db.session.commit()
    flash('Question updated successfully!', 'success')
    return redirect(url_for('admin.manage_quiz'))


@admin_bp.route('/delete_quiz_question/<int:q_id>', methods=['POST'])
@admin_login_required
def delete_quiz_question(q_id):
    q = QuizQuestion.query.get_or_404(q_id)
    db.session.delete(q)
    db.session.commit()
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('admin.manage_quiz'))