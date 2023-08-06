import os
import shutil
import subprocess
from os import path
from setuptools import find_packages
from setuptools import setup
from setuptools.command.sdist import sdist


# copied from https://github.com/simonw/datasette/blob/main/setup.py
# cannot directly import because deps hasn't been installed
def get_version():
    version_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "katatachi", "version.py"
    )
    g = {}
    with open(version_path) as fp:
        exec(fp.read(), g)
    return g["__version__"]


install_requires = [
    "flask==2.1.2",
    "pika==1.0.1",
    "pymongo==3.12.2",
    "flask-cors==3.0.10",
    "flask-jwt-extended==4.4.0",
    "dnspython==1.16.0",
    "jsonschema==3.0.1",
    "apscheduler==3.6.0",
    "sentry-sdk==1.5.1",
    "redis==3.5.3",
    "tzlocal<3.0",
    "Flask-Limiter[redis]==2.6.2",
    # contrib
    "oauthlib==3.1.0",
    "requests<3.0.0",
    "python-twitter==3.5",
]

tests_require = [
    "mongomock==3.23.0",
]

setup_requires = [
    "wheel",
]


WEB_ARTIFACT_PATH = os.path.join("katatachi", "web")


def build_web():
    # check executables which are required to build web
    if not shutil.which("node"):
        raise RuntimeError("node is not found on PATH")
    if not shutil.which("yarn"):
        raise RuntimeError("yarn is not found on PATH")

    # build web
    subprocess.check_call(["yarn", "install"], cwd="web")
    subprocess.check_call(["yarn", "build"], cwd="web")

    # move built artifact
    if os.path.exists(WEB_ARTIFACT_PATH):
        print("removing old web artifact")
        shutil.rmtree(WEB_ARTIFACT_PATH)
    shutil.move(os.path.join("web", "build"), WEB_ARTIFACT_PATH)


class SdistCommand(sdist):
    def run(self):
        build_web()
        sdist.run(self)


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="katatachi",
    version=get_version(),
    description="A Python framework to build web scraping applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k-t-corp/katatachi",
    author="KTachibanaM",
    author_email="whj19931115@gmail.com",
    license_files=("LICENSE",),
    packages=find_packages(),
    # this is important for including web when building wheel
    include_package_data=True,
    # this is important for including web when building wheel
    package_data={"katatachi": ["web"]},
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    test_suite="katatachi_tests",
    cmdclass={"sdist": SdistCommand},
)
