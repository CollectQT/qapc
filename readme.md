# QAPCollective's New Website

install

```
echo "3.4.3" > .python-version
virtualenv --python=python3.4 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

reload data

```
python lib/IWC_integration.py
```

run server

```
python main.py
```
