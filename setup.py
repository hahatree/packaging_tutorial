import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packaging_tutorial", # Replace with your own username
    version="1.0.0",
    author="Mark",
    author_email="NT87189@cathaybk.com.tw",
    description="Django網頁框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hahatree/packaging_tutorial.git",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)