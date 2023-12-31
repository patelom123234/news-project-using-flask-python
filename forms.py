from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password  = StringField("password", validators=[DataRequired()])
    submit = SubmitField('submit')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment",validators=[DataRequired()])
    submit = SubmitField("submit comment")

class ContectForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    phoneNumber = StringField("Phone Number", validators=[DataRequired()])
    message = CKEditorField("message", validators=[DataRequired()])
    submit = SubmitField("Submit")
