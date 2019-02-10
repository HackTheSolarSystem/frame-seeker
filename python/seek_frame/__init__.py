import os
import os.path

data_fmt = '/opt/data/{}'

examples = [data_fmt.format(name) for name in os.listdir('/opt/data')]

def run_test():
    from .frames import Frames
    frames = Frames(examples)
    example = frames._frames[122].img.filename
    results = frames.get_n_most_similar(example, 1000)
    for i in range(1, len(results)):
        prev = results[i-1]
        curr = results[i]
        assert(prev.diff <= curr.diff)

# examples = [
#     pkg_resources.resource_filename('seek_frame', data_fmt.format(name))
#     for name in pkg_resources.resource_listdir('seek_frame', 'data')
# ]

# example_dir = pkg_resources.resource_filename('frame_finder', 'examples/')
# example = pkg_resources.resource_filename('frame_finder', 'data/Sem2_YZ_8a_0172.tif')

# examples = pkg_resources.resource_listdir('frame_finder', 'data')


__version__ = "0.1.0"


def run():
    print("Hello Docker")
