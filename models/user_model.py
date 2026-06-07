import sqlite3
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

DATABASE = "database.db"


class UserModel:

    def __init__(self):
        self.create_table()

    # ==================================
    # Database Connection
    # ==================================

    def get_connection(self):

        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row

        return conn

    # ==================================
    # Create Users Table
    # ==================================

    def create_table(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            skills TEXT,
            interests TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    # ==================================
    # Register User
    # ==================================

    def register_user(
        self,
        name,
        email,
        password
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        try:

            hashed_password = (
                generate_password_hash(password)
            )

            cursor.execute("""
            INSERT INTO users(
                name,
                email,
                password
            )
            VALUES(?,?,?)
            """,
            (
                name,
                email,
                hashed_password
            ))

            conn.commit()

            return True

        except sqlite3.IntegrityError:

            return False

        finally:
            conn.close()

    # ==================================
    # Login User
    # ==================================

    def login_user(
        self,
        email,
        password
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            if check_password_hash(
                user["password"],
                password
            ):
                return user

        return None

    # ==================================
    # Get User By ID
    # ==================================

    def get_user_by_id(
        self,
        user_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (user_id,)
        )

        user = cursor.fetchone()

        conn.close()

        return user

    # ==================================
    # Get User By Email
    # ==================================

    def get_user_by_email(
        self,
        email
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM users
        WHERE email = ?
        """,
        (email,)
        )

        user = cursor.fetchone()

        conn.close()

        return user

    # ==================================
    # Update User Profile
    # ==================================

    def update_profile(
        self,
        user_id,
        skills,
        interests
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE users
        SET skills = ?,
            interests = ?
        WHERE id = ?
        """,
        (
            skills,
            interests,
            user_id
        ))

        conn.commit()
        conn.close()

    # ==================================
    # Change Password
    # ==================================

    def change_password(
        self,
        user_id,
        new_password
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        hashed_password = (
            generate_password_hash(new_password)
        )

        cursor.execute("""
        UPDATE users
        SET password = ?
        WHERE id = ?
        """,
        (
            hashed_password,
            user_id
        ))

        conn.commit()
        conn.close()

    # ==================================
    # Delete User
    # ==================================

    def delete_user(
        self,
        user_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM users
        WHERE id = ?
        """,
        (user_id,)
        )

        conn.commit()
        conn.close()

    # ==================================
    # Get All Users
    # ==================================

    def get_all_users(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM users
        ORDER BY id DESC
        """)

        users = cursor.fetchall()

        conn.close()

        return users

    # ==================================
    # Total Users
    # ==================================

    def total_users(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM users
        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    # ==================================
    # Search Users
    # ==================================

    def search_users(
        self,
        keyword
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM users
        WHERE name LIKE ?
        OR email LIKE ?
        """,
        (
            "%" + keyword + "%",
            "%" + keyword + "%"
        ))

        users = cursor.fetchall()

        conn.close()

        return users


# ==================================
# Testing
# ==================================

if __name__ == "__main__":

    user_model = UserModel()

    success = user_model.register_user(
        "Shivani Singh",
        "shivani@gmail.com",
        "123456"
    )

    if success:
        print("User Registered Successfully")
    else:
        print("Email Already Exists")

    print("\nTotal Users:")
    print(user_model.total_users())

    print("\nAll Users:")

    users = user_model.get_all_users()

    for user in users:

        print(
            user["id"],
            user["name"],
            user["email"]
        )