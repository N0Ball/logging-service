from flask import Blueprint

health = Blueprint(
    'health',
    __name__,
    url_prefix="/health" 
)

@health.route('/')
def check():
    return {
        'detail': "OK"
    }, 200