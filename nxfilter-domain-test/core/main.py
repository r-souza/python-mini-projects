import config.app_config as config
import requests
from bs4 import BeautifulSoup

def login() -> requests.Session:
    """
    Login to NxFilter.
    """
    with requests.Session() as s:
        login_data = {
            'actionFlag' : 'login',
            'uname': config.NXFILTER_USERNAME,
            'passwd': config.NXFILTER_PASSWORD,
        }
        s.post(config.NXFILTER_LOGIN_URI, data=login_data)

        return s

def domain_test(domain: str, s: requests.Session) -> requests.Response:
    """
    Get response of domain test.
    """
    domain_data = {
        'actionFlag': 'update',        
        'domain': domain,
    }

    return s.post(config.NXFILTER_CATEGORY_URI, data=domain_data)

def parse_sandwatch_gui(soup: BeautifulSoup) -> str:
    """
    Parse Sandwatch GUI.
    """
    result_div = soup.find_all('div', attrs={"class": 'form-group col-lg-12'})[0]
    result = result_div.text.strip()

    return result

def parse_default_gui(soup: BeautifulSoup) -> str:
    """
    Parse Default GUI.
    """
    result_table = soup.find_all('table', attrs={"class": 'view'})[1]    
    result = result_table.find_all('td')[1].text.strip()

    return result

def get_category(domain: str, s = login()) -> str:
    """
    Get domain category using NxFilter.
    """

    response = domain_test(domain, s)
    soup = BeautifulSoup(response.text, 'html.parser')

    if config.NXFILTER_GUI == 'sandwatch':
        result = parse_sandwatch_gui(soup)
    else:
        result = parse_default_gui(soup)

    print('Domain: {} - {}'.format(domain, result))
    
    return result

def get_categories(domains: set) -> list:
    """
    Get domain categories using NxFilter.
    """
    s = login()

    results = []
    for domain in domains:
        result = {
            'domain': domain,
            'category': get_category(domain, s)
        }
        results.append(result)

    return results