import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covidstats", # Replace with your own username
    version="0.0.1",
    author="Truthwatcher",
    description="A python package for using amateur data science to analyize covid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Truthwatcher/CovidStats",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)