import sqlite3
import os
import hashlib

database_file_name = "meta.db"
database_file_path  = os.path.join(os.path.dirname(__file__),database_file_name)

def hash_text(text):
    # Convert the text to bytes using UTF-8 encoding
    text_bytes = text.encode('utf-8')

    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the text bytes
    sha256_hash.update(text_bytes)

    # Get the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()

    # Return the hexadecimal hash digest
    return hex_digest

def register_new_user(email, username, password,plan):
    # Connect to the database
    conn = sqlite3.connect('../meta.db')
    c = conn.cursor()
    tableName = "registered_user"
    # Insert the new user into the table
    c.execute(f"Create TABLE IF NOT EXISTS {tableName} (email, username, password,plan);")
    c.execute(f"INSERT INTO {tableName} (email, username, password,plan) VALUES (?, ?,?,?)", (email, username, password,plan))
    print("created")
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    pwd = hash_text("spring2023")
    register_new_user("demo@demo.com",'damg7245', pwd,"free")