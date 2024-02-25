import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

    # DBの変更の度にロギングするのを防ぐ
    SQLALCHEMY_TRACK_MODIFICATIONS = False
