## seek_frames

### Addressing [3D and 2D Bubbles In Rock (subchallenge)][challenge]

Please note: this project focused entirely on solving the included
subchallenge, quoted below:

> Find the frame in the tomography - what plane in the full tomography
> volume best matches the BSE map of a flat polished surface cut from
> the original rock?

### Created by Team Hashalot

* Chuck Bassett [chucksmash][profile]

### Solution Description

I created a small software library for correlating BSE maps to frames
from a computed tomography scan. The library uses a technique known as
perceptual hashing, or phashing, (editor's note: not p-hacking) to
compute a measure of visual similarity.

Cryptographically strong hashing algorithms exhibit a property known
as the avalanche effect, where a small change in the input value
results in a large change in the hashed output. For general
applications, this is a desirable property.

Perceptual hashes are a family of hash algorithms where a small change
in the input value only results in a small change in the hashed
output. Because of this, comparing the output of a phash function
applied to image data is useful for quantifying the degree of
similarity between images and also for quickly finding similar images.

This solution is written in Python 3.7 and uses the `imagehash`
package available from PyPI.

No attempts were made to pre-process or normalize input
data. Normalizing inputs prior to algorithm application could
potentially improve results in the future.

### Installation Instructions

The project includes a Dockerfile. To run the project, you'll need to
install `docker`; to follow the run steps below, you'll also need to
install `docker-compose`.

1. Build the Docker image:

``` bash
$ cd path/to/project/root
$ docker-compose build
```

2. Run the Docker image:

``` bash
$ docker-compose run seek_frame  # TBD
```

[challenge]: https://github.com/amnh/HackTheSolarSystem/wiki/3D-and-2D-Bubbles-In-Rock
[profile]: https://github.com/chucksmash
