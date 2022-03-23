class Config:
    DEBUG = True

    TESTING = False

    SECRET_KEY = "Kenevy"



class DevelopConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class StagingConfig(Config):
    pass


class ProductConfig(Config):
    pass



envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}