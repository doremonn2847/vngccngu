# from flask import render_template, flash, redirect, url_for
# from app import app
# from app.forms import LoginForm

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Miguel'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data
#         ))
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign In', form=form)

    



from flask import render_template, request, redirect, url_for
from app import db
from app.models import Post
from app.forms import PostForm

def init_app(app):
    @app.route('/')
    def cuutoivoi():
        form = PostForm()
        return render_template('test.html', form=form)

    @app.route('/submit', methods=['POST'])
    def submit_post():
        if request.method == 'POST':
            title = request.form.get('title')
            author = request.form.get('author')
            body = request.form.get('body')

            # Create a new post and add it to the database
            new_post = Post(title=title, author=author, body=body)
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('show_submission_result', title=title, author=author, body=body))
        return "Invalid request method"

    @app.route('/submission_result')
    def show_submission_result():
        title = request.args.get('title')
        author = request.args.get('author')
        body = request.args.get('body')
        
        return render_template('submission_result.html', title=title, author=author, body=body)