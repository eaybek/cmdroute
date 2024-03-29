import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmdroute",
    version="0.0.3.1",
    author="Erdem Aybek",
    author_email="eaybek@gmail.com",
    description=" ".join(["pythonic cmd utility"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eaybek/cmdroute",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 1 - Planning",
    ],
    python_requires=">=3.6",
)
