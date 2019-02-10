# Simple atlas file generator for libGDX
This python script generates **atlas** files for [libGDX](https://github.com/libgdx/libgdx) [TextureAtlas](https://github.com/libgdx/libgdx/wiki/Texture-packer#textureatlas) class. You can use it with existing sprite sheets downloaded from sites like [OpenGameArt.org](http://opengameart.org).

Usage
-----
```shell
> python ./main.py <./path/to/sprite_sheet.png> <./path/to/sprite_sheet_descriptor.json> 
```

- `<sprite_sheet.png>` is the path to your spritesheet
- `<sprite_sheet_descriptor.json>` is the JSON description of your spritesheet  (see exmaple directory)

Run the Example
-------
> python ./main.py ./example/dude.png ./example/dude.json
>
Generated dude.atlas:
```
dude.png
size: 832,1344
format: RGBA8888
filter: Linear,Linear
repeat: none
jump_up_00000
	rotate: false
	xy: 0.0, 0.0
	size: 64.0, 64.0
	orig: 64.0, 64.0
	offset: 0, 0
	index: -1
jump_up_00001
	rotate: false
	xy: 64.0, 0.0
	size: 64.0, 64.0
	orig: 64.0, 64.0
	offset: 0, 0
	index: -1
jump_up_00002
	rotate: false
	xy: 128.0, 0.0
	size: 64.0, 64.0
	orig: 64.0, 64.0
	offset: 0, 0
	index: -1
jump_up_00003
	rotate: false
	xy: 192.0, 0.0
	size: 64.0, 64.0
	orig: 64.0, 64.0
	offset: 0, 0
	index: -1
jump_up_00004
	rotate: false
	xy: 256.0, 0.0
	size: 64.0, 64.0
	orig: 64.0, 64.0
	offset: 0, 0
	index: -1

  ... rest ommitted
```

Notes
-----
Every tile in sprite sheet must have the same width and height.

Tiles are in horizontal order, without any gaps between.

Script doesn't check if passed arguments have any sense.

