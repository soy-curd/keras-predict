# coding: UTF-8

class Config(object):
    SITE_NAME='画像予測'
    SITE_SLUG_NAME='image-predict'
    SITE_LOCATION='Outer space'
    TAGLINE='Predict images with AI'
    TAGLINES=['Image prediction using Deep Learning']
    SITE_DESCRIPTION='image prediction'
    SITE_KEYWORDS='depp learning'
    GOOGLE_SITE_VERIFICATION=' X'
    FACEBOOK_PAGE_ID=''
    TWITTER_ID=''
    #  google_plus_id='X'
    GOOGLE_ANALYTICS=' UA-x'
    ADMINS=['soycurd1@gmail.com']


class DevelopmentConfig(Config):
    DOMAIN= 'localhost=8002'
    ASSET_DOMAIN= 'localhost=8002'

class ProductionConfig(Config):
    DOMAIN= 'soy-curd.com/image-predict/'
    ASSET_DOMAIN= 'soy-curd.com/image-predict/'
