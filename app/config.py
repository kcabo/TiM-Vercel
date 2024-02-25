import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["POSTGRES_URL"]

    # DBの変更の度にロギングするのを防ぐ
    SQLALCHEMY_TRACK_MODIFICATIONS = False
