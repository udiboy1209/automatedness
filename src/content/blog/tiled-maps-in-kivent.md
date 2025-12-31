---
title: How To Use Tiled Maps In KivEnt
date: 2016-08-19
tag: GSoC
category: Blog
---

This is a tutorial for using the maps module in kivent to load Tiled maps. It
covers the steps required to load and display a map on the kivent canvas, but
it doesn't cover how to make a map in Tiled.

#### Building and installing the module

Make sure you have kivy and its dependencies properly set up and working using
these [installation instructions](https://kivy.org/docs/gettingstarted/installation.html).

Clone the kivent repository to obtain the source. The module is currently in a
separate branch 'tiled\_gsoc\_2016' so you can clone that branch only.

```
git clone -b tiled_gsoc_2016 https://github.com/kivy/kivent.git
```

You can skip the `-b tiled_gsoc_2016` if you want the whole repository.

Install `kivent_core` first. Assuming you cloned it in a dir named 'kivent'

```
$ cd kivent/modules/core
$ python setup.py build_ext install
```

Then install the maps module similarly

```
$ cd kivent/modules/maps
$ python setup.py build_ext install
```

It is best to set up kivy and kivent in a virtual environment. Just make sure
you use the correct python for the above commands. The module works
best with python3, but it works with python2 too.

#### Setting up the KV file

We need a basic setup of the gameworld and a gameview where we will add the
renderers to be displayed. We also need to add systems which the tiles depend
on like `PositionSystem2D`, `ColorSystem` and `MapSystem`.

    :::python
    TestGame:
    
    <TestGame>:
        gameworld: gameworld
        camera1: camera1
        GameWorld:
            id: gameworld
            gamescreenmanager: gamescreenmanager
            size_of_gameworld: 250*1024
            system_count: 4
            zones: {'general': 100000}
            PositionSystem2D:
                system_id: 'position'
                gameworld: gameworld
                zones: ['general']
            ColorSystem:
                system_id: 'color'
                gameworld: gameworld
                zones: ['general']
            MapSystem:
                system_id: 'tile_map'
                id: tile_map
                gameworld: gameworld
                zones: ['general']
            GameView:
                system_id: 'camera1'
                gameworld: gameworld
                size: root.size
                window_size: root.size
                pos: root.pos
                do_scroll_lock: False
                id: camera1
                updateable: True

`PositionSystem2D` is necessary for any map because it it responsible for the
tile positions. And `MapSystem` holds the relevant data for the map hence that
is necessary too, obviously. `ColorSystem` is required if there are shapes in
your map which require coloring. And `GameView` is the canvas where we will
render the map's layers.

This is the basic boilerplate KV necessary for rendering the map.

#### Setting up the Systems

I will start with the basic game app structure of `main.py`.

    :::python
    def get_asset_path(asset, asset_loc):
        return join(dirname(dirname(abspath(__file__))), asset_loc, asset)
    
    class TestGame(Widget):
        def __init__(self, **kwargs):
            super(TestGame, self).__init__(**kwargs)
    
            # Init gameworld with all the systems
            self.gameworld.init_gameworld(
                ['position', 'color', 'camera1', 'tile_map'],
                callback=self.init_game)
    
        def init_game(self):
            self.setup_states()
            self.set_state()
    
        def setup_states(self):
            # TODO we need to add the state of the systems to this gameworld state
            self.gameworld.add_state(state_name='main')
    
        def set_state(self):
            self.gameworld.state = 'main'
    
    class YourAppNameApp(App):
        pass
    
    if __name__ == '__main__':
        YourAppNameApp().run()

We now need to load the systems required for each layer. We will have to
specify parameters for them the same way we fo it in KV files. We will make 3
dicts, one each for Renderer, PolyRenderer and AnimationSystem and pass them
to `load_map_systems` util function to create 4 layers.

    :::python
        def __init__(self, **kwargs):
            super(TestGame, self).__init__(**kwargs)
    
            # Args required for Renderer init
            map_render_args = {
                'zones': ['general'],
                'frame_count': 2,
                'gameview': 'camera1',
                'shader_source': get_asset_path('positionshader.glsl', 'assets/glsl')
            }
            # Args for AnimationSystem init
            map_anim_args = {
                'zones': ['general'],
            }
            # Args for PolyRenderer init
            map_poly_args = {
                'zones': ['general'],
                'frame_count': 2,
                'gameview': 'camera1',
                'shader_source': 'poscolorshader.glsl'
            }
    
            # Initialise systems for 4 map layers and get the renderer and
            # animator names
            self.map_layers, self.map_layer_animators = \
                    map_utils.load_map_systems(4, self.gameworld,
                            map_render_args, map_anim_args, map_poly_args)

We will be returned a list of renderers and animators. This list can be added
to the gameworld init sequence like so. Renderers and animators require
specific states to be set so we have to add these lists while setting states.
Modify the corresponding lines with these.

    :::python
            # Init gameworld with all the systems
            self.gameworld.init_gameworld(
                ['position', 'color', 'camera1', 'tile_map']
                + self.map_layers
                + self.map_layer_animators,
                callback=self.init_game)

and

    :::python
        def setup_states(self):
            # We want renderers to be added and unpaused
            # and animators to be unpaused
            self.gameworld.add_state(state_name='main',
                    systems_added=self.map_layers,
                    systems_unpaused=self.map_layer_animators + self.map_layers)

These systems need to be rendered from bottom to top to preserve the
layer order. And the gameview camera handles rendering of these systems. So we
will set the render order for that camera to match layer index. Add this line
to `__init__`.

    :::python
            # Set the camera1 render order to render lower layers first
            self.camera1.render_system_order = reversed(self.map_layers)

#### Loading the TMX file

Next up, we need to populate our systems with entities and for that we need
a TileMap loaded with tile data. This data will be obtained from the TMX file.
The util module has a function for loading TMX files and registering them with
the map manager

    :::python
        def setup_tile_map(self):
            # The map file to load
            # Change to hexagonal/isometric/isometric_staggered.tmx for other maps
            filename = get_asset_path('orthogonal.tmx','assets/maps')
            map_manager = self.gameworld.managers['map_manager']
    
            # Load TMX data and create a TileMap from it
            map_name = map_utils.parse_tmx(filename, self.gameworld)

`setup_tile_map()` should be added to `init_gameworld()` so that it is called
after gameworld init.

`parse_tmx` takes the filename of the TMX, loads it to a `TileMap`, registers it
in the `map_manager` with name as the filename without the extension, and
returns that same name.

#### Creating Entities in the GameWorld

All that is left to do is to create entities from this `TileMap`.
The function for that is `init_entities_from_map`. It requires the `TileMap`
instance and an instance of the gameworld's `init_entity` function. It is used
like this:

    :::python
            # Initialise each tile as an entity in the gameworld
            map_utils.init_entities_from_map(map_manager.maps[map_name],
                                           self.gameworld.init_entity)

You can add this to `setup_tile_map` after `parse_tmx` is called and we have
the `TileMap`.

This is all we require to load a Tiled map in KivEnt.

Download the source files from [here](/images/tile_tutorial.zip)!

Thank you and happy tiling!

<hr>

*EDIT (2016-08-24): Added installation instructions.*
