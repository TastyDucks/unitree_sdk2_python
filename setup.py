from setuptools import setup, find_packages

setup(name='unitree_sdk2py',
      version='1.0.1',
      author='UnitreeRobotics',
      author_email='unitree@unitree.com',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      license="BSD-3-Clause",
      packages=find_packages(include=['unitree_sdk2py','unitree_sdk2py.*']),
      description='Unitree robot sdk version 2 for python',
      project_urls={
            "Source Code": "https://github.com/unitreerobotics/unitree_sdk2_python",
      },
      package_data={"unitree_sdk2py": ["utils/lib/*.so"]},
      include_package_data=True,
      python_requires='>=3.8',
      install_requires=[
            "numpy",
            "opencv-python",
      ],
      )
