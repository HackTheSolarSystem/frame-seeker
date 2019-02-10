# AMNH Hackathon 2019

For this Hackathon, I've decided to have a go at the
[Identifying Chondrules][challenge]. I'm going to try to build a proof
of concept using standard image processing and computer vision
libraries in Python.

There are several subgoals that are part of this challenge. The
unifying theme is to identify "bubbles" (magnesium-silicate rocks
called chondrules) within a meteorite sample. The sub goals:

1. Identify the chondrules within the three-dimensional CT scan data.
2. Identify the chondrules within the two-dimensional RGB composite
   map.
3. Find the frame in the tomography that best matches a BSE
   (back-scattered electrons) map of a flat polished surface cut from
   the original rock.

I plan to focus on the third challenge first. I think it's something
that is doable by a single person over the course of ~20 hours. My
reach goals will be to go back and try item #1 or item #2.

## Strategies

### 3D Chondrules

TBD

### 2D Chondrules

TBD

### Frame Matching

This is the part of the challenge to which was initially drawn, and
for which I feel like I have the strongest approach.

I anticipate using a two stage approach to the frame matching
problem. In the first stage, I'll filter the image down to the most
prominent N (N=5? N=10?) features and then create a phash from that.

We'll then create iunno, like a binary search tree of the perceptual
hashes of each of the tomography frames and traverse it to find the
image that image which best matches.

Alternatively, we could just phash the tomography frames themselves
directly. I worry that this will be super noisy though - they're gray
scale images, so how different are any of them really?

## TODOs:

- [x] Pick the computer vision stack you want to use
- [x] Set up a docker environment for running said CV stack
- [ ] Go through an CV tutorial
- [ ] Look up how to process TIFF files by layer
- [ ] Create/find a simple diagnostic tool for viewing side by side
      animations of input/output. If this is too ambitious, just get a
      unanimated version up and working. This might also be useful for
      the demo tomorrow
- [ ] Try out edge and blob detection algorithms included in whatever
      library you picked
- [ ] Write your glue code to ingest the TIFF layers of CT scan and
      store them in a (TBD: data structure) which we will query

[challenge]: https://github.com/amnh/HackTheSolarSystem/wiki/3D-and-2D-Bubbles-In-Rock

## Journal

### 17:30

Took my sweet time up to this point, but I've now picked the computer
vision library I want to use (OpenCV), and set up the Docker
boilerplate for using it.

### 04:42

Gave up on this for the night. Had a lot of trouble with the 16bit
gray scale TIFFs and Pillow, but the 8bit grayscale TIFFs look
reasonable.

I'm going to lay down for a couple of hours now. When I wake up, I'm
planning to write some code to put the phashes into a sorted
list. When we go to match a BSE against that list, we'll just bisect
until we find the best match and then return the top N.

I've basically spent the entire Hackathon up until this point
understanding the problem and doing set up/exploratory work. I think
that will work given the task I've set myself, but in the future it'd
probably be better start sprinting right off the starting gun.

### 07:41

Back at it after a bit of sleep, a change of clothes and a smidge of
deodorant. For Aiur!
