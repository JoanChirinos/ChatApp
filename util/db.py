import sqlite3

DB_FILE = 'data/chat.db'


def create_db():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages(chat TEXT, message TEXT)')

    db.commit()
    db.close()


def add_message(chat, message):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute('INSERT INTO messages VALUES (?, ?)', (chat, message))

    db.commit()
    db.close()


def get_messages(chat):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute('SELECT message FROM messages WHERE chat=?', (chat,))
    msgs = c.fetchall()

    return msgs


if __name__ == '__main__':
    create_db()
    print('created!')
