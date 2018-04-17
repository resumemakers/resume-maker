# Resume maker

A basic command-line resume generator to Python 3

### usage
```
Usage: resume-maker.py [OPTIONS] COMMAND [ARGS]...

  Resume maker.

Options:
  --help  Show this message and exit.

Commands:
  list  List templates
  make  Create a resume
```


#### how to make your resume?
```
python resume-maker make [LANG] [TEMPLATE] [JSON_FILE] [OUTPUT]
```

#### Supported languages
en = English (default)

pt = Portuguese

es = Spanish


#### templates examples
- [basic](examples/basic.pdf) - A very basic resume

- [red](examples/red.pdf) - A red resume - by:[magnvmOpvs](https://github.com/magnvmopvs)

- [simple](examples/simple.pdf) - A simple template - by:[magnvmOpvs](https://github.com/magnvmopvs)


### Json templates
- [simple json](examples/info.json)
- [complex json](examples/complex_info.json)
