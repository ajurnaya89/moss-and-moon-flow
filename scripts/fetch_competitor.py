"""
CLI script to inspect competitor shop data.
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


def analyse_shop(shop_name: str):
    return client.get_competitor_analysis(shop_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/fetch_competitor.py <shop_name> [shop_name2 ...]")
        sys.exit(1)

    results = {name: analyse_shop(name) for name in sys.argv[1:]}
    print(json.dumps(results, indent=2))
