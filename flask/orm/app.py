from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask
app = Flask(__name__)

# sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
db = SQLAlchemy(app)

# migrate 초기화
migrate = Migrate(app, db)


# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
# 정리
# [Create]
# INSERT INTO users (username,email) VALUES('hyeonjin23', 'choo0618@naver.com')
# user = User(username='hyeonjin23', email='choo0618@naver.com')
# db.session.add(user)
# db.session.commit()

# [Read]
# SELECT * FROM users;
# users = User.query.all() # 복수

# SELECT * FROM users WHERE username='hyeonjin23' LIMIT 1;
# user = User.query.filter_by(username='hyeonjin23').first()

# SELECT *FROM users WHERE id=2 LIMIT 1;
# user = User.query.get(2)
# primary key만 get으로 가져올 수 있음.

# SELECT * FROM users WHERE email LIKE '%cho%'
# users = User.query.filter(User.email.like("%cho%")).all()