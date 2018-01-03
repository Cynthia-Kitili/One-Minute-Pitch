
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    pitch = StringField('Title',validators=[Required()])
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class PitchForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    category_id = SelectField(u'Pitch Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    submit = SubmitField('SUBMIT')
    