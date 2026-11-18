# -*- coding: utf-8 -*-
from datetime import datetime
from ..extensions import db

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_on = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Todo '%s'>" % self.title

    def store_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_todo(self):
        db.session.delete(self)
        db.session.commit()
