import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="renard",
    version="0.0.1",
    author="Denisov Artem",
    author_email="arden2545@gmail.com",
    description="File renaming tool written in Python",
    url="https://github.com/Arden97/renard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "renard = renard:main.main",
        ]
    },
    install_requires=[
        'click',
    ],
    python_requires='>=3.6',
)