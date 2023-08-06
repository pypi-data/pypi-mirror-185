# Rebapy

Reba Python Client

## Example

```python
from rebapy import RelayClient
client = RelayClient("0xe28a707663e73e2502d835a5b456af43425196013c6e1218cdf76d43e975dc46")
while True:

    tx = client.read_tx()
    print(tx.as_dict())

```
