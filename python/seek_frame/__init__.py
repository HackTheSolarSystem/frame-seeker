__version__ = "0.1.0"

import argparse
import logging
import os
import os.path
import sys

logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(name)s: %(message)s")
LOGGER = logging.getLogger(__name__)


def run_test():
    from .frames import Frames
    data_fmt = '/opt/data/{}'
    examples = [data_fmt.format(name) for name in os.listdir('/opt/data')]
    LOGGER.info("Loading %s example CT frames", len(examples))
    frames = Frames(examples)
    LOGGER.info("Example CT frames loaded")
    example = frames._frames[122].img.filename
    LOGGER.info("Comparing frame %s for similarity", example)
    results = frames.get_n_most_similar(example, 1000)
    for i in range(1, len(results)):
        prev = results[i-1]
        curr = results[i]
        assert(prev.diff <= curr.diff)
        LOGGER.debug("phash diff for result %s:", prev.diff)
    LOGGER.info("Min phash diff: %s", results[0].diff)
    LOGGER.info("Max phash diff: %s", results[-1].diff)


def main():
    parser = argparse.ArgumentParser(
        description='Check a test image against CT scan frames')
    parser.add_argument('action', metavar='ACTION', choices=['test'],
                        help='Action to run')
    args = parser.parse_args()
    if args.action == 'test':
        run_test()
