import sys
from setuptools import setup, find_packages
from pathlib import Path


CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta

def get_long_desc() -> str:
    return (
        (CURRENT_DIR / "README.md").read_text(encoding="utf8")
        + "\n\n"
        #+ (CURRENT_DIR / "CHANGES.md").read_text(encoding="utf8")
    )

setup(
    name="tbc",
    version="v1.0.0-beta",
    #long_description=get_long_desc(),
    long_description_content_type="text/markdown",
    author="Sota Masuda",
    url="https://github.com/sota0121/twitter-bot",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"data": ["config.yml"],},
    install_requires=[
        "click>=8.0.0",
        "tweepy",
        "gspread",
        "google-cloud-storage",
        "pandas",
        "PyYAML"
    ],
    entry_points={
        "console_scripts": [
            "tbc=tbc:main",
        ]
    },
)

