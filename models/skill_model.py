import sqlite3

DATABASE = "database.db"


class SkillModel:

    def __init__(self):
        self.create_table()

    # ====================================
    # Database Connection
    # ====================================

    def get_connection(self):
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

    # ====================================
    # Create Skills Table
    # ====================================

    def create_table(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS skills(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            skill_name TEXT NOT NULL,
            skill_level TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    # ====================================
    # Add Skill
    # ====================================

    def add_skill(
        self,
        user_id,
        skill_name,
        skill_level
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO skills(
            user_id,
            skill_name,
            skill_level
        )
        VALUES(?,?,?)
        """,
        (
            user_id,
            skill_name,
            skill_level
        ))

        conn.commit()
        conn.close()

    # ====================================
    # Get Skills By User
    # ====================================

    def get_user_skills(
        self,
        user_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM skills
        WHERE user_id = ?
        """,
        (user_id,)
        )

        skills = cursor.fetchall()

        conn.close()

        return skills

    # ====================================
    # Update Skill Level
    # ====================================

    def update_skill(
        self,
        skill_id,
        skill_level
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE skills
        SET skill_level = ?
        WHERE id = ?
        """,
        (
            skill_level,
            skill_id
        ))

        conn.commit()
        conn.close()

    # ====================================
    # Delete Skill
    # ====================================

    def delete_skill(
        self,
        skill_id
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM skills
        WHERE id = ?
        """,
        (skill_id,)
        )

        conn.commit()
        conn.close()

    # ====================================
    # Skill Gap Analysis
    # ====================================

    def skill_gap_analysis(
        self,
        user_id
    ):

        required_skills = [
            "Python",
            "SQL",
            "Git",
            "Communication",
            "Data Structures"
        ]

        user_skills = []

        skills = self.get_user_skills(user_id)

        for skill in skills:
            user_skills.append(
                skill["skill_name"]
            )

        missing_skills = []

        for skill in required_skills:

            if skill not in user_skills:
                missing_skills.append(skill)

        return missing_skills

    # ====================================
    # Skill Statistics
    # ====================================

    def get_skill_statistics(
        self,
        user_id
    ):

        skills = self.get_user_skills(user_id)

        stats = {
            "Beginner": 0,
            "Intermediate": 0,
            "Advanced": 0
        }

        for skill in skills:

            level = skill["skill_level"]

            if level in stats:
                stats[level] += 1

        return stats

    # ====================================
    # Get Total Skills
    # ====================================

    def total_skills(
        self,
        user_id
    ):

        skills = self.get_user_skills(user_id)

        return len(skills)

    # ====================================
    # Search Skill
    # ====================================

    def search_skill(
        self,
        user_id,
        keyword
    ):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM skills
        WHERE user_id = ?
        AND skill_name LIKE ?
        """,
        (
            user_id,
            "%" + keyword + "%"
        ))

        results = cursor.fetchall()

        conn.close()

        return results


# ====================================
# Testing
# ====================================

if __name__ == "__main__":

    skill_model = SkillModel()

    skill_model.add_skill(
        1,
        "Python",
        "Advanced"
    )

    skill_model.add_skill(
        1,
        "Java",
        "Intermediate"
    )

    print("\nUser Skills:\n")

    skills = skill_model.get_user_skills(1)

    for skill in skills:
        print(
            skill["skill_name"],
            "-",
            skill["skill_level"]
        )

    print("\nMissing Skills:")
    print(
        skill_model.skill_gap_analysis(1)
    )

    print("\nStatistics:")
    print(
        skill_model.get_skill_statistics(1)
    )