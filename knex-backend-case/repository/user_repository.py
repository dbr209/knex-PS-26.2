from sqlite3 import IntegrityError

from database.connection import get_connection

def get_user_by_email(email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    user = cur.fetchone()

    conn.close()

    if user:
        return dict(user)
    return user

def get_user_by_id(id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE id = ?",
        (id,)
    )

    user = cur.fetchone()

    conn.close()

    if user:
        return dict(user)
    return user

def create_user(name, email, hashed_password, role):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO users (name, email, password_hash, role)
            VALUES (?, ?, ?, ?)
            """,
            (name, email, hashed_password, role)
        )

        conn.commit()
        return True

    except IntegrityError:
        return False

    finally:
        conn.close()