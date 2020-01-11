import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geofactory",
    version="0.0.1",
    author="Samuel Cook",
    author_email="rigdoncook@gmail.com",
    description="A simple geojson provider for faker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scook12/geofactory",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)