from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_pitches, get_pitch, search_pitch
from .forms import CommentsForm
from ..models import Comment

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    all_pitches = get_pitches()  
    title = 'Home - Welcome to The best Pitching Website Online'

    search_pitch = request.args.get('pitch_query')

    if search_pitch:
        return redirect(url_for('movie',pitch_name= search_pitch)) 
    else:
        return render_template('index.html', title = title , all_pitches= all_pitches)

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    pitch_comments = Comment.get_comments(pitch_id)

    return render_template('pitch.html',title= title ,found_pitch= found_pitch, pitch_comments= pitch_comments)

@main.route('/search/<pitch_name>')
def search(pitch_name):
    '''
    View function to display the search results
    '''
    searched_pitches = search_pitch(pitch_name)
    title = f'search results for {pitch_name}'

    return render_template('search.html',pitches = searched_pitches)

@main.route('/pitch/comments/new/<int:id>', methods = ['GET','POST'])
def new_comment(id):
    form = CommentsForm()
    pitch_result = get_pitch(id)

    if form.validate_on_submit():
        pitch = form.pitch.data
        comment = form.comment.data
        new_comment = Comment(pitch_result.id,pitch,comment)
        new_comment.save_comment()
        return redirect(url_for('pitch', pitch_id= pitch_result.id))
    title = f'{pitch_result.id} review'
    return render_template('new_comment.html',title = title, comment_form=form,pitch = pitch_result)
