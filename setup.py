from setuptools import setup

setup(
    name='ameliapkg',
    version='0.1.1',    
    description='Python test for amelia',
    url='https://github.com/<<rest of url>>',
    author='Amelia Schroeder',
    author_email='amelia.schroeder@gmail',
    packages=['ameliapkg'],
    install_requires=['python-magic==0.4.27',
                      ],

    classifiers=[
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

