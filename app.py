from flask import Flask, render_template

import models


app = Flask(__name__)


@app.route("/")
@app.route("/students")
@app.route("/students/<student_id>")
def students_list(student_id=None):
    if student_id:
        students = models.Student.select().where(
            models.Student.id == student_id
        )
    else:
        students = models.Student.select()

    return render_template('students.html', students=students)


@app.route("/teachers")
@app.route("/teachers/<teacher_id>")
def teachers_list(teacher_id=None):
    if teacher_id:
        teachers = models.Teacher.select().where(
            models.Teacher.id == teacher_id
        )
    else:
        teachers = models.Teacher.select()

    return render_template('teachers.html', teachers=teachers)


@app.route("/subjects")
@app.route("/subjects/<subject_id>")
def subjects_list(subject_id=None):
    if subject_id:
        subjects = models.Subject.select().where(
            models.Subject.id == subject_id
        )
    else:
        subjects = models.Subject.select()

    return render_template('subjects.html', subjects=subjects)


@app.route("/marks")
@app.route("/marks/<mark_id>")
def marks_list(mark_id=None):
    if mark_id:
        marks = models.Mark.select().where(
            models.Mark.id == mark_id
        )
    else:
        marks = models.Mark.select()

    return render_template('marks.html', marks=marks)


if __name__ == "__main__":
    models.initialize()

    app.run(debug=True)  # debug=True, host=8000, port='0.0.0.0'