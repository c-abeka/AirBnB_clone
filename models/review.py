#1/usr/bin/python3

'''
    Review Module

    containes attributes to the reviews 
    created by users
'''

from models.base_model import BaseModel

class Review(BaseModel):
    ''' Review Class

        Fields:
            place_id(str): uuid or place
            user_id(str): uuid of user
            text(str): the review message
    '''
    
    place_id = ''
    user_id = ''
    text = ''