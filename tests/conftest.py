import json
import tempfile

import pytest

DEMO_CONFIG = {
    "office": [
        "192.1.1.1",
    ],
    "kitchen": ["192.1.1.2", "192.1.1.3"],
    "bedroom": ["192.1.1.4", "192.1.1.5"],
}


@pytest.fixture
def cfg():
    with tempfile.NamedTemporaryFile(mode="w+") as cfg:
        cfg.write(json.dumps(DEMO_CONFIG))
        cfg.flush()
        yield cfg.name
    return
