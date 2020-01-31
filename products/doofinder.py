import requests
import time

from itertools import islice

API_KEY = 'eu1-627d8304aa910e7dcee0432525ea52a73d94aea6'
TOKEN = '627d8304aa910e7dcee0432525ea52a73d94aea6'
HASH_ID = '16ba07e99ddcb00ec317c09928161b7b'
TYPE = 'product'
URL = 'https://eu1-api.doofinder.com/v1'
HEADERS = {'Authorization': 'Token %s' % TOKEN}


# Returns a list of the SearchEngines of the user
def list_search_engines():
    r_url = URL + '/searchengines'
    r = requests.get(url=r_url, headers=HEADERS)

    print(r.json())


# Returns details of a single SearchEngine
def get_search_engine():
    r_url = URL + '/searchengines/%s' % HASH_ID
    r = requests.get(url=r_url, headers=HEADERS)

    print(r.json())


# Returns a list of the types defined for the search engine
def list_types():
    r_url = URL + '/%s/types' % HASH_ID
    r = requests.get(url=r_url, headers=HEADERS)

    print(r.json())


# Returns information about a single type
def get_type():
    r_url = URL + '/%s/types/product' % HASH_ID
    r = requests.get(url=r_url, headers=HEADERS)

    print(r.json())


# Returns information about a single item
def get_item(item_id):
    r_url = URL + '/%s/items/product/%s' % (HASH_ID, item_id)
    r = requests.get(url=r_url, headers=HEADERS)

    print(r.json())


# Creates a new item. The response is a representation of the recently created item.
# Notice the dynamically, read-only url field that points to the item's resource location.
def create_item(item):
    r_url = URL + '/%s/items/product' % HASH_ID
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    r = requests.post(url=r_url, headers=r_headers, json=item)

    print(r.json())


# You can create up to 100 Items in a single API call. Just upload a list of objects.
# The response is, as expected, a representation of the recently created list of items.
def create_items_in_bulk(items):
    r_url = URL + '/%s/items/product' % HASH_ID
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    # Replace iid with id
    for item in items:
        item['id'] = item['iid']
        try:
            del item['_id']
        except KeyError:
            pass  # Item has been processed previously => _id is not in item anymore

    # Create items in chunks of size 100
    for chunk in chunks(items, 100):
        r = requests.post(url=r_url, headers=r_headers, json=chunk)

        # Limit of 2 requests per seconds
        while r.status_code == 429:
            # Sleep 1 second if timeout limit is reached
            time.sleep(1)
            # Retry after 1 second
            r = requests.post(url=r_url, headers=r_headers, json=chunk)

        print(r.json())


# Updates an existing item. If the provided {item_id} doesn't exist, a new item will be created
def update_or_create_item(item):
    r_url = URL + '/%s/items/product/%s' % (HASH_ID, item['iid'])
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    r = requests.put(url=r_url, headers=r_headers, json=item)

    print(r.json())


# Updates or creates several items in one REST operation.
# You have to provide a list of items, and every item has to have the id attribute.
# If, for any of the items in the list, there is an already indexed item with the same id attribute,
# it will be replaced with the uploaded item.
# If not, a new item will be created.
def update_or_create_items_in_bulk(items):
    r_url = URL + '/%s/items/product' % HASH_ID
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    r = requests.put(url=r_url, headers=r_headers, json=items)

    print(r.json())


# Update or create only some attributes of an existing item.
# If the provided {item_id} doesn't exist, no action is performed.
def partially_update_item(item):
    r_url = URL + '/%s/items/product/%s' % (HASH_ID, item['iid'])
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    r = requests.patch(url=r_url, headers=r_headers, json=item)

    print(r.json())


# Partially updates item's attributes in one REST operation.
# You have to provide a list of objects containing the attributes to be modified or added.
# The id attribute is mandatory.
# Only the uploaded attributes are modifed for every item.
# Every other attribute an item may have beside the ones in the PATCH operation is kept
def partially_update_items_in_bulk(items):
    r_url = URL + '/%s/items/product' % HASH_ID
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    r = requests.patch(url=r_url, headers=r_headers, json=items)

    print(r.json())


# Delete an existing item
def delete_item(item):
    r_url = URL + '/%s/items/product/%s' % (HASH_ID, item['iid'])
    r = requests.delete(url=r_url, headers=HEADERS)

    print(r.json())


# You can also delete up to 100 Items in a single API call.
# You must provide a list of objects each containing the id attribute.
# The response contains two lists of ids: those that could be successfully deleted and those that failed.
def delete_items_in_bulk(items):
    r_url = URL + '/%s/items/product' % HASH_ID
    r_headers = HEADERS
    r_headers['content-type'] = 'application/json'

    item_ids = []

    # Replace iid with id
    for item in items:
        item_id = {'id': item['iid']}
        item_ids.append(item_id)

    # Create items in chunks of size 100
    for chunk in chunks(item_ids, 100):
        r = requests.delete(url=r_url, headers=r_headers, json=chunk)

        # Limit of 2 requests per seconds
        while r.status_code == 429:
            # Sleep 1 second if timeout limit is reached
            time.sleep(1)
            # Retry after 1 second
            r = requests.delete(url=r_url, headers=r_headers, json=chunk)

        print(r.json())


# Generator that yields chunks of size n
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
