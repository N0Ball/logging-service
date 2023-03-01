import os
import datetime

 
class BaseConfig:
    SECRET_KEY = 'ff5c9316ab2939c0cfefb52c940692cffc28f4051d0ba6e3d41f64785ff0b1e9'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True

class DeployConfig(BaseConfig):
    DEBUG = False

config = {
    'deployment': DeployConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
