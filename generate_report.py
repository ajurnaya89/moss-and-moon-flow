"""
CEO Report Generator for Moss & Moon Etsy shop.
"""

import pathlib
import sys

SCRATCH_DIR = pathlib.Path(__file__).resolve().parent.parent
if str(SCRATCH_DIR) not in sys.path:
    sys.path.insert(0, str(SCRATCH_DIR))

from shared.report_engine import CEOReportEngine

ENV_FILE = pathlib.Path(__file__).resolve().parent / ".env"
REPORTS_DIR = pathlib.Path(__file__).resolve().parent / "reports"


def generate_report() -> pathlib.Path:
    engine = CEOReportEngine(
        env_path=ENV_FILE,
        reports_dir=REPORTS_DIR,
        default_shop_name="Moss & Moon (mossandmoonflow)",
        default_shop_url="https://www.etsy.com/shop/mossandmoonflow",
    )
    return engine.generate()


if __name__ == "__main__":
    generate_report()
