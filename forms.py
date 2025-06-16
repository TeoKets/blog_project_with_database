from wsgiref.validate import validator


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import EmailField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField




class CreatePostForm(FlaskForm):
   title = StringField("Blog Post Title", validators=[DataRequired()])
   subtitle = StringField("Subtitle", validators=[DataRequired()])
   img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
   body = CKEditorField("Blog Content", validators=[DataRequired()])
   submit = SubmitField("Submit Post")




class RegisterForm(FlaskForm):
   username = StringField("username",validators=[DataRequired()])
   password=PasswordField("password",validators=[DataRequired()])
   email = EmailField("email address", validators=[DataRequired()])
   submit=SubmitField("Register")




class LoginForm(FlaskForm):
   email = EmailField("email address", validators=[DataRequired()])
   password = PasswordField("password", validators=[DataRequired()])
   submit = SubmitField("Login")


class CommentForm(FlaskForm):
   comment=CKEditorField(label="comment",validators=[DataRequired()])
   submit=SubmitField(label="Comment")