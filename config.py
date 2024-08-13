import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')


from app import create_app  # Replace with your actual package name

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)