from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import schema
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+cx_oracle://system:sporades@centos13:1521/casinodev"
oracle_db_metadata = schema.MetaData(schema='PANAGIOTIS')

db = SQLAlchemy(app, metadata=oracle_db_metadata)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue with the task!"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)