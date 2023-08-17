from setuptools import setup, find_packages

setup(
    name="vocabulary",
    version="0.1",
    description="This is a vocabulary scraper for definitions and synonyms",
    packages=find_packages(),
    install_requires=[
        "bs4",
        "curl_cffi",
    ],
)