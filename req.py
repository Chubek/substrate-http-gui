import httpx

def get_results(id: str, method: str):
    print(id, method)
    json_data = {
        "id": id,
        "jsonrpc": "2.0",
        "method": method
    }

    return httpx.post("http://localhost:9933/", json=json_data).json()['result']