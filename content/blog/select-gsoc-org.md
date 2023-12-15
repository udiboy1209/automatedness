---
title: How to select an organisation for GSoC?
date: 2016-12-06
tag: GSoC
category: Blog
image: http://67.media.tumblr.com/13d6615cc38164ea526e76dfb97120b2/tumblr_inline_o8yymp7tDw1tovw1t_500.gif
---

Hello! Its been a long time since I have posted something, because it has been
a really long and hectic semester of college! Its over now, Phew! My friend
Chinmay, who has been asking GSoC related questions to me for a while now, asked
me to describe how does one go about selecting an organisation to apply for GSoC.
So here I am. Hope you find this post useful.

#### What is a GSoC organisation?

GSoC is basically a platform for open source projects to attract potential
students to contribute over the summers in return for some great working
experience (and a good stipend :D). And it encourages open source organisations
to propose such projects and provide mentors. It is in the interest of
organisations to propose and mentor projects so that they get enthusiatic people
to contribute a summer of work, and it is in the interest of students to do such
projects for the awesomely fun experience of working on actively developed projects
and getting to interact with the open source community.

Examples of such organisations are [Mozilla](https://wiki.mozilla.org/SummerOfCode),
[Python Software Foundation](https://wiki.python.org/moin/SummerOfCode/2016),
[KDE](https://community.kde.org/GSoC) and many more. These organisations I mentioned
are quite huge with a very large community backing them, and have multiple projects
actively being developed. There are a lot more such organisations and communities
which participate in GSoC every year (some big and some small but just as great :D).
You can see the entire list of organisations and the projects they mentored 
on [the GSoC website](https://summerofcode.withgoogle.com/archive/2016/organizations).
Previous year's data is just a google search away
(get used to googling and get better at it :P, it's really necessary for GSoC).

#### What should I look for in an organisation?

People think GSoC is all about coding and sitting in front of your laptop working
through the summer but that's not true. GSoC or any other open source contribution
is about interacting with a community of like-minded people and contributing along
with them to a common cause. The motivation to contribute can be anything from
you personally benefitting out of it, or you wanting to thank the community because
it helped you before. Or maybe you just want to explore something new! Contributions
can be anything, not just actual code. A lot of communities appreciate help with
their documentation and testing of various issues and features. Maybe you found
a small typo in a documentation page you were reading, and felt like fixing it.
Maybe you were that guy/girl and found some grammatical errors :P . You can go over
to the community and tell them you found this mistake, and ask them to fix it.
Maybe ask them to show you a way to fix it yourself. Yes you could definitely fix
such mistakes yourself! All open source communities have a very easy-to-use way
to make changes to its codebase/documentation. Most use `git` which is really
easy once you start using it. So what if its just a small typo. It will be fixed
because of you, your tiny little enthusiasm to right a wrong. The community will
surely appreciate that effort, no matter how tiny it is. It may be scrutinized
and checked so that it doesn't cause any trouble, but it will be appreciated.

![open_source](http://image.slidesharecdn.com/amigos-oss-2015-150918030424-lva1-app6891/95/open-your-mind-open-source-in-libraries-3-638.jpg?cb=1442545537)

Its like you volunteering to decorate the neighbourhood for Diwali. So what if
you just hang one light bulb. Or you just test if all the lights work or not.
Your neighbours will surely appreciate that effort no matter how tiny. And in
the end you will enjoy the festival and the lights along with the rest of the
community, knowing that one light of the many is there because you hanged it! 

More than the project, more than the work you might want to do, you should focus
on the community of the organisation you choose. I have seen people pick organisations
because they already know one or two people in the community. Or they have interacted
with the community before for various reasons (almost always personal). 

I popped my cherry in open source with a python-based music library manager called
[beets](https://github.com/beetbox/beets). I was using that software to organise
my music and found a problem in it which I thought could be fixed. So after
a bit of googling I found their github repository and posted an issue there, soon
to get a reply from the creator that I could fix it myself if I was willing!
And I did. It was a pretty small change in the code but it is still there, and
it is there because of me.

#### Lets get specific to GSoC

All that banter was to give you a feel of the open source mindset. That I feel
is important for GSoC, but you would need some more info to proceed.
Now let me tell you a bit about how you should choose an organisation for GSoC.

It helps if you have in mind what softwares/languages/fields you want to work
with. And this shouldn't be restricted to what you currently know. The timeline
of your project has and should have time for learning all the new things required
for your project. Learning and exploring something new is part of the fun!
And remember...

![help](http://67.media.tumblr.com/13d6615cc38164ea526e76dfb97120b2/tumblr_inline_o8yymp7tDw1tovw1t_500.gif)

Well, you may not be a wizard at Hogwarts but this is true.
You will have mentors in GSoC who are proficient in the area of
your project and you can ask them to teach you all the new stuff that is required.
All you need is enthusiasm and the will to learn.

When I decided I wanted to do GSoC, I was doing a lot of Android projects and apps,
and so it may have been easier for me to work on some Android based project. But
I was interested in learning python, which is a language I had tried out a bit only,
so I opted for a python org instead. So I started contributing to Kivy
and started interacting with the community. Kivy has a game engine
called KivEnt and there was a project idea proposed by the Kivy community to work
on KivEnt over the summer under GSoC. Coincidentally, I am very interested in game
development and this project idea really appealed to me. So that is what I decided
to take up as my project. The problem though was that KivEnt isn't coded in pure python and due to performance
reasons use a C-extension called Cython. Cython is something really different
to someone used to python, and especially to someone with very little C experience (me :P).
I told a few people about this and they assured me that they will help me with learning
Cython while I am working on the project and it will be quite possible to keep up
with deadlines of the project. And I did successfully learn Cython through the summer
while also finishing my project on time! I learned two things from that. One is that
nothing is too tough to learn and second, people in open source will help you with
**anything** if you ask nicely and show the will to learn.

_Note: while some stuff like languages and frameworks are easy to learn,
some require a little bit more effort especially the topics involving CS or Maths
theory like Computer Vision, Machine Learning, Algorithms etc.
It helps to have some previous overview of such topics
(like a college or online course) if you want to pick such a project/organisation_

So this is how I picked my organisation and project:

 * Language I wanted to work on: python. I chose Kivy which is a NUI framework in
   python.
 * Field I wanted to work in: Game development. I chose to work on KivEnt, Kivy's game engine.

It will really help if you define this for yourself. Then, when you go looking
for orgs in previous org lists or ask people about what org to pick, you will know
exactly what you are looking for.

#### I dont know what my interests are :P

That is a problem faced by a lot of people. There is always the option of trying
out random stuff till you find something you like. But that is very time and
energy consuming. What you could do is ask people you know who have contributed in
open source before, previous GSoCers for example. You could ask them about their
experience of the community, the stuff they worked on and take suggestions from
them.

For eg. there are some python based organisations which do medical image processing
based projects. These projects may not be development intensive and may involve
implementing research papers in those fields and testing multiple cases. You could find
out more about such projects by contacting students from last year.

There are some things other than just the project and the field you are working in.
The entire contribution process for example is something you need to be comfortable with.
Big organisations like Mozilla have a very active community of contributors who
will help you, but they have strict rules when it comes to contribution. Your
contribution isnt accepted until its perfect according to the rules. The community
very readily helps people to clean up their code and patches so that they are
acceptable by the rules, but some people would find such strictness useless or
even frustrating. Smaller organisations on the other hand are more lax. It helps
to know about such experiences beforehand.

![style it](http://imgs.xkcd.com/comics/code_quality.png)

All you need to remember is that whatever these people tell you will be their 
own experience. It is possible that you experience something entirely different.
You will only find out what your interests are when you try out something on your
own. All you will get from asking people is some suggestions on what to explore.
In the end, it is you who defines your interests.

#### How do I find out more about the community?

You start interacting with people of the community. Its not a girl/guy you're
trying to woo that you'd need an icebreaker. Nobody in open source forums likes
small talk, especially from newbies. You want to start contributing, you say
that point blank. People will point you to easy bugs and issues to fix so
you can get set up easily and have a good start. If you are having trouble with
something, don't try being polite, don't ask to ask, don't beat around the bush
trying to be discreet. Just ask, and you will be helped :D.

Once you start on some easy bugs, you will face problems getting the development
environment set up, finding where the bug originated from, what file serves what
purpose and what not. The key is seeking help whenever you are stuck. Nobody
is grading you or keeping score about how well you have performed.

![no grades yay](https://qph.ec.quoracdn.net/main-qimg-73ad447f9b7c51de85ea12405c1e9a3c?convert_to_webp=true)

#### Will the organisation get selected in GSoC?

It is important to know if the organisation has a chance to get selected in
the final list of organisations for GSoC. You may like the community and what they
work on might align with your interests but not all open source orgs apply for
GSoC and not all that apply get selected. There are some criterias Google follows
to select orgs too. 

 1. Only those organisations which are planning to apply for GSoC will get selected.
    Obviously :P. This is the first thing you should check. You can simply ask the
    community directly whether they are planning to apply. There's no reason for them
    to keep this a secret. (for eg. *beets* doesn't apply for GSoC)
 2. Organisations which have been selected last year, or for the past two three
    years are very likely to get selected again. You can look up the list of selected
    organisations on previous year's websites of GSoC.
 3. If the organisation is applying for the first time, it will very likely
    get selected if it has a good community and reasonable number of long time
    contributors. GSoC wants its students to have experience with well-established
    communities and not those which are in the initial phases of ther life.

#### TL;DR

I'll outline the steps you should follow to pick an organisation:

 1. Define what you are interested in learning and working on over the summers.

    1. What language: C++, Java, Python, Rust, JS, etc.
    2. What field: Android, iOS, Game dev, Web dev, Computer vision, Machine learning, etc.

    Ask previous GSoCers about their experiences and suggestions for things to explore.
 2. Ask/Search for organisations which have a probability of getting selected
    for GSoC (look for those which were previously selected) and aligns with your interests.
 3. Start interacting with the community for solving easy bugs, making minor
    contributions. You will get a feel of whether you like the community of that
    org or not.

_Thanks to Kalpesh Krishna for the review and suggestions_
