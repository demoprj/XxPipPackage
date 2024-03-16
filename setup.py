import setuptools

# with open("README.md", "r", encoding="utf-8") as file:
#     long_description = file.read()

setuptools.setup(
    name="XxPipPackage",
    version="0.0.1",
    author="tokoyi",
    author_email="tokoyi@gmail.com",
    description="A demo for Python pip package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    long_description = 'A demo for Python pip package ...',
    url="https://github.com/demoprj/XxPipPackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    python_requires='>=3'
)