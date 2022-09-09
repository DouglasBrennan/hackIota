import json

from interface import IotaClient

def main():
    client = IotaClient()
    raw_message = client.get_message_by_id('0025b7e4dae3819cf84534095065dc4013542c7964b76d33267873548aa1f4ed')
    message_payloads = client.get_message_payload(raw_message)
    pass

if __name__ == '__main__':
    main()