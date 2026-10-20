"""
CLI script to fetch fetch_shop for the shop.
"""

import json
import pathlib
import sys

SCRATCH_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
if str(SCRATCH_DIR) not in sys.path:
    sys.path.insert(0, str(SCRATCH_DIR))

from shared.client import EtsyClient

ENV_FILE = pathlib.Path(__file__).resolve().parent.parent / ".env"
client = EtsyClient(ENV_FILE)


def fetch_shop():
    return client.get_shop()


if __name__ == "__main__":
    data = fetch_shop()
    print(json.dumps(data, indent=2))
    if isinstance(data, list):
        print(f"\nTotal fetched: {len(data)}")
