import requests
import decode
from req import get_results


def test_decode():
    data = get_results("1", "state_getMetadata")    

    print(decode.decode_event_data(data))


test_decode()