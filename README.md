# Flask Messenger
![GitHub release](https://img.shields.io/github/release/adoria298/flask-messenger.svg?style=plastic) ![GitHub last commit](https://img.shields.io/github/last-commit/adoria298/flask-messenger.svg?style=plastic) ![Github commits (since latest release)](https://img.shields.io/github/commits-since/Adoria298/flask-messenger/latest.svg?style=plastic) 

A python3 app that uses Flask to create a web messenging app for your local network.

### Branches:
 - master: for stable releases only.
 - login-system: for the original login-system.
 - rewrite: for the rewrite (see projects)
 

### Installation:
#### Dependencies (for master branch):
 - [Python 3](https://www.python.org/downloads) 
     - choose the latest version of Python 3 (currently 3.6.5)
 - [Flask](http://flask.pocoo.org/)
    - `$ pip install flask`
 - Please ensure you have all dependencies installed, before attempting to use flask-messenger.
 - Please note that this project was tested on a [Raspberry Pi](https://www.raspberrypi.org/products/), but it should work on any platform with these dependencies installed.
 #### Download:
Download from the [latest release](/releases/latest), then extract into a directory. Or, for development:
`git clone https://www.github.com/Adoria298/flask-messenger.git`
 
 ### Usage:
 - Change directory into the cloned directory (flask-messenger)
 - `$ python3 app.py`
 - If using this in a production environment (if you don't want to edit the code), please:
    - open app.py in a text editor of your choice,
    - go to the `if __name__ == '__main__':` section (currently starting on line 63),
    - remove `debug=True` from the call to `app.run()`, so it looks like this:
    ```python
    if __name__ == '__main__':
        app.run(host='0.0.0.0')
    ```
 
 ### Meta:
 #### License:
 Flask Messenger is licensed under the GNU GPL v3 license. For more information, please see [LICENSE](https://github.com/Adoria298/flask-messenger/blob/master/LICENSE).
 #### Acknowledgements:
 - The [Raspberry Pi](https://www.raspberrypi.org) people for their ["Build a Python Web Server With Flask"](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask) project, and for the Raspberry Pi itself.
 #### Versioning: 
 Flask Messenger uses [Semantic Versioning](https://www.semver.org)
 
 ### Roadmap
 - Re write the API, with an internal messaging API, and an external REST API - the [rewrite project](/projects/1)
 - Add a CLI messaging utitity.
 - Improve the UI of the frontend web app.
 - Release v1.0
