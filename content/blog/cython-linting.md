---
title: Cython Needs A Lint Tool
date: 2016-06-18
tag: GSoC
category: Blog
image: red_blue_stars.gif
---

My love for cython has kept increasing constantly for the past few weeks.
It feels like by the end of my GSoC I might switch to cython entirely, if thats
possible. Cython lacks a few key development tools though - a code testing tool
and a lint tool. I felt great need for it while cleaning up unused variables
in the latest PR. Manually doing stuff just doesn't cut it for an automater :D.

This week was mainly focused on getting animated tiles implemented and working.
Implementing animation was easy. I just had to store an extra pointer in the
`Tile` object for the animation `FrameList`, and add a python api to access it.
Animations can now be specified for a tile while map creation by specifying the
animation name to load in the dict. The `MapManager` will take care of fetching
the `FrameList` pointer and `map_utils` will take care of initialising the
animation system.

#### Debugging is inevitable

Have I mentioned before that no code works on the first go?
Not even something simple like making a tile animated which very frankly just
involved copying and modifying code from the last example I had built for
testing the animation. After breaking my head behind debugging this for almost
a day, I asked Kovak about it. It turned out to be a bug in the animation
system! KivEnt's renderer does a very neat trick to improve efficiency.
It batches all the entities which have to be rendered from the same image
to be processed together so that the same image doesn't need to be loaded
repeatedly. In `AnimationSystem`, we constantly keep updating the texture of an
entity with time, hence it is important that we add those entities to the
corresponding batch according to the new texture to be set. Sometimes entities
don't need to be "rebatched" because they already are in the final batch they
will end up in after the texture change. There was a bug in the test condition
for this which made it return `True` always.
In the very basic sense this was what was happenning: `old_batch == old_batch`
:P, while it should have been `old_batch == new_batch`. Because of the always
true condition, the case where the animation was created from different images 
was never rendered because the texture change was never rebatched.
A few code fixes and updates to the twinkling stars example so that animations
use different image files led to this:

![beautiful night sky]({static}/images/red_blue_stars.gif)

Isn't this even more beutiful than the previous example :D. Because I had to
remove a lot of code for this fix, there were a lot of unused variables lying
around. That is why I so desparately wanted a good linting tool I could import
into vim and automate the boring process of manually finding unused variables.
Also, because cython code is majorly python-like, there needs to be a pep8 like
standard for cython, along with a checker tool.

I then later found out the cython compiler can be configured to issue warnings
for unused variables. Someone needs to make a good tool out of it, probably
just a vim plugin for that matter. I might do it myself if I get enough motivation.

Anyway, that fix led to one more thing, animated tiles started working! Here,
have a look:

![Yay!]({static}/images/animated_tiles.gif)

#### Next in line

Now that a basic map creating pipeline is in place for KivEnt, I can move on to
actually trying to parse a Tiled Map file i.e. a TMX file and create a map from
it. Parsing TMX should be easy as there are a lot of feature-rich TMX parsers
existing for python. [PyTMX](https://github.com/bitcraft/PyTMX) is one such
module I have in mind to use for this job. The rest of the task is just loading
textures, models and animations from the tmx file and then assigning those
values to individual tiles to create entities. I have been trying to create
my own maps on tiled to get familiarised with it, and the first thing I did was
create a Pokemon map because why not :P. Obviously, I won't be able to use this
in KivEnt examples because I don't think the tileset is open source :P. So I'll
have to find an open source tileset and make another Tiled map for testing.
Have a look at the Poekemon map:

![pokemon_map]({static}/images/pokemon_map.png)


