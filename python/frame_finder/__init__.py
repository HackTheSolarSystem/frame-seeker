import pkg_resources

example = pkg_resources.resource_filename('frame_finder', 'examples/example_0000.tif')

__version__ = "0.1.0"


def run():
    print("Hello Docker")
