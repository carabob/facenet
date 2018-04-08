from distutils.core import setup

setup(
    name='facenet',
    version='0.0.1',
    description="Face recognition with Google's FaceNet deep neural network & TensorFlow",
    url='https://github.com/jonaphin/facenet',
    packages=['facenet'],
    license='MIT',
    author='David Sandberg',
    packageAuthor='Jonathan Lancar',
    install_requires=[
        'tensorflow', 'scipy', 'scikit-learn', 'opencv-python', 
        'h5py', 'matplotlib', 'Pillow', 'requests', 'psutil'
    ]
)