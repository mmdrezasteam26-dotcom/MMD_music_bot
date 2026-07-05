import sqlite3

conn = sqlite3.connect(
    "songs.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    performer TEXT,
    country TEXT,
    mood TEXT,
    file_id TEXT UNIQUE,
    duration INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


# ==========================
# Add Song
# ==========================

def add_song(title, performer, country, mood, file_id, duration):

    try:
        cursor.execute(
            """
            INSERT INTO songs
            (title,performer,country,mood,file_id,duration)

            VALUES(?,?,?,?,?,?)
            """,

            (
                title,
                performer,
                country,
                mood,
                file_id,
                duration
            )
        )

        conn.commit()
        return True
    
    except sqlite3.IntegrityError:
        return False


# ==========================
# Get Songs
# ==========================

def get_songs(country, mood):

    cursor.execute(
        """
        SELECT *
        FROM songs

        WHERE country=? AND mood=?

        ORDER BY title
        """,

        (
            country,
            mood
        )
    )

    return cursor.fetchall()


# ==========================
# Get Titles
# ==========================

def get_song_titles(country, mood):

    cursor.execute(
        """
        SELECT id,title

        FROM songs

        WHERE country=? AND mood=?
        """,

        (
            country,
            mood
        )
    )

    return cursor.fetchall()


# ==========================
# Delete Song
# ==========================

def delete_song(song_id):

    cursor.execute(
        """
        DELETE FROM songs

        WHERE id=?
        """,

        (song_id,)
    )

    conn.commit()


# ==========================
# Get One Song
# ==========================

def get_song(song_id):

    cursor.execute(
        """
        SELECT *

        FROM songs

        WHERE id=?
        """,

        (song_id,)
    )

    return cursor.fetchone()


# ==========================
# Count Songs
# ==========================

def count_songs():

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM songs
        """
    )

    return cursor.fetchone()[0]