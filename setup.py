from setuptools import setup, find_packages

def build_native(spec):
    build = spec.add_external_build(
        cmd=['cargo', 'build', '--release'],
        path='./rust'
    )
    spec.add_cffi_module(
       module_path='flaskrust._native',
       dylib=lambda: build.find_dylib('flaskrust', in_path='target/release'),
       header_filename=lambda: build.find_header('flask-rust.h', in_path="target"),
       rtld_flags=['NOW', 'NODELETE']
    )


setup(
    name='flaskrust',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'milksnake',
    ],
    install_requires=[
        'milksnake',
    ],
    milksnake_tasks=[
        build_native,
    ]
)
