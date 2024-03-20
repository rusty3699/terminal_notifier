from setuptools import setup, find_packages

setup(
    name="terminal-notifier",  # Replace with your package name
    version="0.1.0",  # Replace with your package version
    author="Anish Tipnis",
    author_email="rusty3699@gmail.com",
    description="A package for notifying users about command execution in the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rusty3699/terminal-notifier",  # Replace with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.6",
    install_requires=[
        "plyer",
        "playsound"
    ]
)