import os

#モジュールの親ディレクトリのフルパスを取得
basedir = os.path.dirname(os.path.dirname(__file__))
#親ディレクトリのblog.sqliteをデータベースに設定
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.sqlite')

SECRET_KEY = os.urandom(10)

#管理者のユーザー名とパスワード
USERNAME ='matudatatuya'
PASSWORD = 'hh19802421'

#メール関連の設定
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False 
MAIL_USERNAME = 'matudatatuya7@gmail.com'
MAIL_PASSWORD = 'ptsigzwhhhkkyzfz'
MAIL_DEFAULT_SENDER = 'matudatatuya7@gmail.com'