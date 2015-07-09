# django-angular-cookiecutter
CookieCutter Template for Django/Angular applications

Project that sets up MC706's environment for a new project.

### Use
To use, first install cookiecutter:

```
pip install cookiecutter
```

Then use the github options

```
cookiecutter gh:mc706/django-angular-cookiecutter
```

### Tools
This sets up a few tools

* Django
* Django settings for Codeship.com
* Django settings for AWS
* Django S3Boto Storage for AWS Deployment
* Django-Behave
* Coverage Reporting
* NPM
* Bower
* JSHint
* Prospector, Pep8, and Pyflakes
* Xenon Cyclomatic Complexity Tester
* Automatic Changelog updater (based off of git logs)
* Automatic semantic versioning fabric commands
* Multi App Angular Directory Structure
* django-angular-scaffold tool
* Django-compressor configuration setup to include all of your assets in a single concatenated and minified file
* SASS directory setup
* Bower components directory setup.