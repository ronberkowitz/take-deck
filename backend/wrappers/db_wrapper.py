# import sqlite3
# import psycopg2
import sqlite3

PATH_TO_DB = '../database/take-deck.db'


class Database:
    def __init__(self):
        db = sqlite3.connect(PATH_TO_DB)
        cursor = db.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS running_games(game_id TEXT,  TEXT, aes_key TEXT, first_name TEXT, last_name TEXT, email TEXT)')
        db.commit()


x = Database()