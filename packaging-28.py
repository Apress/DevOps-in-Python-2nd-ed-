$ pip-compile --extra test > requirements-test.txt
<output snipped>
$ sed -e 's/ *#.*//' -e '/^$/d' requirements.txt
attrs==21.4.0
gunicorn==20.1.0
iniconfig==1.1.1
packaging==21.3
pluggy==1.0.0
py==1.11.0
pyparsing==3.0.6
pytest==6.2.5
toml==0.10.2
