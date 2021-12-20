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

It's also possible pass a list of domains to the app.py by using multiple -d options:
```bash
python3 app.py -d wikipedia.org -d github.com -d google.com
```
And you will see something like this:
```bash
Domain: wikipedia.org - Knowledge
Domain: github.com - Computer/Technology
Domain: google.com - Search Engine
```
## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). Please see the [license file](../LICENSE) for more information.
