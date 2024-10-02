from setuptools import find_packages, setup

def get_requirements()->list[str]:
    """Get the list of required packages

    """
    requirement_list = list[str] = []
    return requirement_list




setup(
name="Live-Sensor",
version= "0.0.1",
author="Abdur RAHMAN",
author_email= "abdulrehman100198@gmail.com",
packages=find_packages(),
install_requires=get_requirements()

)