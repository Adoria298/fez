# ![Fez Logo](./fez_logo_by_Luke_Wynne.png) Fez

![GitHub release](https://img.shields.io/github/release/adoria298/flask-messenger.svg?style=plastic) ![GitHub last commit](https://img.shields.io/github/last-commit/adoria298/flask-messenger.svg?style=plastic) ![Github commits (since latest release)](https://img.shields.io/github/commits-since/Adoria298/flask-messenger/latest.svg?style=plastic)

A LAN chat app, built with python3 and flask.

## Branches

- master: for stable releases only.

- login-system: for the original login-system.

- rewrite: for the rewrite (see projects)

## Installation

### Dependencies (for this branch)

- [Python 3](https://www.python.org/downloads)

  - choose the latest version of Python 3. Fez should work on a minimum of 3.5.2.

- [Flask](http://flask.pocoo.org/)

  - `$ pip install flask`

- [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/latest/)

  - `$ pip install flask-restplus`

- [python-dotenv](https://github.com/theskumar/python-dotenv#readme)

  - `$ pip install python-dotenv`

- [markdown](https://python-markdown.github.io)

  - `$ pip install markdown`

- Please ensure you have all dependencies installed, before attempting to use fez.

- Please note that this project was tested on a [Raspberry Pi](https://www.raspberrypi.org/products/), but it should work on any platform with these dependencies installed.

### Download

- `$ git clone https://www.github.com/Adoria298/flask-messenger.git`

## Usage

- Change directory into the cloned directory (usually flask-messenger)

- `$ python3 -m flask run`

### For Production

- open .flaskenv in a text editor of your choice,

  - change `FLASK_ENV` to `production`.
  
  - change `FLASK_DEBUG` to `0`.
  
- run on a production server, following official guidelines.

### For Development

- See CONTRIBUTING.md for development guidelines.

- If you find a bug, please report it on the issue page. If you think that you can fix, it, note this, and follow the contribution guidelines for doing so.

- If you want to suggest a feature, create an issue describing that feature, and attempt to implement it obeying the named guidelines.

- API docs can be found in a running installation at /api .

## Meta

### License

 Fez is licensed under the GNU GPL v3 license. For more information, please see [LICENSE](https://github.com/Adoria298/flask-messenger/blob/master/LICENSE).

### Acknowledgements

- The [Raspberry Pi](https://www.raspberrypi.org) people for their ["Build a Python Web Server With Flask"](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask) project, and for the Raspberry Pi itself.

### Versioning

 Fez uses [Semantic Versioning](https://www.semver.org)

## Roadmap

- Add a CLI messaging utitity.

- Improve the UI of the frontend web app.

- Release v1.0
