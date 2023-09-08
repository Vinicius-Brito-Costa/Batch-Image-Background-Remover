import os
import sys
from pathlib import Path
from rembg import remove, new_session

def loadVariable(var):
    if(os.getenv(var["name"]) != None):
        return os.getenv(var["name"])
    return sys.argv[var["index"]]

target = "/app" + loadVariable({"name": "target", "index": 1})
dest = "/app" + loadVariable({"name": "dest", "index": 2})
extension = loadVariable({"name": "extension", "index": 3})

print("Files expected extension: " + extension)
print("Target directory: " + target)
print("Destiny directory: " + dest)

session = new_session()

for file in Path(target).glob('*.' + extension):
    input_path = str(file)
    output_path = str(Path(dest) / (file.stem + ".out." + extension))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)