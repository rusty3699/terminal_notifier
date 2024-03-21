from setuptools import setup, find_packages

setup(
    name="terminal_notifier",  # Replace with your package name
    version="0.3",  # Replace with your package version
    author="Anish Tipnis",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "plyer",
        "playsound"
    ],
   

    include_package_data=True,  # Include package data specified by MANIFEST.in
    package_data={
        "": ["*.mp3"],  # Include all mp3 files in the package
    }
)
