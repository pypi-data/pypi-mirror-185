https://typer.tiangolo.com/tutorial/package/

# update version in pypyroject.toml

poetry install
poetry build

rm dist/_
twine upload dist/_ -u joncombe

---

on a server

(sudo apt-get install python3-pip)
python -m pip install tagbackup

---

Todo:

- Large files should be upload in multipart
- Improve status: show linked / unlinked, get device name
- Proper help page: a main one and one per command
- Help and errors should link to the docs
- Better error handling
