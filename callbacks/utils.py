import sqlite3
from assets.lib import vacancy

conn = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = conn.cursor()


def words(key: str) -> str:
    return vacancy[key]["word"]


def link(key: str) -> str:
    return vacancy[key]["link"]
