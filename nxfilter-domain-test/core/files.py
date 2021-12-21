import csv

def get_file_content(file: str) -> str:
    """
    Get file content.
    """
    try:
        with open(file, 'r') as f:
            content = f.read()

        return content
    except IOError as e:
        print(e)
        print('Exiting...')
        exit(1)

def write_domain_category_csv(file: str, content: list, header = False) -> None:
    """
    Write CSV content to file.
    """
    try:
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            if header:
                writer.writerow(['domain', 'category'])
            for line in content:                
                writer.writerow([line['domain'], line['category'].replace('/', '-').replace(' ', '-')])

    except IOError as e:
        print(e)
        print('Exiting...')
        exit(1)