from app import db
from datetime import datetime

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    version = db.Column(db.String(20))
    download_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
