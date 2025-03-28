from setuptools import setup, find_packages

setup(
    name="doc-crawler",
    version="0.1.0",
    description="Documentation Web Crawler that converts HTML to Markdown",
    author="Fillipi Bittencourt",
    author_email="fahbittencourt@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "google-cloud-storage>=2.0.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "doc-crawler=src.cli:run",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)