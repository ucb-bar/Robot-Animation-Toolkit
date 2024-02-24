import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unrealbridge",
    version="2024.2.19",
    author="Uncertainty.",
    author_email="t_k_233@outlook.email",
    description="Unreal Python TCP Bridge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ucb-bar/Robot-Animation-Toolkit",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
