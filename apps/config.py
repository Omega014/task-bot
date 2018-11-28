import os


class BaseConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/taskbot?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'host': os.getenv('DB_HOST', '127.0.0.1'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Slack
    SLACK_AUTH_URL = "https://slack.com/oauth/authorize?"
    SLACK_AUTH_ACCESS_URL = "info: https://slack.com/api/oauth.access?"
    CLIENT_ID = os.getenv('CLIENT_ID', '')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET', '')
    SCOPE = "identify"
    TEAM_NAME = os.getenv('TEAM_NAME', '')
    REDIRECT_URI = os.getenv('REDIRECT_URI' + '/mypage', 'http://locaclhost:5000/mypage')
    STATE = ""

Config = BaseConfig
