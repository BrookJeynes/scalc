import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="Subnet Calculator",
    version="0.1.0",
    author="Brook Jeynes",
    author_email="",
    description=("A tool to calculate subnets from an IP address"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "subnet-calculator": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "typer==0.6.1",
        "pytest==7.1.2",
        "pandas==1.4.3",
        "tabulate==0.8.9"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "scalc = scalc.cli:app",
        ]
    }
)  
