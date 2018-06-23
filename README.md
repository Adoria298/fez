# Flask Messenger

A python3 app that uses Flask to create a web messenging app for your local network.

## Branches

- master: for stable releases only.

- login-system: for the original login-system.

- rewrite: for the rewrite (see projects)

## Installation

### Dependencies (for this branch)

- [Python 3]
 (https://www.python.org/downloads)

  - choose the latest version of Python 3 (currently 3.6.5)

- [Flask](http://flask.pocoo.org/)

  - `$ pip install flask`

- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

  - `$ pip install flask-restful`
  
- [Requests](https://http://docs.python-requests.org/en/master/)

  - `$ pip install requests`

- Please ensure you have all dependencies installed, before attempting to use flask-messenger.

- Please note that this project was tested on a [Raspberry Pi](https://www.raspberrypi.org/products/), but it should work on any platform with these dependencies installed.

### Download

- `$ git clone https://www.github.com/Adoria298/flask-messenger.git`

## Usage

- Change directory into the cloned directory (usually flask-messenger)

- `$ python3 app.py`

### For Production

- open app.py in a text editor of your choice,

  - go to the `if __name__ == '__main__':` section (currently starting on line 63),

- remove `debug=True` from the call to `app.run()`, so it looks like this:
    ```python
    if __name__ == '__main__':
        app.run(host='0.0.0.0')
    ```

### For Development

- See CONTRIBUTING.md for development guidelines.

- If you find a bug, please report it on the issue page. If you think that you can fix, it, note this, and follow the contribution guidelines for doing so.

- If you want to suggest a feature, create an issue describing that feature, and attempt to implement it obeying the named guidelines.

## Meta

### License

 Flask Messenger is licensed under the GNU GPL v3 license. For more information, please see [LICENSE](https://github.com/Adoria298/flask-messenger/blob/master/LICENSE).

### Acknowledgements

- The [Raspberry Pi](https://www.raspberrypi.org) people for their ["Build a Python Web Server With Flask"](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask) project, and for the Raspberry Pi itself.

### Versioning

 Flask Messenger uses [Semantic Versioning](https://www.semver.org)
