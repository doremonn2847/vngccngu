# from flask_wtf import FlaskForm 
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])   
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')



from flask_wtf import FlaskForm
from wtforms import StringField
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    body = CKEditorField('Body')