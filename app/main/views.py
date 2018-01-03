from flask import render_template, request, redirect, url_for, abort  
from . import main  
from .forms import CommentsForm, UpdateProfile, PitchForm
from ..models import Comment, Pitch, User 
from flask_login import login_required, current_user
from .. import db,photos

import markdown2



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    search_pitch = request.args.get('pitch_query')
    pitches= Pitch.get_all_pitches()

    if search_pitch:
        return redirect(url_for('movie',pitch_name= search_pitch))  
    else:
        return render_template('index.html', title = title, pitches= pitches )

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

@main.route('/category/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    Function that creates new pitches
    '''
    form = PitchForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        pitch= form.content.data
        category_id = form.category_id.data
        new_pitch= Pitch(pitch= pitch, category_id= category_id)

        new_pitch.save_pitch() 

    return render_template('new_pitch.html', new_pitch_form= form, category= category)

@main.route('/category/<int:id>')
def category(id):
    '''
    function that returns pitches based on the entered category id
    '''
    category = PitchCategory.query.get(id)

    if category is None:
        abort(404)

    pitches_in_category = Pitches.get_pitch(id)
    return render_template('category.html' ,category= category, pitches= pitches_in_category)

@main.route('/pitch/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    pitch_result = get_pitch(id)

    if form.validate_on_submit():
        pitch = form.pitch.data
        comment = form.comment.data

        # redefine how the comments are constructed 
        new_comment = Comment(pitch_id=pitch_result.id,pitch_title=title,image_path=movie.poster,pitch_comment=review,user=current_user)


        new_comment.save_comment()
        return redirect(url_for('main.pitch', pitch_id= pitch_result.id))
    title = f'{pitch_result.id} review'
    return render_template('new_comment.html',title = title, comment_form=form,pitch = pitch_result)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

@main.route('/comment/<int:id>')
def single_comment(id):
    comment=Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.pitch_comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment=format_comment)

@main.route('/test/<int:id>')
def test(id):
    '''
    this is route for basic testing
    '''
    pitches= Pitch.get_all_pitches()
    pitches_by_category = Pitch.get_pitches_by_category(id)

    return render_template('test.html',pitches =pitches)

