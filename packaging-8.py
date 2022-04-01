import tomlkit
import datetime
import os
import pathlib
import zoneinfo

now = datetime.datetime.now(tz=zoneinfo.ZoneInfo("UTC"))
prefix=f"{now.year}.{now.month}."
pyproject = pathlib.Path("pyproject.toml")
data = tomlkit.loads(pyproject.read_text())
current = data["project"].get("version", "")
if current.startswith(prefix):
    serial = int(current.split(".")[-1]) + 1
else:
    serial = 0
version = prefix + str(serial)
data["project"]["version"] = version
pyproject.write_text(tomlkit.dumps(data))
