# terminal-notifier
  A command-line tool that provides multi-channel notifications (desktop, phone, email, popup) based on command outcomes (success, failure, user input required, crash).


## Installation

To install Command Notifier, you can use pip:

```bash
pip todecide
```

# for DEV
- to build and install
 1. python .\setup.py sdist bdist_wheel

 pip uninstall terminal-notifier
 
 pip install dist/terminal_notifier-0.2-py3-none-any.whl --force-reinstall

 to upload on pypi ``` twine upload dist/*