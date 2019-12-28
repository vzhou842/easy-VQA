import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-vqa",
    version="0.0.1",
    author="Victor Zhou",
    author_email="vzhou842@gmail.com",
    description="A wrapper for the easy-VQA dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/vzhou842/easy-VQA",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
