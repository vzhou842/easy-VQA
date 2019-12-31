import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-vqa",
    version="1.0.beta1",
    author="Victor Zhou",
    author_email="vzhou842@gmail.com",
    description="The official package for the easy-VQA dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/vzhou842/easy-VQA",
    project_urls={
      'Demo': 'https://easy-vqa-demo.victorzhou.com',
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
