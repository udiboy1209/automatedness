---
title: SegFaults At 3 In The Morning
date: 2016-05-17
tag: GSoC
category: Blog
image: /images/twinkling_stars.gif
image_size: side
---

Segmentation Faults are a nasty sucker. Any moderately experienced C/C++ programmer would know that. 
But well, I didn't.
I had started coding in Java initially, which has an exception throwing tendency
which is the inverse of Perl's :P!
And it throws very clear and precise exceptions with a stack trace to point out exactly where you messed up.
After Java I moved to Python, which is no different in terms of how it behaves with run-time errors. 
Modern programmers love exception-handling and stack traces it seems! Most of the contributions I have
done till now for Kivy have involved only dealing with python code,
but Kivy heavily relies on [Cython](http://cython.org/).

#### Cython - The backbone of computational python!

Cython is a C-Extension for python, which means it compiles python code to 
C to optimize and improve speed and computational power.
Cython also lets you write C -like code the *"python way"* and integrate it with existing python code.
Naturally Kivy relies heavily on it -- any Native UI application requires speed.
Something like KivEnt would have been out of the question if Cython didn't exist. 
You just cannot get the speed you need for a game engine with pure python.
A lot of scientific computation libraries like [numpy](http://numpy.org) and [sympy](http://sympy.org)
use it too.

These past two weeks I have been working on a new animation system for KivEnt, 
which let me get my hands dirty in Cython for the first time. I really liked the experience, 
and I'll also need it for most of my GSoC! I have always found python insufficient or lacking 
when I'm using it for computationally intensive tasks. Cython takes all those worries away!

#### KivEnt's new AnimationSystem

KivEnt essentially works using modular, inter dependant systems. These systems define how to process specific 
types of data components for each entity. Take the `PositionSystem` and `Renderer` 
(system which draws objects on the screen) -- The `PositionSystem` will update a `PositionComponent` 
in the entity's data to change physical position of the 
entity and Renderer will use the values stored inside this `PositionComponent` 
to draw that entity on the screen. Thats a very basic example, now try to think how a `VelocitySystem` 
would interact with `PositionSystem` and use `VelocityComponent` to modify `PositionComponent` 
and you'll get the general idea of how KivEnt systems work :P.

The `AnimationSystem` is something which can render animations. Animations are extremely simple. 
You display an image for some duration, and then switch it with another image. Each image displayed for
a certain duration is called a frame. So for making an animation, you need to specify a bunch of frames which
is essentially a list of `{image, duration}` values.

Rendering images is handled by the `Renderer` so all the `AnimationSystem` has to do is wait 
for a frame to complete its duration and then change the render images for the entity, 
then again wait for its next frame. 
It's job is so simple it could have been directly coded in python. 
In fact here is an example displaying just that: 
[Simple Animation](https://github.com/kivy/kivent/tree/2.2-dev/examples/8_simple_animation)

But we need a faster and more powerful alternate.
Something which can handle thousands of entities in each update.
Cython!
Plus we also need to make an `AnimationManager` to load/handle all animations, auto load animations from
files, etc. So it needed to be done in Cython!

#### The mother of all SegFaults: Bad Pointers

Wait why do we need to deal with pointers in python? Is there even such a thing?

There is in Cython. I mentioned before that Cython is a C-Extension.
That means you have to pre-declare all your variables. With type. 
Which in turn leads to having to declare whether your variable is some type or a pointer to that 
type. You don't have Python here to automatically assume (or work around) them for you during assignment.

The segfault I was encountering was because one of the functions was getting a null value 
instead of a pointer parameter. I had found this out by adding `print` statements to every function 
and checking where my program got stuck. This is a pretty stupid thing to do with segfaults. 
I wasted one whole day looking in the function which was apparently throwing the segfault, 
never realizing that the problem was in some other function passing the wrong parameter.

Well, I relayed this to my mentors and they suggested using this awesome tool for debugging:
[GNU Debugger](https://www.gnu.org/software/gdb/). It can do a lot of uber-cool ninja-level stuff
which I still have to learn but the one thing that it surely does is give me a stack trace of the error
which led to the segfault. But again, gdb stack traces for Cythonized C code are nasty as hell. 

Here's an example:

```
#0  0x000000000000000a in ?? ()
#1  0x00007fffe7ea8630 in __pyx_f_11kivent_core_15memory_handlers_5block_11MemoryBlock_allocate_memory_with_buffer (__pyx_v_self=0x7fffd9fdccd0, __pyx_v_master_buffer=0x8fb4d0 <_Py_NoneStruct>)
    at kivent_core/memory_handlers/block.c:1162
#2  0x00007fffe22d0e61 in __pyx_pf_11kivent_core_9rendering_9animation_9FrameList___cinit__ (__pyx_v_name=<optimized out>, __pyx_v_model_manager=<optimized out>, __pyx_v_frame_buffer=<optimized out>, 
        __pyx_v_frame_count=<optimized out>, __pyx_v_self=0x7fffe0fa5e60) at ./kivent_core/rendering/animation.c:2022
#3  __pyx_pw_11kivent_core_9rendering_9animation_9FrameList_1__cinit__ (__pyx_kwds=<optimized out>, __pyx_args=<optimized out>, __pyx_v_self=0x7fffe0fa5e60) at ./kivent_core/rendering/animation.c:1888
#4  __pyx_tp_new_11kivent_core_9rendering_9animation_FrameList (t=<optimized out>, a=<optimized out>, k=<optimized out>) at ./kivent_core/rendering/animation.c:2900
#5  0x00000000004b6db3 in ?? ()
#6  0x00007fffe24d9280 in __Pyx_PyObject_Call (kw=0x0, arg=0x7fffe544e1b0, func=0x7fffe24d5900 <__pyx_type_11kivent_core_9rendering_9animation_FrameList>) at ./kivent_core/managers/animation_manager.c:2124
#7  __pyx_pf_11kivent_core_8managers_17animation_manager_16AnimationManager_4load_animation (__pyx_v_loop=<optimized out>, __pyx_v_frames=<optimized out>, __pyx_v_frame_count=<optimized out>, __pyx_v_name=<optimized out>, 
            __pyx_v_self=0x7fffe56d3410) at ./kivent_core/managers/animation_manager.c:1427
#8  __pyx_pw_11kivent_core_8managers_17animation_manager_16AnimationManager_5load_animation (__pyx_v_self=0x7fffe56d3410, __pyx_args=<optimized out>, __pyx_kwds=<optimized out>)
                at ./kivent_core/managers/animation_manager.c:1387
#9  0x00000000004c4d5a in PyEval_EvalFrameEx ()
#10 0x00000000004ca39f in PyEval_EvalFrameEx ()
#11 0x00000000004c2e05 in PyEval_EvalCodeEx ()
#12 0x00000000004ded4e in ?? ()
#13 0x00007fffe28ef5a9 in __Pyx_PyObject_Call (kw=0x0, arg=0x7fffe0fac9d0, func=0x7fffe54510c8) at ./kivent_core/gameworld.c:13802
#14 __Pyx__PyObject_CallOneArg (func=func@entry=0x7fffe54510c8, arg=arg@entry=0x7fffe80ca670) at ./kivent_core/gameworld.c:13839
#15 0x00007fffe2901f2d in __Pyx_PyObject_CallOneArg (arg=0x7fffe80ca670, func=0x7fffe54510c8) at ./kivent_core/gameworld.c:13853
#16 __pyx_pf_11kivent_core_9gameworld_9GameWorld_6init_gameworld (__pyx_self=<optimized out>, __pyx_v_callback=<optimized out>, __pyx_v_list_of_systems=<optimized out>, __pyx_v_self=<optimized out>)
                    at ./kivent_core/gameworld.c:5916
#17 __pyx_pw_11kivent_core_9gameworld_9GameWorld_7init_gameworld (__pyx_self=<optimized out>, __pyx_args=<optimized out>, __pyx_kwds=<optimized out>) at ./kivent_core/gameworld.c:5630
#18 0x00000000004b1153 in PyObject_Call ()
```

Google Summer of Code is a really great platform for students to learn, because everybody
is assigned one or more mentors to help them out. I do too. So why debug yourself :P.
Just kidding! I had no clue how to interpret this because I was kinda new to Cython. Also it was 3AM in the
morning at that point and I wa just too sleepy to look at any more of this stack trace!
My mentor told me to show him the stack trace and he helped me find the culprit. It was this:

```
__pyx_v_master_buffer=0x8fb4d0 <_Py_NoneStruct>
```

The parameter `master_buffer` is being passed a `None` value! It was an easy debug after this.
I wish I knew about this earlier. But quoting Kovak, one of my mentors:

> Some of the most valuable experience is knowing what not to do.

After this I encountered another segfault, and debugging that was a breeze. I had made a pointer 
assignment inside an `if` and used it somewhere outside.

#### Twinkling stars!

So twinkling stars is an example I was trying to debug my new code with. It loads 50 animations
with three frames, each having three successive images of a twinkling star animation. The difference between
each of the 50 is the duration of each frame, which is randomly assigned. I thought it would look beautiful.

The results are pretty great:

![twinkling_stars](/images/twinkling_stars.gif)

This was a pretty satisfying result for me :D! I still have to add and test a few features before I can do
a performance test, but this has 3000 stars with 1 of 50 different animations, and it runs pretty
smooth on my machine!
