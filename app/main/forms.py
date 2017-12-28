
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    pitch = StringField('Title',validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')