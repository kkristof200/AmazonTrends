import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'amazontrends'

setuptools.setup(
    name="amazontrends",
    version="0.0.6",
    author="Kristof",
    description="amazontrends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/AmazonTrends",
    packages=setuptools.find_packages(),
    install_requires=["kcu"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)