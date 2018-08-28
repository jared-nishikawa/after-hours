# json

JSON (JavaScript Object Notation: [link](https://json.org)) is a library for encoding basic python objects into ASCII.  (You can *jsonify* things like integers, floats, strings, lists, dictionaries, tuples, and sets... and you *cannot* jsonify functions, custom class instances, modules, and the like).

This process of encoding an object into a structure that can be easily shared (i.e., ASCII) is called *serialization*.

Since lists and dictionaries provide incredible flexbility of data structure, `json` provides a convenient way to serialize that data and share it.

Example:
```python
import json
data = {"orgId": 4185, "numHits": 7923, "timeTaken": 340, "entries": [{"description": "The application svchost.exe invoked the application dllhost.exe", "threatScore": 1}, {"description": "The application GoogleUpdate.exe successfully established a TCP/443 connection to 172.16.163.67", "threatScore": 5}]}

json_str = json.dumps(data)
# This string can then be used later

loaded_data = json.loads(json_str)
```

Or, we could save the json data to a file:
```python
import json
data = {"orgId": 4185, "numHits": 7923, "timeTaken": 340, "entries": [{"description": "The application svchost.exe invoked the application dllhost.exe", "threatScore": 1}, {"description": "The application GoogleUpdate.exe successfully established a TCP/443 connection to 172.16.163.67", "threatScore": 5}]}

with open('data.json', 'w') as f:
    json.dump(data, f)

# This file can be reopened later and loaded into a variable

with open('data.json') as f:
    loaded_data = json.load(f)
```

Note: some markup languages interpret or record these nested dictionaries and lists in a conveniently presentable way.

For example, the data above could be represented like this:
```yaml
orgId: 4185
numHits: 7923
timeTaken: 340
entries:
- description: The application svchost.exe invoked the application dllhost.exe
  threatScore: 1
- description: The application GoogleUpdate.exe successfully established a TCP/443 connection to 172.16.163.67
  threatScore: 5
```
