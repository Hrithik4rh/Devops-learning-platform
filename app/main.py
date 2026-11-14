
from pathlib import Path
from flask import Flask, render_template, abort

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

# Course information
courses = {
    "python": {
        "name": "Python",
        "icon": "🐍",
        "description": "Learn Python programming, scripting and automation.",
        "topics": [
            "Python fundamentals",
            "Variables and data types",
            "Conditions and loops",
            "Functions and modules",
            "Python automation projects"
        ]
    },
    "docker": {
        "name": "Docker",
        "icon": "🐳",
        "description": "Learn how to build and manage containerized applications.",
        "topics": [
            "Introduction to Docker",
            "Docker images and containers",
            "Writing Dockerfiles",
            "Docker networking and volumes",
            "Docker Compose"
        ]
    },
    "kubernetes": {
        "name": "Kubernetes",
        "icon": "☸️",
        "description": "Learn container orchestration and application deployment.",
        "topics": [
            "Kubernetes architecture",
            "Pods and Deployments",
            "Services and Networking",
            "ConfigMaps and Secrets",
            "Persistent Volumes"
        ]
    },
    "aws": {
        "name": "AWS Cloud",
        "icon": "☁️",
        "description": "Learn cloud infrastructure and AWS services.",
        "topics": [
            "Introduction to AWS",
            "EC2 and Security Groups",
            "VPC and Networking",
            "IAM and Permissions",
            "Load Balancers and Auto Scaling"
        ]
    },
    "terraform": {
        "name": "Terraform",
        "icon": "🏗️",
        "description": "Automate cloud infrastructure using Infrastructure as Code.",
        "topics": [
            "Terraform fundamentals",
            "Providers and Resources",
            "Variables and Outputs",
            "State Management",
            "Terraform Modules"
        ]
    },
    "cicd": {
        "name": "CI/CD",
        "icon": "⚙️",
        "description": "Automate software testing, builds and deployments.",
        "topics": [
            "Introduction to CI/CD",
            "Git and GitHub",
            "GitHub Actions",
            "Automated Testing",
            "Deployment Pipelines"
        ]
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/courses/<course_id>")
def course_details(course_id):
    course = courses.get(course_id)

    if course is None:
        abort(404)

    return render_template("course.html", course=course)


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
