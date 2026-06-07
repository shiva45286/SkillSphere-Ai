import sqlite3

DATABASE = "database.db"


class CertificateModel:

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
    # Create Table
    # ==================================

    def create_table(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS certificates(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            certificate_name TEXT NOT NULL,
            platform TEXT NOT NULL,
            issue_date TEXT,
            certificate_link TEXT,
            uploaded_file TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    # ==================================
    # Add Certificate
    # ==================================

    def add_certificate(
        self,
        user_id,
        certificate_name,
        platform,
        issue_date,
        certificate_link="",
        uploaded_file=""
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO certificates(
            user_id,
            certificate_name,
            platform,
            issue_date,
            certificate_link,
            uploaded_file
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            user_id,
            certificate_name,
            platform,
            issue_date,
            certificate_link,
            uploaded_file
        ))

        conn.commit()
        conn.close()

    # ==================================
    # Get Certificates By User
    # ==================================

    def get_user_certificates(
        self,
        user_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM certificates
        WHERE user_id = ?
        ORDER BY issue_date DESC
        """,
        (user_id,)
        )

        certificates = cursor.fetchall()

        conn.close()

        return certificates

    # ==================================
    # Get Certificate By ID
    # ==================================

    def get_certificate_by_id(
        self,
        certificate_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM certificates
        WHERE id = ?
        """,
        (certificate_id,)
        )

        certificate = cursor.fetchone()

        conn.close()

        return certificate

    # ==================================
    # Update Certificate
    # ==================================

    def update_certificate(
        self,
        certificate_id,
        certificate_name,
        platform,
        issue_date,
        certificate_link
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE certificates
        SET certificate_name = ?,
            platform = ?,
            issue_date = ?,
            certificate_link = ?
        WHERE id = ?
        """,
        (
            certificate_name,
            platform,
            issue_date,
            certificate_link,
            certificate_id
        ))

        conn.commit()
        conn.close()

    # ==================================
    # Delete Certificate
    # ==================================

    def delete_certificate(
        self,
        certificate_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM certificates
        WHERE id = ?
        """,
        (certificate_id,)
        )

        conn.commit()
        conn.close()

    # ==================================
    # Count User Certificates
    # ==================================

    def count_certificates(
        self,
        user_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM certificates
        WHERE user_id = ?
        """,
        (user_id,)
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    # ==================================
    # Search Certificates
    # ==================================

    def search_certificates(
        self,
        user_id,
        keyword
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM certificates
        WHERE user_id = ?
        AND (
            certificate_name LIKE ?
            OR platform LIKE ?
        )
        """,
        (
            user_id,
            "%" + keyword + "%",
            "%" + keyword + "%"
        ))

        certificates = cursor.fetchall()

        conn.close()

        return certificates

    # ==================================
    # Platform Statistics
    # ==================================

    def platform_statistics(
        self,
        user_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT platform,
               COUNT(*) as total
        FROM certificates
        WHERE user_id = ?
        GROUP BY platform
        """,
        (user_id,)
        )

        stats = cursor.fetchall()

        conn.close()

        return stats


# ==================================
# Testing
# ==================================

if __name__ == "__main__":

    certificate_model = CertificateModel()

    certificate_model.add_certificate(
        1,
        "Python for Everybody",
        "Coursera",
        "2025-08-01",
        "https://coursera.org"
    )

    certificate_model.add_certificate(
        1,
        "Java Programming",
        "Udemy",
        "2025-09-01",
        "https://udemy.com"
    )

    print("\n===== Certificates =====\n")

    certificates = (
        certificate_model.get_user_certificates(1)
    )

    for cert in certificates:

        print(
            cert["certificate_name"],
            "-",
            cert["platform"]
        )

    print("\nTotal Certificates:")

    print(
        certificate_model.count_certificates(1)
    )

    print("\nPlatform Statistics:")

    stats = (
        certificate_model.platform_statistics(1)
    )

    for row in stats:

        print(
            row["platform"],
            ":",
            row["total"]
        )