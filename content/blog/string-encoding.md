---
title: Python Strings and the Headaches of Encoding
date: 2016-05-22
tag: GSoC
category: Blog
---

#### Life is never simple

For the last week of the community bonding period,
I was finishing off the animation module for KivEnt.
I added a JSON parser inside `AnimationManager` to read and store
animation lists stored on disk in JSON format. Making this module
was fairly simple. I had to use python's json library to get a dict from
the JSON file for reading, and convert a dict to a JSON string to store to
a file. You must be thinking this would have gotten finished pretty easy,
adding two functions in the `AnimationManager` and making a simple test
JSON file in the twinkling stars example accompanying this module.
But alas, things are never so simple in life. I mean, NEVER!

Every python user, if they have worked with python 2,
will have faced this infamous error:

```
UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in \
position 0: ordinal not in range(128)
```

What this essentially means is that the python string we have
has a byte of value `0x80` somewhere and our poor old ASCII.
encoding, in which python strings are encoded, has no character for that value.
The JSON parser module very smartly returns Unicode encoded
strings, which is a character encoding different from ASCII.
But the animation names in my module were beign stored as python
strings, which are encoded in ASCII, and hence the error.

The JSON parser has to do this because the JSON files would almost always be
in UTF-8 format which follows the Unicode encoding. Unicode allows
support for a lot more characters than ASCII (The Euro symbol for example),
hence is more widely used. Let me explain in detail what encodings are.

#### Encodings - Why do they exist?

Computers, being the stupid chips of silicon they are, do not
understand text as we do. They love numbers, binary numbers, and hence store,
interpret and communicate all kinds of data in that format. So humans need to
devise a system to convert that binary data to an understandable format, which
is the desired symbol of the alphabet in the case of text data. A very simple
example is ASCII, which is basically a table mapping a 7-digit binary no. to
an English letter or symbol.

![ascii_table](http://www.asciitable.com/index/asciifull.gif)

This is still quite popular and in use
(Python 2 uses this encoding for the `str` data type, as we saw above).
ASCII originally was and still is only a 128-symbol encoding (7 bits) but
there are a lot of extended versions to make use of the remaining 128 numbers
left unassigned. So you have accented characters, currency signs and what not
in those extended encodings ([ISO Latin-1](http://www.ascii-code.com/) is one
such example). The problem is that there is no global standard which is
followed for these extended encodings. So a file containing accented
characters written in one standard, might be rendered as something else
entirely on some other computer which uses some other standard.

That's the problem python had with the number 128 (or `0x80`) as one of the
characters in the string. ASCII, encoding used by python 2, has no symbol
mapped to that number. Or any number above 127.

The number 128 stands for the Euro sign(€) in the Latin-1 encoding.
What if some European programmer wanted to print out the Euro sign
in one of his very useful programs which calculates your monthly expenditure.
Or what if a Japanese programmer wanted to output logs in Japanese and not
English? ASCII doesn't have characters for that!

Japanese people came up with their own standards to map japanese symbols,
ended up with 4 different such standards, with no way to interchange between
them and made a mess of the 'Information Interchange' problem ASCII had tried
to solve. We need a standard which:

 - Has support for all possible symbols and languages in use
 - Is followed world-wide
 - Can represent any symbol as 8-bit bytes (called octets in the Unicode specification)

#### Enter Unicode

Unicode is like a mega mega version of ascii. In the simplest sense, what it
does is assign a number to every possible symbol that you would ever want to
display on a screen. These numbers are decided by the Unicode Consortium, a
group of large tech companies who are concerened about text encodings.
From Unicode's [Wikipedia entry](https://en.wikipedia.org/wiki/Unicode):

> The Unicode Standard, the latest version of Unicode contains a repertoire
> of more than 120,000 characters covering 129 modern and historic scripts,
> as well as multiple symbol sets.

Okay so our first 2 criterias are satisfied. We just need to convert these
numbers into an octet format. We could just convert each number to binary,
and split it into how many ever octets are required. Unicode is able to
assign symbols to numbers upto `0x10FFFF` which is 3 octets.
This is a very wasteful way to convert Unicode to octets, because most of
English text files would use 24 bits for each character when one only requires
7 bits. With each character we have 17 redundant bits. This is bad for storage
and data-transfer bandwidths.

Most of the internet today uses a standard called 'UTF-8' for this conversion.
It is an ingenious way which enables one to represent all of Unicode's code points
(numbers mappable to a symbol).

It can be defined using these very simple rules:

 - A byte starting with `0` is a single byte character (`0XXXXXXX`).
 - A byte starting with `110` denotes the starting of a
   two byte character (`110XXXXX 10XXXXXX`)
 - A byte starting with `10` is a continuation byte to a starting byte
   for a character.
 - `1110XXXX` and `11110XXX` denote starting bytes for 3 and 4
   byte long characters. They will be followed by the required continuation bytes.
 - The character's code point is determined by concatenating all the `X`es and reading
   them as a single binary number.
   
It becomes immediately obvious by the single byte characters
that such an encoding supports ASCII and represents it
by default as a single byte. Any valid ASCII file is a valid UTF-8 file.

For an example lets try decoding an emoji character:

```
0xF0 0x9F 0x98 0x81
```

In binary:

**`11110`**`000` **`10`**`011111` **`10`**`011000` **`10`**`000001`

Look how the first byte will tell its a four byte character,
so three continuation bits are to be expected.
Removing the UTF-8 header bits (highlighted ones) and concatenating
the remaining bits:

```
000 011111 011000 000001 = 0x1f601
```

Looking up [U-1f601](http://www.fileformat.info/info/unicode/char/1f601/index.htm)
in the Unicode table we find that it is the grin emoji :D!

Most of the web has moved to using UTF-8. The problem with the python 2 data type
`str` is that we need to explicitely declare it to be the unicode data type if we
want support for special characters. And you need to be extra careful using one
in place of the other, in which case you need to convert them. Else python throws
you that headache of an error because it can't decode a few characters in ascii.

But because UTF-8 is backwards compatible with
ASCII, python 3 uses UTF-8 encoded Unicode as its standard string encoding.
I wonder why we haven't all dumped python 2 in some history archive and
moved to python 3 yet :P! I have had too much of `UnicodeDecode` errors!

#### Credits

This awesome video by Computerphile <3:
[https://www.youtube.com/watch?v=MijmeoH9LT4](https://www.youtube.com/watch?v=MijmeoH9LT4)

#### Other News

I'm anxious for the start of the coding period for GSoC! And I also just launched
my club's new website:
[https://stab-iitb.org/electronics-club/](https://stab-iitb.org/electronics-club/)
which is getting awesome reviews from my friends so I'm kinda happy and excited too!

I also recently read 'The Martian' by Andy Weir, after having watched the really great movie.
The book is atleast 10 times more awesome than the movie!
Its a must read for any hacker, tinkerer and automater!
