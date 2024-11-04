import pathlib
import datetime

folder = "public"
filename = "index.html"

path = pathlib.Path(folder)
if not path.exists():
    path.mkdir()

now = datetime.datetime.now()

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>My Website create by Python</title>
</head>
<body>
    <h1>Hello, World!</h1>
    Published: {now}
</body>
</html>
"""

with open(path.joinpath(filename), "w") as file:
    file.write(html)
