"""Module containing main function"""
from pprint import pprint

import iota_client
import os
import hashlib

def main():
    """Main function"""
    # create a client with a node
    client = iota_client.Client(
        nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])
    client.get_info()

    pprint(client.get_info())

if __name__ == '__main__':
    main()
