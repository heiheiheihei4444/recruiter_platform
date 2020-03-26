import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    engine=dbinfo.get("ENGINE")or "sqlite"
    driver=dbinfo.get("DRIVER")or "sqlite"
    user=dbinfo.get("USER")or""
    password=dbinfo.get("PASSWORD")or""
    host=dbinfo.get("HOST")or" "
    port=dbinfo.get("PORT")or""
    name=dbinfo.get("NAME")or""
    return"{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)

class Config:
    DEBUG=False
    TESTING=False
    RESTFUL_JSON = dict(ensure_ascii=False)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='heihei'

class DevelopConfig(Config):
    DEBUG = True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "HOST": "localhost",
        "PORT": "3306",
        "PASSWORD":"jiewei123",
        "NAME":"app1"

    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class StagingConfig(Config):
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "HOST": "localhost",
        "PORT": "3306",
        "PASSWORD":"jiewei123",
        "NAME":"app"

    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class ProductConfig(Config):
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "HOST":"localhost",
        "PORT":"3306",
        "PASSWORD":"jiewei123",
        "NAME":"app"

    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class TestingConfig(Config):
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "HOST": "localhost",
        "PORT": "3306",
        "PASSWORD":"jiewei123",
        "NAME":"app"

    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

envs={
    "develop":DevelopConfig,
    "testing":TestingConfig,
    "staging":StagingConfig,
    "product":ProductConfig,
    "default":ProductConfig
}