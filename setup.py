from setuptools import setup

setup(
    name='labeled_projection_quality',
    version='0.1.0',    
    description='labeled_projection_quality',
    url='https://github.com/barbarabenato/labeled_projection_quality.git',
    author='Bárbara C. Benato',
    author_email='barbara.benato@ic.unicamp.br',
    license='BSD 2-clause',
    packages=['labeled_projection_quality'],
    install_requires=[
                      'csv',
                      'numpy',
                      'sklearn'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)