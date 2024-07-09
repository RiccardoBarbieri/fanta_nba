```bash
# installa venv
python3 -m pip install --user virtualenv
# crea venv in locale, non modificare nome nba_venv per gitignore
python3 -m venv nba_venv 
# attiva venv
source ./nba_venv/bin/activate
# installa requirements
python3 -m pip install -r venv_req.txt
```