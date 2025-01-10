import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case_record.id'), nullable=False)
    alert_type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Observable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case_record.id'), nullable=False)
    observable_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(255), nullable=False)

class IOC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case_record.id'), nullable=False)
    ioc_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(255), nullable=False)

class ExternalReference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case_record.id'), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)

class CaseRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    alerts = db.relationship('Alert', backref='case', lazy=True)
    observables = db.relationship('Observable', backref='case', lazy=True)
    iocs = db.relationship('IOC', backref='case', lazy=True)
    external_references = db.relationship('ExternalReference', backref='case', lazy=True)

@app.route('/cases', methods=['GET'])
def get_cases():
    cases = CaseRecord.query.all()
    return jsonify([{'id': case.id, 'title': case.title, 'description': case.description, 'status': case.status} for case in cases])

@app.route('/cases', methods=['POST'])
def create_case():
    data = request.get_json()
    new_case = CaseRecord(title=data['title'], description=data['description'], status=data['status'])
    db.session.add(new_case)
    db.session.commit()
    return jsonify({'id': new_case.id}), 201

# Additional CRUD operations can be added here

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True) 