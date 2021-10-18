---
title: One Hell Of A Summer!
date: 2016-08-16
tag: GSoC
category: Blog
---

I always wondered how large-scale projects and organisations got formed and
got to the stage where they currently are, where there are tens or even
hundreds of people maintaining them and constantly contributing to make them
better. I wondered how it would feel like to see the project build up from
the first line of code! Google Summer of Code allowed me to experience that!
It truly has been an overwhelming and exciting summer of code!

I got to see the very beginning of the maps module, from not just the first
line of code but the initial concept, the plan of coding it and everything.
I know it is just a small part of kivent but it has certainly been huge for me
compared to the projects I have done before!

I will try to describe my project from the very beginning in this post.

#### Initial Idea

KivEnt is a game engine and the one thing every game engine needs is a module
for displaying tile maps. Tile maps make it simple to design game levels and
fields. For example without a map module, a pokemon game developer would have
to individually place each grass tile, sand tile and water tile manually, he
would have to decide where which cliff edge goes so that the cliffs look
elevated in 3D. You are already thinking of ways to automate all this aren't
you? Yeah, just store a 2D array with which tile to render in that position
and we can make the 2D array separately. Why don't we store the array in a file
in some standardised format so we could create that file externally. Layering
would just require multiple 2D arrays!

![pokemon map created in Tiled]({static}/images/pokemon_map.png)

These are such fundamental requirements of games that there are a lot of tools
out there just for creating that external file I mentioned above. A very famous
editor is the Tiled Map Editor. Tiled has a fixed format of its files known as
TMX and so to display the map created in Tiled on KivEnt, we need module to
take all that data from the TMX and render it correctly on the KivEnt canvas.
That is essentially what the map module does. But just displaying those tiles
and forgetting about them isn't done. We need to be able to access and modify
every tile hence the module also has a good api to access the data.

#### Fundamental Requirements

KivEnt runs on the entity-component architecture which in the simplest sense
means that each object in the game is an entity which has data components for
each system that controls its properties. So each tile of the map has to be
an entity and have some component which relates it to a map. So we have the
MapSystem which controls the position of each tile on the map (row, col).
First requirement hence was to setup such a system and the corresponding
component. Also each tile could have additional properties like animation and
hence be a part of other Systems.

Next, we need a way to efficiently store all the data about which place on the 
map has which tile. Contiguous allocation is the best way because the tile at
row `m` and column `n` is at element `m * map width + n` in the array!
We do such array allocation at the Cython level to have greater control
over the memory used. But to access this data in code, we also need to have 
Python APIs for all this data. I built wrapper API classes for both a single
tile and the whole tilemap which was the second requirement.

 - [PR #141](https://github.com/kivy/kivent/pull/141): This is the PR where I
   built this first minimum viable prototype of the module.
 - [PR #142](https://github.com/kivy/kivent/pull/142): Added animation to tiles
   in this PR.
 - [PR #143](https://github.com/kivy/kivent/pull/143): Fixed a batching bug
   in the AnimationSystem which prevented textures from two different sources
   being added as animation frames together.

I then rendered this kinda trippy color tiles map. There was no automatic
entity creation features so I had to set the tile in each place randomly but
its a good test case.

![First working prototype]({static}/images/animated_tiles.gif)


#### Loading TMX files

Now that we have a setup which can store tile map data and easily render it as
entities in the game, we just need to get the data from the TMX to the TileMap
object. For that we first need something which could parse the XML in TMX and
get data. I decided to use [python-tmx](https://pypi.python.org/pypi/tmx)
which is simple and pretty lightweight. It wraps up the XML data to python data
objects. There were some feilds which were not being read by the module because
it wasn't up to date with the latest TMX format. So I submitted patches to it
for implementing the missing bits.

 * [Patch #1](http://savannah.nongnu.org/support/?109083): For loading
   animation frames correctly.
 * [Patch #2](http://savannah.nongnu.org/support/?109092): For hexsidelength
   parameter for hexagonal tiles.

#### Basic TMX parser

There are a lot of steps involved in loading TMX files. For a basic idea, each
tile would require a texture, a model and possibly an animation to display it.
[This previous blog post](TODO) covers the
details of the parser.

 * [PR #149](https://github.com/kivy/kivent/pull/149): Basic TMX parser
   implementation for orthogonal tiles.

Next step was to support other tile formats like hexagonal and isometric

#### Hexagonal and Isometric tiles

Hexagonal tiles have a form of arrangement called staggered arrangement. We can
have the same kind of arrangement for isometric to get an isometric staggered
map.

This is the way tiles in a staggered arrangement would look like.

```
o   o   o   o
o o o o o o o o
o o o o o o o o
o o o o o o o o
  o   o   o   o
```

The above arrangement has stagger index as even and stagger axis as x axis.
This just means that every even indexed tile along the x-axis will be shifted
along the y-axis by 1.

If the stagger index was odd and the stagger axis was y axis, this would be the
outcome.

```
  o o o o o o o
o o o o o o o 
  o o o o o o o
o o o o o o o 
  o o o o o o o
o o o o o o o 
```

Now consider if these tiles were hexagonal or isometric in shape, with the
correct spacing and positioning we could create a map using staggered
arrangement. All we have to add to the code is how to get position of the tile
from `(i,j)`. Silimar lgic applies for isometric arrangement.

Here are some examples:

![hexagonal]({static}/images/hexagonal.png)

![isometric]({static}/images/isometric.png)

![staggered]({static}/images/staggered.png)

[PR #153](https://github.com/kivy/kivent/pull/153) is where I added this
feature. Figuring out the formula for the position from `(i,j)` was really
interesting! I will probably describe it in another blog post.

#### Shapes and other Objects

Maps may have something other than just tiles drawn on them, like circles,
polygons and images. Tiled has a way to store all that data, and so our module
has to be able to display it. For drawing shapes we use KivEnt's VertexModel.

VertexModel is a set of vertices and a list of indices which indicate what
triangles to draw to create the shape required. So essentially all polygons 
can be represented as multiple adjoint traingles using these vertices
and indices. We can also display ellipses using a high number of triangles.
So there is a util function which takes the vertex data of the shapes in TMX
and converts them to suitable data for the VertexModel. To display the shape
all we have to do is create an entity with this model as its render data.
Images are trivial too because they will be rendered separately as any other
image with a rectangular model and texture.

This is how the objects look on screen:

![objects]({static}/images/kivent_objects.png)

I added this feature in [PR #154](https://github.com/kivy/kivent/pull/154).

### The End

This was the entire work I did as part of GSoC, ending it with
[PR #156](https://github.com/kivy/kivent/pull/156) for documentation and a bit
of code cleanup. In the community bonding period I had worked on the
AnimationSystem in [PR #131](https://github.com/kivy/kivent/pull/131) which was
required in the maps module.

This has been really the most exciting project I have ever done!
I thank Google Summer of Code, Kivy, and Jacob Kovak, my mentor, for
giving me this great oppurtunity and helping me complete it!

*Check out the tutorial to use the maps module with KivEnt
[here](TODO)*
