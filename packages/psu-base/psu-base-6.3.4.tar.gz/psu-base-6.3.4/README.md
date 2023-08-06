# PSU-Base

Reusable Django app specifically for PSU's custom-built web applications.  
It encapsulates the common functionality that we would otherwise need to program into each application we build.
Features include:
-  PSU Single Sign-On (SSO)
-  Authentication and authorization features
-  Feature toggles
-  Template tags for our static content server

## Quick Start
### Dependencies
The following dependencies may be REQUIRED in your system:
- `libpq-dev`
    ```sh
    sudo apt install libpq-dev
    ```

### Start a PSU Base Enabled Project
```sh
django-admin.py startproject \ 
--template=*some-path-to*/psu-base-template.zip \
--extension=py,md,env \
my_project_name
```

### Configuring Your App
After starting a new project from the custom template (above):
1. `cd my_project_name`
1. `pip install -r requirements.txt`
1. Review/Update the application metadata in settings.py
1. Run migrations: `python manage.py migrate`

If you have the PSU Secret Key file, your site was configured to access Finti's test server. 
This will need to be overwritten in local_settings.py eventually. If you do not have the 
PSU Secret Key file, you'll need to set these prior to running your app.


## Usage
Usage of the psu-base app is documented in 
[Confluence](https://portlandstate.atlassian.net/wiki/spaces/WDT/pages/713162905/Reusable+Django+Apps+The+Django+PSU+Plugin).

As of version 4.2, css files and other project-specific static assets are automatically
hosted on the AWS server along side the application. Projects created prior to 4.2 will need
to re-copy their `.ebextension` and `.platform` directories from the latest project template to
take advantage of this feature.

## For Developers
The version number must be updated for every PyPi release.
The version number is in `psu_base/__init__.py`

### Document Changes
Record every change in [docs/CHANGELOG.txt](docs/CHANGELOG.txt)
Document new features or significant changes to existing features in [Confluence](https://portlandstate.atlassian.net/wiki/spaces/WDT/pages/713162905/Reusable+Django+Apps+The+Django+PSU+Plugin).

### Publishing to PyPi
1. Create accounts on [PyPi](https://pypi.org/account/register/) and [Test PyPi](https://test.pypi.org/account/register/)
1. Create `~/.pypirc`
    ```
    [distutils]
    index-servers=
        pypi
        testpypi
    
    [testpypi]
    repository: https://test.pypi.org/legacy/
    username: mikegostomski
    password: pa$$w0rd
    
    [pypi]
    username: mikegostomski
    password: pa$$w0rd
    ```
1. Ask an existing developer to add you as a collaborator - [test](https://test.pypi.org/manage/project/psu-base/collaboration/) and/or [prod](https://pypi.org/manage/project/psu-base/collaboration/)
1. `python setup.py sdist bdist_wheel --universal`
1. `twine upload --repository testpypi dist/*`
1. `twine upload dist/*`
1. Tag the release in Git.  Don't forget to push the tag!
Example:
```shell script
git tag 0.1.2
git push origin 0.1.2 
```