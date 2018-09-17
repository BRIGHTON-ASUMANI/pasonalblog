from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    blog = TextAreaField('Write a blog')
    submit = SubmitField('Submit')

class BlogComForm(FlaskForm):
    blogcom = TextAreaField('comment on your blog ')
    submit = SubmitField('Submit')
