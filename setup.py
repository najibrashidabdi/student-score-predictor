from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        # Remove editable installs
        requirements = [req for req in requirements if req != '-e .']
    return requirements

setup(
    name="student_score_predictor",
    version="1.0.0",
    author="Najib Rashid",
    author_email='cabdinajiibrcabdirashiid@gmail.com',
    description="A machine learning project to predict student scores",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.8',
)
