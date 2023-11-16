from setuptools import setup, find_packages

__package_name__ = "validations_engine"
__version__ = "2.0.0"
__repository_url__ = "https://github.com/quintoandar/validations-engine"


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = [line for line in f.read().splitlines() if len(line) > 0]

with open("requirements.test.txt") as f:
    test_requirements = [line for line in f.read().splitlines() if len(line) > 0]

setup(
    name=__package_name__,
    description="Engine for creating and running validation suites for general purposes",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=["python", "validations", "validations-engine"],
    version=__version__,
    url=__repository_url__,
    packages=find_packages(include=["validations_engine", "validations_engine.*"]),
    author="QuintoAndar",
    install_requires=requirements,
    python_requires=">=3.7, <4",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
    test_suite="tests",
    tests_require=test_requirements,
)
