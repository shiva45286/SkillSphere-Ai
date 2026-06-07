# ==========================================
# SkillSphere AI Recommendation Engine
# ==========================================

class SkillRecommender:

    def __init__(self):

        self.learning_resources = {

            "Python": [
                "Python for Everybody - Coursera",
                "Automate the Boring Stuff with Python",
                "Flask Web Development",
                "Python Data Structures"
            ],

            "Java": [
                "Java Programming Masterclass",
                "Spring Boot for Beginners",
                "DSA with Java",
                "Java OOP Concepts"
            ],

            "Web Development": [
                "HTML & CSS Complete Course",
                "JavaScript Mastery",
                "React JS Fundamentals",
                "Full Stack Development"
            ],

            "Data Science": [
                "Pandas for Data Analysis",
                "NumPy Fundamentals",
                "Data Visualization with Python",
                "Data Science Bootcamp"
            ],

            "Machine Learning": [
                "Machine Learning by Andrew Ng",
                "Scikit-Learn Tutorial",
                "Deep Learning Specialization",
                "ML Projects for Beginners"
            ],

            "Cyber Security": [
                "Ethical Hacking Basics",
                "Network Security",
                "Cyber Security Fundamentals",
                "Penetration Testing"
            ],

            "Cloud Computing": [
                "AWS Cloud Practitioner",
                "Microsoft Azure Fundamentals",
                "Google Cloud Basics",
                "Docker and Kubernetes"
            ],

            "DevOps": [
                "Git & GitHub",
                "Docker Essentials",
                "CI/CD Pipeline",
                "Jenkins Fundamentals"
            ]
        }

        self.career_paths = {

            "Python": [
                "Software Developer",
                "Backend Developer",
                "Automation Engineer"
            ],

            "Java": [
                "Java Developer",
                "Software Engineer",
                "Android Developer"
            ],

            "Web Development": [
                "Frontend Developer",
                "Full Stack Developer",
                "UI Developer"
            ],

            "Data Science": [
                "Data Analyst",
                "Data Scientist",
                "Business Analyst"
            ],

            "Machine Learning": [
                "ML Engineer",
                "AI Engineer",
                "Research Engineer"
            ],

            "Cyber Security": [
                "Security Analyst",
                "Ethical Hacker",
                "Cyber Security Engineer"
            ],

            "Cloud Computing": [
                "Cloud Engineer",
                "AWS Engineer",
                "Cloud Architect"
            ]
        }

    # ==========================================
    # Generate Recommendations
    # ==========================================

    def recommend_courses(self, interests):

        recommendations = []

        for interest in interests:

            interest = interest.strip()

            if interest in self.learning_resources:

                recommendations.extend(
                    self.learning_resources[interest]
                )

        return list(set(recommendations))

    # ==========================================
    # Career Suggestions
    # ==========================================

    def recommend_careers(self, interests):

        careers = []

        for interest in interests:

            interest = interest.strip()

            if interest in self.career_paths:

                careers.extend(
                    self.career_paths[interest]
                )

        return list(set(careers))

    # ==========================================
    # Skill Gap Analysis
    # ==========================================

    def skill_gap_analysis(self, user_skills):

        required_skills = [

            "Python",
            "SQL",
            "Git",
            "Communication",
            "Data Structures"
        ]

        missing_skills = []

        for skill in required_skills:

            if skill.lower() not in [
                s.lower().strip()
                for s in user_skills
            ]:

                missing_skills.append(skill)

        return missing_skills

    # ==========================================
    # User Report
    # ==========================================

    def generate_report(
        self,
        skills,
        interests
    ):

        report = {}

        report["skills"] = skills

        report["interests"] = interests

        report["missing_skills"] = (
            self.skill_gap_analysis(skills)
        )

        report["recommended_courses"] = (
            self.recommend_courses(interests)
        )

        report["career_suggestions"] = (
            self.recommend_careers(interests)
        )

        return report


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    recommender = SkillRecommender()

    user_skills = [
        "Python",
        "Git"
    ]

    user_interests = [
        "Machine Learning",
        "Data Science"
    ]

    report = recommender.generate_report(
        user_skills,
        user_interests
    )

    print("\n===== SkillSphere AI Report =====\n")

    print("Skills:")
    print(report["skills"])

    print("\nInterests:")
    print(report["interests"])

    print("\nMissing Skills:")
    print(report["missing_skills"])

    print("\nRecommended Courses:")
    print(report["recommended_courses"])

    print("\nCareer Suggestions:")
    print(report["career_suggestions"])