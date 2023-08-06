# testzli 
A personal practice repo, mainly contains a simple implementation of the uniswap v2 algorithm.

### Use this package
```pip install ```  <br/>
More details on [pypi](https://pypi.org/project/testzli/)

If you need, you can build the package after your modification. <br/>
Navigate to the location of the project<br/>
```cd path/to/testzli ```  <br/>
```python setup.py sdist ``` 

(With yor login and password of pypi.org)Upload it to pypi.org<br/>
```twine upload dist/* ```  <br/>


### Branch Architecture

``master``: protected branch for the PRODUCTION & releases, only the administrator has the right to touch it. 

``develop``: protected branch for integration.

``feature/featureName``: branch for adding new features, should be rebased on develop branch before making pull requests.

``fix/bugName``: branch for bug fixing, should be rebased on master(or develop) branch.


### Release Versioning
Any new changes to master branch have to be validated(reviewed and tested) on the develop branch before being accepted.

A release version, based on a master branch which should be fully validated, should be called ``testzli-v*.*.*``. <br/>
More details here: [releasing and versioning](https://py-pkgs.org/07-releasing-versioning.html)

### Python coding conventions
[PEP8](https://peps.python.org/pep-0008/)



