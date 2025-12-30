from setuptools import find_packages, setup

setup(
    name="docx_meditation_form",
    version="0.0.3",
    description="Generate court-ready DOCX mediation application forms",
    author="Harsh",
    author_email="harshhbtmuz@users.noreply.github.com",
    url="https://harshhbt.github.io/docx_meditation_form/",
    license="Unlicense",
    packages=find_packages(),
    install_requires=[
        "python-docx",
        "google-api-python-client",
        "google-auth",
        "google-auth-oauthlib",
    ],
    python_requires=">=3.9",
)
