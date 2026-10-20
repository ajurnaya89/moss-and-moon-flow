"""
Etsy OAuth2 token refresh helper for Moss & Moon.
"""

import pathlib
import sys

SCRATCH_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
if str(SCRATCH_DIR) not in sys.path:
    sys.path.insert(0, str(SCRATCH_DIR))

from shared.auth import EtsyAuth
from shared.env_utils import read_env

ENV_FILE = pathlib.Path(__file__).resolve().parent.parent / ".env"
_auth = EtsyAuth(ENV_FILE)


def _read_env():
    return read_env(ENV_FILE)


def get_valid_token() -> str:
    return _auth.get_valid_token()


if __name__ == "__main__":
    token = get_valid_token()
    print("Token is valid:", token[:20] + "…")
