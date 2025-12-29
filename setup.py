from setuptools import find_packages, setup

setup(
    name="docx_meditation_form",
    version="0.0.1",
    description="Generate court-ready DOCX mediation application forms",
    author="Harsh",
    packages=find_packages(),
    install_requires=[
        "python-docx",
        "google-api-python-client",
        "google-auth",
        "google-auth-oauthlib",
    ],
    python_requires=">=3.9",
)
