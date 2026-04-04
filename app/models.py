from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(10), nullable=False, default='JMD')
    property_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    images = db.relationship('PropertyImage', backref='property', lazy=True, cascade='all, delete-orphan')

class PropertyImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)