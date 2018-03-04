from setuptools import setup, find_packages

setup(
    name='django-sqlformatter',
    version='1.0.3',
    packages=find_packages(),
    url='http://github.com/gabrielhora/django_sqlformatter',
    license='MIT',
    author='Gabriel Hora',
    author_email='gabrielhora@gmail.com',
    description='Better SQL formatter for Django',
    install_requires=['pygments', 'sqlparse'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='django formatter logging',
)
