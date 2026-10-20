"""
Etsy OAuth2 PKCE authorization flow for Moss & Moon.
"""

import pathlib
import sys

# Add shared module to path
SCRATCH_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
if str(SCRATCH_DIR) not in sys.path:
    sys.path.insert(0, str(SCRATCH_DIR))

from shared.auth import EtsyAuth

if __name__ == "__main__":
    env_file = pathlib.Path(__file__).resolve().parent.parent / ".env"
    auth = EtsyAuth(env_file)
    auth.run_oauth_flow()
