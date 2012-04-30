from distutils.core import setup
import os

package_data = []
BASE_DIR = os.path.dirname(__file__)
walk_generator = os.walk(os.path.join(BASE_DIR, "project_template"))
paths_and_files = [(paths, files) for paths, dirs, files in walk_generator]
for path, files in paths_and_files:
    prefix = path[path.find("project_template") + len("project_template/"):]
    if files:
        package_data.append(os.path.join(prefix, "*.*"))

setup(
    name="armstrong.templates.tutorial",
    version="1.0.0",
    description="The tutorial project for Armstrong",
    long_description=open("README.rst").read(),
    author='Texas Tribune & Bay Citizen',
    author_email='dev@armstrongcms.org',
    packages=[
        "armstrong.templates.tutorial",
    ],
    package_dir={
        "armstrong.templates.tutorial": "project_template",
    },
    package_data={
        "armstrong.templates.tutorial": package_data,
    },
    namespace_packages=[
        "armstrong",
        "armstrong.templates",
        "armstrong.templates.tutorial",
    ],
    entry_points={
        "armstrong.templates": [
            "tutorial = armstrong.templates.tutorial",
        ],
    },
)
