from setuptools import setup, find_packages

setup(
    name="bounty_code",
    version="0.1.0",
    description="bounty hunter problem in project",
    author="Nicole Lama",
    author_email="nicolenlama@gmail.com",
    packages=find_packages(include=["bounty_code", "bounty_code*"]),
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
)
