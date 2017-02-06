class Config(object):
    DEBUG = False
    SHOW_GOOGLE_ANALYTICS = False


class ProductionConfig(Config):
    SHOW_GOOGLE_ANALYTICS = True


class DevelopmentConfig(Config):
    DEBUG = True
