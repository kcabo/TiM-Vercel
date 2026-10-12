import os

from sqlalchemy.engine import make_url


class Config:
    # requirements.txt に含まれる psycopg2 を明示し、既定ドライバーに依存しない。
    SQLALCHEMY_DATABASE_URI = make_url(
        os.environ["POSTGRES_URL"].replace("postgres://", "postgresql://", 1)
    ).set(drivername="postgresql+psycopg2")

    # DBの変更の度にロギングするのを防ぐ
    SQLALCHEMY_TRACK_MODIFICATIONS = False
