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
# wordpress passive only
python3 -m pentets -u https://herby.tv/ -V

# wordpress passive & active
python3 -m pentets -u http://phoenix.etsmtl.ca/ -a

# IBM WebSphere Commerce passive & active
python3 -m pentets -u http://www.scottsofstow.co.uk -a

# OpenCart passive & active
python3 -m pentets -u https://nutrizoo.com -a

# Expression Engine
python3 -m pentets -u https://www.exp-resso.com -a

# Oracle Portal
python3 -m pentets -u http://ville.montreal.qc.ca -a

# Adobe Experience Manager
python3 -m pentets -u http://www.intel.ca -a

# Kentico
python3 -m pentets -u http://etsmtl.ca -a
```
