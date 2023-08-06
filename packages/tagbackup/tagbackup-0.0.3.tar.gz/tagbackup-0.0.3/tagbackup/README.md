https://typer.tiangolo.com/tutorial/package/

# update version in pypyroject.toml

rm dist/\*

poetry install
poetry build

twine upload dist/\* -u joncombe

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
