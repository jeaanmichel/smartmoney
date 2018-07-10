from app.user import db
from datetime import datetime


class Usuario(db.Model):

    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(20), nullable=False)
    ultimo_nome = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
