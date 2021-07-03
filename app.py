from modules.peloton import Peloton
import os
import logging
import json


def main():
    peloton = Peloton(os.environ['PELOTON_USERNAME'], os.environ['PELOTON_PASSWORD'])

    peloton.login()
    logger.info(peloton.token)

    print(json.dumps(peloton.workouts(), indent=4))


if __name__ == "__main__":
    # noinspection SpellCheckingInspection
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)-6s %(name)s -> %(message)s')
    logger = logging.getLogger('main.app.py')
    logger.debug("Logging started...")

    main()
