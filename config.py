from flask_mysqldb import MySQL


class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '01082021'
    MYSQL_DB = 'api_flask'

config = {
    'development': DevelopmentConfig
}
