# argparse

The following four lines have crept into dozens of my quick scripts:
```python
import sys
if not sys.argv[1:]:
    sys.exit(f"Usage: {sys.argv[0]} [filename]")
fname = sys.argv[1]
```

(See the [sys](../sys) module for reference.)

This is an easy way to check if the user specified a command line argument to be used as a filename.

Nice for quick scripts, but if you need anything more powerful (for example, using flags) then this method quickly becomes cumbersome.

The `argparse` module is a wonderful tool for creating an argument framework that automatically generates useful help messages for the user.

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
print(args.file)
```

TODO: Finish this article
