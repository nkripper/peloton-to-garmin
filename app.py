import json
from peloton import Peloton
import garmin
import os
import logging


def main():
    log.warning("testing warning message")
    peloton = Peloton(os.environ['PELOTON_USERNAME'], os.environ['PELOTON_PASSWORD'])


if __name__ == "__main__":
    log = logging.getLogger("main")
    main()
