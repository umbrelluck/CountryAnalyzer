from setuptools import find_packages, setup

setup(name="CountryAnalyzer",
      version="1.0",
      author='Yaroslav Borys',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['copy',
                        'datetime',
                        'json',
                        'sys',
                        'urllib.request',
                        'webbrowser'],
      )
