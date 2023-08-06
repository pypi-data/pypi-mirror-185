# Scriptum
A command line utility for storing, documenting, and executing your project's scripts. 

## Documentation
See documentation [here](http://gadhagod.github.io/scriptum).

## A simple use case
With `scriptum`, you can easily configure scripts into a repo or directory, by placing defining them in a configuration file. Here is an example of a configuration file:
```jsonc
/*
  Scripts for my project!
*/
{
    "serve": "python3 server.py",           // runs the server
    "test": {                               // tests my project
        "permissions": {                    // configures the permissions
            "set": "chmod 777 main.py",     // makes the executable public
        },
        "run": "./main.py $1",              // runs the executable
        "checks": ["mypy **/*.py", "python3 tests/main.py"]       // runs the tests
    },
    "package": {                                                  // distribution
        "build": "python3 setup.py sdist bdist_wheel",            // prepares for release
        "publish": "twine upload --repository pypi dist/*"        // publishes the package
    },
    "deps": {                                                     // dependency management
        "install": ["pip3 install reqs.txt", "brew install pkg"], // installs dependencies
        "list": "cat reqs.txt",                                   // lists dependencies
        "resolve": "python3 -m pip freeze > main/reqs.txt"        // updates the dependency list
    },
    "docs": {                               // manage documentation
        "install": "npm i -g docsify",      // installs docs dependencies
        "serve": "docsify serve",           // runs the server
        "open": "open http://localhost:3000"// opens the preview
    }
}
```
You can now execute any of these scripts conviniently with the scriptum CLI (`scr`):
```bash
scr <script category> <script> <args>
```

So if you wanted to run the scripts, you can enter the them into the command line like so:

```bash
scr help                    # open index.html
scr deps install            # python3 -m pip install requirements.txt
scr deps resolve            # python3 -m pip freeze > requirements.txt
scr test permissions set    # chmod 777 main.py
scr test run [[production]] # ./main.py 'production'
scr test checks             # mypy **/*.py and ./tests/main.py
```

If you check the configuration file into you repo, your team can now run these scripts with ease.

## Features
* Highly configurable
* Cross-platform support
* Supports dependency management from multiple sources (NPM, pip, etc.)
* Script categories
* JSON configuration support for comments and documentation
* Supports command lists that stop on fail