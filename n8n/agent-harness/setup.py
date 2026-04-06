#!/usr/bin/env python3
from setuptools import setup, find_namespace_packages
with open("cli_anything/n8n/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="cli-anything-n8n", version="2.4.5",
    author="Juan Jose Sanchez Bernal", author_email="info@webcomunica.solutions",
    description="CLI harness for n8n workflow automation — 55+ commands. Requires: N8N_BASE_URL, N8N_API_KEY",
    long_description=long_description, long_description_content_type="text/markdown",
    url="https://github.com/HKUDS/CLI-Anything",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    python_requires=">=3.10",
    install_requires=["click>=8.0.0", "requests>=2.28.0", "prompt-toolkit>=3.0.0"],
    entry_points={"console_scripts": ["cli-anything-n8n=cli_anything.n8n.n8n_cli:main"]},
    package_data={"cli_anything.n8n": ["skills/*.md", "README.md"]},
    include_package_data=True, zip_safe=False,
)
