# NxFilter Domain Test

## About

This project uses **requests** and **BeautifulSoup** packages to access the NxFilter server and extract category information for a given domain.

## Getting started

To use this project, just clone it and follow these steps:

1. Open project directory
2. Install all dependencies:

```bash
pip install -r requirements.txt
````

2.  Copy .env.example to .env and fill it with your configuration

```bash
cp .env.example .env
```

3. Done. Now you can run the app:
```bash
python3 app.py
```

When you run the app.py, you will see something like this:
```bash
Usage: app.py [OPTIONS]

  Get domain categories using NxFilter.

Options:
  -d, --domain TEXT  Domain to test against NxFilter. You can specify multiple
                     domains by using multiple -d options. E.g. -d example.com
                     -d example.org
                     -f, --file TEXT    File containing domains to test     
                     against NxFilter. One domain per line.
  --help             Show this message and exit.
```

To get a category for a domain, you can run the following command:
```bash
python3 app.py -d wikipedia.org
```
And you will see something like this:
```bash
Domain: wikipedia.org - Knowledge
```

It's also possible pass a list of domains to the app.py by using multiple `-d` options:
```bash
python3 app.py -d wikipedia.org -d github.com -d google.com
```
And you will see something like this:
```bash
Domain: wikipedia.org - Knowledge
Domain: github.com - Computer/Technology
Domain: google.com - Search Engine
```

You can also pass a file containing domains (one per line) to the app.py by using the `-f` option:
```bash
python3 app.py -f domains.txt
```
The output will be the same as the previous example (**multiple `-d` options**). E.g.:
```bash
Domain: wikipedia.org - Knowledge
Domain: github.com - Computer/Technology
Domain: google.com - Search Engine
Domain: gitlab.com - Computer/Technology
Domain: stackoverflow.com - Computer/Technology
Domain: facebook.com - Social Networking
```

By default, `-f` option will generate a file called `classified.csv` stored in the user's download directory. You can define its name and/or path by editing the .env file. Example:
```.env
OUTPUT_CLASSIFIED_CSV="/tmp/domain_category_data.csv"
```


## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). Please see the [license file](../LICENSE) for more information.
