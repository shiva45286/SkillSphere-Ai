import os

class Config:

    # Flask Secret Key
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "skillsphere_secret_key_2026"
    )

    # Database Configuration
    DATABASE = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "database.db"
    )

    # Upload Folder
    UPLOAD_FOLDER = "static/uploads"

    # Maximum Upload Size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Allowed Resume Extensions
    ALLOWED_EXTENSIONS = {
        "pdf",
        "doc",
        "docx"
    }

    # Session Configuration
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    # Application Name
    APP_NAME = "SkillSphere AI"

    # Admin Configuration
    ADMIN_EMAIL = "admin@skillsphereai.com"

    # Pagination
    USERS_PER_PAGE = 10

    # Skill Categories
    SKILL_CATEGORIES = [
        "Python",
        "Java",
        "C++",
        "Web Development",
        "Machine Learning",
        "Data Science",
        "Cloud Computing",
        "Cyber Security",
        "UI/UX Design",
        "DevOps"
    ]

    # Recommended Learning Platforms
    LEARNING_PLATFORMS = {
        "Python": [
            "Python for Everybody",
            "Flask Web Development",
            "Automate the Boring Stuff"
        ],
        "Java": [
            "Java Masterclass",
            "Spring Boot Course",
            "DSA with Java"
        ],
        "Web Development": [
            "HTML & CSS Bootcamp",
            "JavaScript Complete Guide",
            "React Developer Course"
        ],
        "Machine Learning": [
            "Machine Learning by Andrew Ng",
            "Deep Learning Specialization",
            "Scikit-Learn Tutorial"
        ],
        "Data Science": [
            "Pandas",
            "NumPy",
            "Data Visualization"
        ]
    }

    # Career Roles
    CAREER_ROLES = [
        "Software Engineer",
        "Data Analyst",
        "Data Scientist",
        "Machine Learning Engineer",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer",
        "Cloud Engineer",
        "Cyber Security Analyst",
        "DevOps Engineer"
    ]

    # Dashboard Statistics
    DEFAULT_TARGET_SKILLS = [
        "Python",
        "SQL",
        "Git",
        "Data Structures",
        "Communication"
    ]

    # AI Recommendation Settings
    MAX_RECOMMENDATIONS = 10

    # Debug Mode
    DEBUG = True

    # Project Version
    VERSION = "1.0.0"