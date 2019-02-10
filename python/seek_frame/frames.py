"""
Presents a data structure of frames, sorted by phash

Useful for finding N most similar frames
"""

import bisect
from collections import namedtuple

import PIL
import imagehash


LARGE_NUM = float('inf')

Frame = namedtuple('Frame', ['phash_str', 'phash', 'img'])
Similarity = namedtuple('Similarity', ['diff', 'frame'])


class Frames:
    """
    A thin wrapper around a sorted list

    Note that items should be placed in the list all at once,
    when a Frames instance is created. Each insertion after
    the initial sorting is an O(n) operation.
    """

    def __init__(self, paths):
        imgs = (PIL.Image.open(path) for path in paths)
        pairs = ((imagehash.phash(img), img) for img in imgs)
        self._frames = sorted(
            (
                Frame(phash_str=str(pair[0]), phash=pair[0], img=pair[1])
                for pair in pairs
            ),
            key=lambda frame: frame.phash_str
        )
        self._keys = [f.phash_str for f in self._frames]

    def get_n_most_similar(self, img, n=1):
        """
        img may be either a PIL.Image or a path
        """
        if isinstance(img, str):
            img = PIL.Image.open(img)
        phash = imagehash.phash(img)
        phash_str = str(phash)
        low = bisect.bisect_left(self._keys, phash_str)
        high = low + 1
        results = []
        n = min(n, len(self._keys))
        while len(results) < n:
            low_frame = high_frame = None
            low_diff = high_diff = LARGE_NUM
            if low >= 0:
                low_frame = self._frames[low]
                low_diff = abs(phash - low_frame.phash)
            if high < len(self._frames):
                high_frame = self._frames[high]
                high_diff = abs(phash - high_frame.phash)
            print("low: {}, high: {}, low_diff: {}, high_diff: {}".format(
                low, high, low_diff, high_diff))
            if high_diff <= low_diff:
                # prefer high since we are bisecting left
                result_diff = high_diff
                result = high_frame
                high += 1
            if low_diff < high_diff:
                result_diff = low_diff
                result = low_frame
                low -= 1
            to_append = Similarity(diff=result_diff, frame=result)
            results.append(to_append)
        return results
