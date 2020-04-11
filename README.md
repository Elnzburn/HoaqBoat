## Hoaqbot

## Requirements
- Python 3.6
- Cython
- C compiler
- MySQLdb (`mysqlclient`)
- Tornado
- Bcrypt
- Raven

## How to set up Hoaqbot
```
install requirements
```
$ pip install -r requirements.txt
```
then, compile all `*.pyx` files to `*.so` or `*.dll` files using `setup.py` (distutils file)
```
$ python3 setup.py build_ext --inplace
```
finally, run hoaq.py once to create the default config file and edit it
```
$ python3 hoaq.py
...
$ nano config.ini
```
you can run HoaqBoat by typing
```
$ python3 hoaq.py
```

## License
All code in this repository is licensed under the GNU AGPL 3 License.  
See the "LICENSE" file for more information  
This project contains code taken by reference from [miniircd](https://github.com/jrosdahl/miniircd) by Joel Rosdahl.
