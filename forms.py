from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import data_required, length, equal_to
from flask_wtf.file import FileField,FileRequired, FileSize, FileAllowed

class RegisterForm(FlaskForm):
    username = StringField("Your Username", validators=[data_required(message="Username field should not be empty"), length(min=5,max=15, message="username should contain 5-15 letters")])
    password = PasswordField("Your Password", validators=[data_required(message="password field should not be empty"), length(min=8,max=32, message="Password should contain 8-32 letters")])
    repeat_password = PasswordField("Repeat Your Password", validators=[data_required(message="Repeat password field should not be empty"), equal_to("password", message="Passwords do not match")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Your Username", validators=[data_required(message="Username field should not be empty"), length(min=5,max=15, message="username should contain 5-15 letters")])
    password = PasswordField("Your Password", validators=[data_required(message="password field should not be empty"), length(min=8,max=32, message="Password should contain 8-32 letters")])
    submit = SubmitField("Log in")

class PostForm(FlaskForm):
    description = StringField("Information about the game", validators=[data_required(message="description field should not be empty")])
    game_name = StringField("Game name", validators=[data_required(message="name field should not be empty")])
    game_img = FileField("Game image")
    submit = SubmitField("Post")