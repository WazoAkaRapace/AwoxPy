from distutils.core import setup

setup(
    name='awoxpy',
    packages=['awoxpy'],
    version='0.8',
    description='A library that help you control Awox Smartlight with BTLE protocol',
    author='Mika Benoit',
    author_email='mika.benoit@gmail.com',
    url='https://github.com/Rapace21/AwoxPy',
    download_url='https://github.com/Rapace21/AwoxPy/archive/0.8.tar.gz',
    keywords=['awox', 'bluetooth', 'lib'],
    classifiers=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'bluepy',
    ],
)

