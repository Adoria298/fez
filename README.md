# Flask Messenger
A python3 app that uses Flask to create a web messenging app for your local network.

### Branches:
 - master: for stable releases only.
 - login-system: for the original login-system.
 

### Installation:
#### Dependencies (for master branch):
 - [Python 3](https://www.python.org/downloads) 
     - choose the latest version of Python 3 (currently 3.6.5)
 - [Flask](http://flask.pocoo.org/)
    - `$ pip install flask`
 - Please ensure you have all dependencies installed, before attempting to use flask-messenger
 #### Download
 - `$ git clone https://www.github.com/Adoria298/flask-messenger.git`
 
 
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
