from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        print("Login:", email)

        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        print("Register:", name, email)

        return redirect(url_for("login"))

    return render_template("register.html")


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    user = {
        "name": "Shivani Singh",
        "email": "shivani@example.com",
        "skills": "Python, Java, SQL"
    }

    return render_template(
        "dashboard.html",
        user=user
    )


# ==========================================
# PROFILE
# ==========================================

@app.route("/profile")
def profile():
    return render_template("profile.html")


# ==========================================
# RECOMMENDATIONS
# ==========================================

@app.route("/recommendations")
def recommendations():

    recommendations = [
        "Python for Everybody",
        "Machine Learning by Andrew Ng",
        "SQL Fundamentals",
        "Git & GitHub",
        "Data Structures and Algorithms"
    ]

    return render_template(
        "recommendations.html",
        recommendations=recommendations
    )


# ==========================================
# SKILL GAP
# ==========================================

@app.route("/skill-gap")
def skill_gap():

    missing_skills = [
        "SQL",
        "Git",
        "Communication",
        "Data Structures"
    ]

    return render_template(
        "skill_gap.html",
        missing_skills=missing_skills
    )


# ==========================================
# PORTFOLIO
# ==========================================

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


# ==========================================
# PORTFOLIO PREVIEW
# ==========================================

@app.route("/portfolio-preview")
def portfolio_preview():

    sample_projects = [

        {
            "name": "SkillSphere AI",
            "description":
            "AI powered skill gap analyzer",
            "technology":
            "Python, Flask, SQLite"
        },

        {
            "name":
            "Student Result Management System",

            "description":
            "Web application for managing student results",

            "technology":
            "HTML, CSS, Python"
        }
    ]

    return render_template(

        "portfolio_preview.html",

        name="Shivani Singh",

        title="Software Engineer",

        about="Computer Science Engineering Student",

        profile_image=
        "https://via.placeholder.com/150",

        skills=[
            "Python",
            "Java",
            "SQL",
            "Flask"
        ],

        education=
        "B.Tech Computer Science Engineering",

        experience=
        "Project Development Experience",

        projects=sample_projects,

        certificates=[
            "Python Certificate",
            "Java Certificate"
        ],

        email="shivani@example.com",

        phone="+91 9876543210",

        linkedin=
        "https://linkedin.com",

        github=
        "https://github.com"
    )


# ==========================================
# RESUME BUILDER
# ==========================================

@app.route("/resume-builder")
def resume_builder():
    return render_template("resume_builder.html")


# ==========================================
# RESUME UPLOAD
# ==========================================

@app.route("/resume-upload")
def resume_upload():
    return render_template("resume_upload.html")


# ==========================================
# ROADMAP
# ==========================================

@app.route("/roadmap")
def roadmap():

    roadmap_data = {

        "Month 1": [
            "Python",
            "SQL"
        ],

        "Month 2": [
            "Pandas",
            "NumPy"
        ],

        "Month 3": [
            "Machine Learning"
        ],

        "Month 4": [
            "Projects"
        ]
    }

    return render_template(
        "roadmap.html",
        roadmap=roadmap_data
    )


# ==========================================
# ADMIN DASHBOARD
# ==========================================

@app.route("/admin")
def admin():

    return render_template(
        "admin_dashboard.html",

        total_users=50,

        total_skills=120,

        total_certificates=80,

        total_resumes=35,

        users=[]
    )
@app.route("/forgot-password")
def forgot_password():
    return """
    <h2>Forgot Password Page</h2>
    <p>This feature will be added soon.</p>
    """

# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)