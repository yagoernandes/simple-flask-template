from setuptools import setup, find_packages

setup(
	name='boilerplate_flask',
	version='0.0.1',
	url='https://github.com/yagoernandes',
	author='Yago Ernandes',
	author_email='yago.700+contato@gmail.com',
	description='Just a simple app',
	install_requires=['flask'],
	packages=find_packages(exclude=['tests'])
)