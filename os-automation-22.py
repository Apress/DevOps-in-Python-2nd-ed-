>>> here = pathlib.Path.cwd()
>>> poem = here / "poem.txt"
>>> poem.write_text("""\
... Roses are red,
... Their leave are green.
... Python is awesome,
... and pathlib is keen
... """)
77
>>> import os
>>> subprocess.run(["grep", "een$", os.fspath(poem)])
and pathlib is keen
