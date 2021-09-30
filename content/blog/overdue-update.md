---
title: An Update Long Overdue
date: 2016-07-11
category: GSoC
---

It has been a little over a month since I last posted a blog about my updates
on the work I've been doing. I admit I've been a bit lazy these past few weeks
and pushed a few deadlines ahead, but I've caught up with my planned time line 
now after a few night-outs :D.

Stuff not working and dealing with futile attempts at optimization are to blame
for my temporary loss of enthusiasm. I've also been reading A Song of Ice
and Fire which is the book series Game of Thrones is based on, and those books
are difficult to put down once you've started. I was going to work on a TMX
parser for directly loading maps from a TMX file. Implementing a parser was
easy because I had planned on using an existing python library. I ended up
using [python-tmx](https://pypi.python.org/pypi/tmx) which is a pretty
lightweight and straightforward library with the minimal set of features our
module requires unlike the feature rich and heavy **PyTMX** which I had 
mentioned last time.

#### What the parser does

All **python-tmx** does is parses the tmx file's xml and loads the data into
python objects arranged hierarchically according to the xml nesting. So my job
just involved reading data from those python objects and initializing all the
referenced components. The code is so simple to understand that I was able to
submit a patch to this library for animation frames support.

First we need to load the tilesets as textures in KivEnt and register them in
the `texture_manager`. Kivy, and even KivEnt uses image atlases for loading
multiple textures from a single source image, which is faster because we load
and process one large image file instead of multiple smaller image files. The
atlas file contains the texture name and its position and size in the source
image, so its pretty obvious how to extract the texture from the image.
In graphics rendering term you only need to modify the mesh matrix without the
overhead of loading an image. More details can be found in this
[Gamasutra article](http://www.gamasutra.com/view/feature/2530/practical_texture_atlases.php)

#### The **Tiled** way of assigning images to tiles 

**Tiled** use the fact that each tile is of the same size to its advantage in
storing atlas-like information in a concise manner. Each tile in a tileset has
an index assigned to it starting with the top-left tile as 0 and incrementing
as we move left. So a 3x3 tileset would have tile indices like so:

```
0 1 2
3 4 5
6 7 8
```

Each tileset has a unique id called the `firstgid` or first global id.
The intention is that each tile of each tileset should have a unique id or
`gid` which is the `firstgid + index` for each tile. So if we have 3 tilesets
3x3, 2x2 and 2x3 respectively and the `firstgid` of the first is 1. Then the
gids of the tiles in that first tileset is 1,2,..9. Hence to maintain uniqueness
the `firstgid` of second tileset is 10, similarly for the third. Now all you
need to store is the `firstgid` for each tileset and you know the gid of each
tile.

The next thing we have to do is to arrange these tiles on the grid to make our
desired map. The way to do it is now extremely simple. Each position on the
map `(x,y)` will have a `gid` corresponding to the tile we place there or 0 to
denote no tile or empty space (notice how gids are greater than 1 because the
firstgid of the first tileset was 1). For multiple layers you just need to have
this data for each layer.

You can play around with the tilesets and tiles to add properties like vertical
or horizontal flipping, animation frames, opacity, etc. by adding a tile
property element in the tileset with the index of the tile and the property you
want to add.

#### Rendering it all on our game canvas

The map grid data for layers is stored as one big sequence of gids. Because we
know the size of the map grid we can easily find the `(x,y)` coordinates from
the index in this sequence where

```
x = index % width
y = index / width
```

Once you know the `(x,y)` coordinate, we also know the actual pixel position
on the canvas of where to draw this tile because we know the tile size. We also
know what texture to draw because of the gid.

I have fixed the textures and models to be loaded with the name 'tile\_\<gid\>'.
To pass to the `tile_manager` we need a three-dimensional array spanning
**rows** x **columns** each element being a list of dictionaries with the
model and texture name and layer index for that grid location. It is easy to
form this array of dicts from the layer data when we have fixed the naming
convention for textures and models. This also lets us form a list of all the
gids we will use so that we only optimally load those.

Once we have this list of gids we have to load, we will create an atlas dict
for each tileset which has the texture name in our defined format and the
position of that texture in the image calculated from the index of the tile.
We pass this atlas dict to the `texture_manager` which then handles the rest of
the job. Once we have the textures loaded we load the models using the same
naming convention. And then we load the tile\_map using that array of dicts we 
generated before. This order is necessary because `map_manager` loads data for
textures and models using the registered names and for that the names need to
be registered with the texture and model managers first.

Next task is to initialize each tile as an entity so that it gets rendered on
the screen. Each layer requires a different renderer if we need to control the
z-index of the tiles. And for animated tiles each renderer requires its own
animation system. I made a util function for easily initializing multiple
renderers and animation systems at once and adding them to the gameworld. And
I tweaked the `init_enitity_from_map` function from before to support layers
and use the correct renderer names.

The result is pretty amazing :D

![Finally!]({static}/images/map_tmx.png)

#### Futile optimizations

I tried researching into trying to use a single renderer with z-index support
for rendering layers without the need for multiple systems. But there are a lot
of problems which would arise when batching. It is better performance-wise to
let Kivy handle z-index in terms of order of drawing the canvas.

Currently the util functions are all pure python functions because the api to
init entities and register textures and models is python-based. A cython api
doesn't exist and hence we have the python overhead of creating dicts to pass
as init args. Kovak says there is some more tweaks in the base of KivEnt
required to correctly implement a cython api, and that he has been considering
it for months now. So for now, I have to stick to using the python api.

#### What next

Next is implementing hexagonal and isometric tiles support, which is essentially
just figuring out the pixel position of the tiles on the canvas differently.
I think the toughest part will be to create a hexagonal and isometric map but
you never know :P.
