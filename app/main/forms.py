from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    blog = TextAreaField('Please write your blog.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogComForm(FlaskForm):
    blogcom = TextAreaField('You can comment your blog',validators = [Required()])
    submit = SubmitField('Submit')
