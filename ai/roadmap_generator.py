# ==========================================
# SkillSphere AI - Roadmap Generator
# ==========================================

class RoadmapGenerator:

    def __init__(self):

        self.roadmaps = {

            "Software Engineer": {
                "Month 1": [
                    "Programming Fundamentals",
                    "Python Basics",
                    "Git & GitHub"
                ],
                "Month 2": [
                    "Data Structures",
                    "Algorithms",
                    "Problem Solving"
                ],
                "Month 3": [
                    "Database Management",
                    "SQL",
                    "Object-Oriented Programming"
                ],
                "Month 4": [
                    "Projects",
                    "System Design Basics",
                    "Interview Preparation"
                ]
            },

            "Data Analyst": {
                "Month 1": [
                    "Excel",
                    "Statistics",
                    "Data Cleaning"
                ],
                "Month 2": [
                    "SQL",
                    "Python",
                    "Pandas"
                ],
                "Month 3": [
                    "Data Visualization",
                    "Power BI",
                    "Matplotlib"
                ],
                "Month 4": [
                    "Real Projects",
                    "Dashboard Creation",
                    "Interview Preparation"
                ]
            },

            "Data Scientist": {
                "Month 1": [
                    "Python",
                    "Statistics",
                    "Mathematics"
                ],
                "Month 2": [
                    "Pandas",
                    "NumPy",
                    "Data Visualization"
                ],
                "Month 3": [
                    "Machine Learning",
                    "Scikit-Learn",
                    "Model Evaluation"
                ],
                "Month 4": [
                    "Deep Learning",
                    "Projects",
                    "Portfolio Building"
                ]
            },

            "Machine Learning Engineer": {
                "Month 1": [
                    "Python",
                    "Data Structures",
                    "Statistics"
                ],
                "Month 2": [
                    "Machine Learning",
                    "Scikit-Learn",
                    "Feature Engineering"
                ],
                "Month 3": [
                    "Deep Learning",
                    "TensorFlow",
                    "Neural Networks"
                ],
                "Month 4": [
                    "MLOps",
                    "Deployment",
                    "Industry Projects"
                ]
            },

            "Frontend Developer": {
                "Month 1": [
                    "HTML",
                    "CSS",
                    "Responsive Design"
                ],
                "Month 2": [
                    "JavaScript",
                    "DOM",
                    "ES6"
                ],
                "Month 3": [
                    "React",
                    "API Integration",
                    "Routing"
                ],
                "Month 4": [
                    "Portfolio Projects",
                    "Deployment",
                    "Interview Preparation"
                ]
            },

            "Backend Developer": {
                "Month 1": [
                    "Python",
                    "Flask",
                    "Git"
                ],
                "Month 2": [
                    "SQL",
                    "Database Design",
                    "REST APIs"
                ],
                "Month 3": [
                    "Authentication",
                    "Security",
                    "Testing"
                ],
                "Month 4": [
                    "Deployment",
                    "Projects",
                    "Interview Preparation"
                ]
            },

            "Full Stack Developer": {
                "Month 1": [
                    "HTML",
                    "CSS",
                    "JavaScript"
                ],
                "Month 2": [
                    "React",
                    "Frontend Projects",
                    "Bootstrap"
                ],
                "Month 3": [
                    "Python",
                    "Flask",
                    "SQL"
                ],
                "Month 4": [
                    "Full Stack Projects",
                    "Deployment",
                    "Portfolio"
                ]
            }
        }

    # ==========================================
    # Generate Roadmap
    # ==========================================

    def generate_roadmap(self, career):

        if career in self.roadmaps:
            return self.roadmaps[career]

        return {
            "Message": [
                "Career roadmap not found."
            ]
        }

    # ==========================================
    # Print Roadmap
    # ==========================================

    def display_roadmap(self, career):

        roadmap = self.generate_roadmap(career)

        print("\n==============================")
        print("Career Roadmap")
        print("==============================\n")

        print("Target Career:", career)
        print()

        for month, topics in roadmap.items():

            print(month)

            for topic in topics:
                print("  ✓", topic)

            print()

    # ==========================================
    # Get Progress Percentage
    # ==========================================

    def calculate_progress(
        self,
        completed_topics,
        total_topics
    ):

        if total_topics == 0:
            return 0

        return round(
            (completed_topics / total_topics) * 100,
            2
        )


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    roadmap = RoadmapGenerator()

    roadmap.display_roadmap(
        "Data Scientist"
    )

    progress = roadmap.calculate_progress(
        8,
        12
    )

    print(
        "Overall Progress:",
        progress,
        "%"
    )