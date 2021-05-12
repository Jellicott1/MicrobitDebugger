# MicrobitDebugger
Re-implementation of microbit python package that pushes outputs to stdout rather than the microbit to enable easy debugging.

## Installation
To use this tool in your microbit project, download the project as a zipfile and extract the MicrobitDebugger.py file into the same directory as your python script. Then replace the `from microbit import *` line with `from MicrobitDebugger import *` in your script. 

Alternatively, if you want to be able to easily change between using the debugger and standard versions of the microbit package, you can use a DEBUG_MODE switch as shown below. This should replace your default microbit import statement.

```python
DEBUG_MODE = True

if DEBUG_MODE:
    from MicrobitDebugger import *
else:
    from microbit import *
```

## Notes
This package is currently under development and is regularly updated to add compatability with more microbit functions. At this stage it is recommended to check back frequently for new versions.

Feedback is also encouraged. If you encounter a bug or unimplemented method that you would like, please raise an issue [here](https://github.com/Jellicott1/MicrobitDebugger/issues).
