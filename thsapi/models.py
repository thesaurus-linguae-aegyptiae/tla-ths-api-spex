from flask_sqlalchemy import SQLAlchemy

from thsapi import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

#from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()


taxonomy_table = db.Table('taxonomy', db.Model.metadata,
        db.Column('parent_id', db.String(24), db.ForeignKey('descriptor.id')),
        db.Column('child_id', db.String(24), db.ForeignKey('descriptor.id'))
        )
        


class Descriptor(db.Model):
    __tablename__ = 'descriptor'
    id = db.Column(db.String(24), unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(80), nullable=False)
    parents = db.relationship("Descriptor",
            secondary=taxonomy_table,
            primaryjoin=taxonomy_table.c.parent_id==id,
            secondaryjoin=taxonomy_table.c.child_id==id,
            backref="children")

