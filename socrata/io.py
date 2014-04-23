
def get(warehouse, url):
    if url in warehouse:
        output = warehouse[url]
    else:
        try:
            response = requests.get(url)
        except Exception as error:
            output = error, response
            warehouse[url] = output
    return output

