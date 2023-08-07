from setuptools import setup, find_namespace_packages

setup(
    name='qrdet',
    version='1.1',
    packages=find_namespace_packages(),
    # expose qreader.py as the unique module
    py_modules=['QRDetector'],
    url='https://github.com/Eric-Canas/qrdet',
    license='MIT',
    author='Eric Canas',
    author_email='elcorreodeharu@gmail.com',
    description='Robust QR Detector based on YOLOv7',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
        'yolov7-package',
    ],
    # To include the __yolo_v3_qr_detector weights in the package, we need to add the following line:
    include_package_data=True,
    # To include the __yolo_v3_qr_detector weights in the package, we need to add the following line:
    data_files=[('.yolov7_qrdet',
                 ['.yolov7_qrdet/qrdet-yolov7-tiny.pt'])],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Multimedia :: Graphics',
        'Typing :: Typed',
    ],
)
