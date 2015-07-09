import os

from {{cookiecutter.repo_name}}.installed_apps import INTERNAL_APPS

setting_folder = '{{cookiecutter.repo_name}}'
version_file = os.path.join(setting_folder, '_version.py')

try:
    from fabconfig import *
except ImportError as exp:
    pass
