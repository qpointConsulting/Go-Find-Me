import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GoFindMe-pkg-qpointconsulting", # Replace with your own username
    version="0.0.1",
    author="Bryan Galbraith, Mikah Hoffman",
    author_email="qpoint@shaw.ca",
    description="A small app to locate usernames on various social media sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qpointconsulting/Go-Find-Me",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
