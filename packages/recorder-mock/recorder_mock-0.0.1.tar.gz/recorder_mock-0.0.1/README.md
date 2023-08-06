`recorder-mock` allows to record interactions on patched Python objects and repeat the interactions when the patched object is no longer available.

## Installation

```bash
pip install recorder-mock
```

## Usage
```
from recorder_mock import recorder_patch

@recorder_patch("httpx")
class ExampleTestCase(unittest.TestCase):
    def test_get_example_com_content():
        client = httpx.client()
        resp = client.get("example.com")
        return resp.content
```

First execution of the tests will hit the Internet and record the interactions.
Second test run won't hit the internet, recorded interactions will be repeated instead.


## Related projects
This tool was inspired by:
- `patch` and `MagicMock` from [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) standard library package
- [VCR.py](https://vcrpy.readthedocs.io/en/latest/index.html) package
