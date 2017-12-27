from .models import Pitch, list_of_pitches

Pitch = Pitch

sample_pitches = list_of_pitches

#Getting the secret key
secret_key = None

def configure_request(app):
    global secret_key
    secret_key = app.config['SECRET_KEY']



def get_pitches():
    '''
    Function that will get list of pitches from the database
    '''
    requested_pitches = process_pitches(list_of_pitches)
    return requested_pitches

def process_pitches(list_of_pitches_objects):
    '''
    Function that will define the results retrived from the database
    '''
    processed_pitches =[]
    for obj in list_of_pitches_objects:
        id= obj[0]
        pitch= obj[1]

        pitch_object = Pitch(id,pitch)
        processed_pitches.append(pitch_object)

    return processed_pitches

def get_pitch(id):
    '''
    Function that will a get a pitch using the id passed in
    '''
    requested_pitches1 = sample_pitches
    pitch_object = None
    for obj in requested_pitches1:
        if id in obj:
            id= obj[0]
            pitch = obj[1]

            pitch_object = Pitch(id,pitch)

    return pitch_object

def search_pitch(pitch_name):
    '''
    Function that will a get a pitch using user input passed in
    '''
    found_list= []
    requested_pitches1 = sample_pitches
    search_objects = []
    for obj in requested_pitches1:
        if pitch_name in obj:
            id= obj[0]
            pitch = obj[1]

            found_pitch= Pitch(id,pitch)
            found_list.append(found_pitch)
    
    return found_list