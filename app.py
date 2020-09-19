from flask import Flask, render_template
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

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)