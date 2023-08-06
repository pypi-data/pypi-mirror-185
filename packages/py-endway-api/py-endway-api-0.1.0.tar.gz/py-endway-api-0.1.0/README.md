# EndWay Api
Library for convenient work with the EndWay forum

### Installation
```
pip install py-endway-api
```

### Get started
How to start working with the library

```Python
from py-endway-api import EndWayApi

# Instantiate a EndWayApi object
ewApi = EndWayApi("...example xf_user...")

# call the method of sending a message to the thread
result = ewApi.add_reply(1, "Hello")
print(result)
```