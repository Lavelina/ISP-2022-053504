from setuptools import setup

setup(
    name='serializer',
    version='1.0',
    packages=['test', 'sourses', 'sourses.packer', 'sourses.FactoryMethod', 'sourses.SerializerJson',
              'sourses.SerializerToml', 'sourses.SerializerYaml'],
    url='',
    license='',
    author='avelina',
    author_email='7660990@gmail.com',
    install_requires=['PyYaml == 6.0',
                      'pytoml == 0.1.21'],
    description='Lab2_ISP_cooltask',
    entry_points={
            'console_scripts': [
                'redump = sourses.redump:main'
            ]}
)
