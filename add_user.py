from index import app, db, User

with app.app_context():
    db.create_all()
    db.session.add(User(username="First User"))
    db.session.commit()
