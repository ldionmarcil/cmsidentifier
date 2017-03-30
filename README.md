# LOG515 - PentÉTS

## Installation

```sh
pip3 install setuptools
python3 setup.py develop

# execution des tests
python3 setup.py test

# example d'execution
python3 -m pentets -u https://herby.tv/
python3 -m pentets -u http://phoenix.etsmtl.ca/ -a
```

## Manual testing examples

```sh
python3 -m pentets -u https://herby.tv/ -V
# [2017-03-20 13:45:56,647 DEBUG] Loading rule data
# [2017-03-20 13:45:58,788 DEBUG] Unpacking YAML documents
# [2017-03-20 13:45:58,793 DEBUG] Launching passive rules for Wordpress
# [2017-03-20 13:45:58,794 INFO] Match for Wordpress (https://wordpress.com/)

python3 -m pentets -u http://phoenix.etsmtl.ca/ -a -V
# [2017-03-21 21:42:35,729 INFO] Match for Wordpress (https://wordpress.com/)
# [2017-03-21 21:42:36,114 INFO] Active /readme.html match
# [2017-03-21 21:42:36,114 INFO] Exracted: 4.3.9
# [2017-03-21 21:42:36,567 INFO] Active /license.txt match
# [2017-03-21 21:42:36,567 INFO] Exracted: Copyright 2017 by the contributors
```
