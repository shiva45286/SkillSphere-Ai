import requests


class GitHubAnalyzer:

    def __init__(self):
        self.base_url = "https://api.github.com/users/"

    # ==========================================
    # Get User Profile
    # ==========================================

    def get_profile(self, username):

        url = self.base_url + username

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return None

    # ==========================================
    # Get Repositories
    # ==========================================

    def get_repositories(self, username):

        url = self.base_url + username + "/repos"

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return []

    # ==========================================
    # Analyze Profile
    # ==========================================

    def analyze_profile(self, username):

        profile = self.get_profile(username)

        if not profile:

            return {
                "error":
                "GitHub User Not Found"
            }

        repos = self.get_repositories(username)

        total_repos = len(repos)

        total_stars = 0

        languages = {}

        top_projects = []

        for repo in repos:

            total_stars += repo["stargazers_count"]

            language = repo["language"]

            if language:

                if language in languages:

                    languages[language] += 1

                else:

                    languages[language] = 1

            top_projects.append({

                "name":
                repo["name"],

                "stars":
                repo["stargazers_count"],

                "url":
                repo["html_url"]

            })

        top_projects = sorted(

            top_projects,

            key=lambda x: x["stars"],

            reverse=True

        )[:5]

        return {

            "name":
            profile.get("name"),

            "username":
            profile.get("login"),

            "bio":
            profile.get("bio"),

            "followers":
            profile.get("followers"),

            "following":
            profile.get("following"),

            "public_repos":
            profile.get("public_repos"),

            "total_stars":
            total_stars,

            "languages":
            languages,

            "top_projects":
            top_projects

        }


# ==========================================
# Testing
# ==========================================

if __name__ == "__main__":

    analyzer = GitHubAnalyzer()

    username = "torvalds"

    result = analyzer.analyze_profile(
        username
    )

    print("\n===== GitHub Analysis =====\n")

    print(
        "Name:",
        result.get("name")
    )

    print(
        "Username:",
        result.get("username")
    )

    print(
        "Followers:",
        result.get("followers")
    )

    print(
        "Public Repositories:",
        result.get("public_repos")
    )

    print(
        "Total Stars:",
        result.get("total_stars")
    )

    print("\nLanguages:")

    for language, count in result[
        "languages"
    ].items():

        print(
            language,
            ":",
            count
        )

    print("\nTop Projects:")

    for project in result[
        "top_projects"
    ]:

        print(
            project["name"],
            "-",
            project["stars"],
            "Stars"
        )