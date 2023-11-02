from app.extensions import db

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    image_name = db.Column(db.String(255), nullable=True)
    image_path = db.Column(db.String(2048), nullable=True)
    user = db.relationship('Users', backref=db.backref('tweets', lazy=True))
    like = db.Column(db.Integer, default=0)  # Menggunakan tipe data Integer untuk menghitung jumlah like

    def serialize(self): 
        return {
            "id": self.id,
            "content": self.content,
            "user_id" : self.user_id,
            "image_name": self.image_name,
            "image_path": self.image_path,
            "like": self.like,
            "user": self.user.serialize()
        }    
