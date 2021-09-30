---
title: A Man Has Duties
date: 2016-06-05
category: GSoC
---

Game of Thrones fans might identify the title as a (not so)
famous dialogue from the series' mysterious character
Jaqen H'ghar. So the GSoC coding period began two weeks back
on 23<sup>rd</sup> May while I was obsessed with this epicly
famous TV series. I was busy binge-watching episodes from
season 1 through 6 (which is currently running) when I realized
that I needed to get on with the planned work of these two weeks.
A man has duties.

#### A man's plans

The planned work for these two weeks involved writing boilerplate code
for the new Map module in KivEnt. Boilerplate for a new module in KivEnt
essentially involves making a python package with the name
`kivent_<module_name>` and creating a `setup.py` file to compile cython
inside it.

And then there's KivEnt specific classes to be added i.e. GameSystems and
data objects. The map module requires a manager to make creating and modifying
maps easy enough and bundled in a class. So my plan was to first learn about
KivEnt's structure and then create all these classes and decide how to pipeline
the flow of creating and rendering a map for the user would be.
Possibly also make an example app to demonstrate this.

#### Give a man a task and a man will do it

In all fairness, nobody gave me this task. I planned for it myself.
But you'll understand my obsession if you have seen GoT :P.

I had planned for reading and researching on how to make KivEnt
gamesystems and managers, how to render entities on the screen
inside a system and how to allocate and use contiguous memory.
But I didn't need to do that this week because the `AnimationSystem`
I had coded in the community bonding period gave me a very good
introduction to a lot of KivEnt's internals. Making the classes for
the map module was fairly easy. I had to just reuse and modify code I
had written for the animation module.

I had thought memory management might be a problem but my mentor
Jacob Kovak has done a really great job with wrapping up the ugliness
of cython's memory management and `malloc` into a really [easy-to-use API](//www.kivent.org/docs/memory_handlers.html).
I realized this while figuring out how to store the animations for the
animation module. I wanted to read more about it and dive into the code,
but I've been obsessed with something else this week :P. The only problematic
or challenging thing was dealing with the build script `setup.py`.

##### `setup.py` is dark and full of terrors

Quite frankly its not that horrible, but it was my first time dealing
with cython build scripts. The cython docs for building are vast and
quite complex. There's a lot of options and features which can be used
and would take a lot of time to understand them all.

So I was fiddling around with a lot of options that didn't work too well.
In the end, I just copied the `setup.py` of another KivEnt module which
was easy to understand and modify and worked out pretty well :D.

#### Current status

I still need to test the code I have written. I am waiting for
Kovak to add a feature to the core module for registering managers
to be init in the GameWorld. It is easy to do if you are adding a module
to core, because it just involves adding a few lines to GameWorld's init.
But I can't add a manager I create in the map module to GameWorld because
that would make the map module a dependency of the core module which is
not desirable. In most cases people would use the core module without
needing the map module.

Once that is done, the GameWorld instance would have a MapManager instance
which can be accessed in your app. Then I can test the example I have written.

#### And my watch ends

The next task is integrating animated tiles into the map module, which will use
the animation module I added to core. I hope things run well in the boilerplate,
else it would make me a little behind schedule.

I don't have a demo to show currently but I can show you a screen shot of my code.

![tty1]({static}/images/tty1.jpg)

Okay, okay don't laugh at me! I usually code on tty1 in linux (its very distraction free)
and I didn't know how to take a screen shot of that :P.

In other news, we got logo stickers printed for the new Electronics Club logo!
And I also received the GSoC welcome package which contained a sticker. So that
makes two sticker additions on my laptop! I also learned a bit about 3D printing
and used a 3D printer to print [a batman logo](http://www.thingiverse.com/thing:320808), which I'll paint and stick somewhere :D!
