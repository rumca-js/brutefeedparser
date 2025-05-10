# Overview

This is a brute-force feed parser.

Why?

 - feedparser doesn’t handle all feeds correctly. I can vividly recall that it could not parse something
 - It has trouble parsing CDATA sections (at least, from what I recall).
 - There were issues using it in threaded or async contexts—warnings or errors would show up.
 - Some parsers can’t handle RSS embedded in HTML, which is unfortunate. I plan to address this... eventually (in Valve time).

This project aims to be a drop-in replacement for [feedparser](https://github.com/kurtmckee/feedparser)

# Installation

```
    $ pip install brutefeedparser
```

# Use

```
reader = BruteFeedParser.parse(contents)
```

# Standards? What standards?

This project does not care about standards. Standards are for loosers. 

Look at me! I am the standard now!

You can quote me on the thing below:
```
If the problem is a nail and your hammer fails, perhaps it's time to reach for a bigger one.
```

# Disclaimer

This project contains code so questionable that at least one line could cause Linus Torvalds to spontaneously combust.

Reading the code in large doses may result in dizziness, despair, or the sudden realization that tabs vs. spaces was the least of your problems.

Keep the code far away from any seasoned kernel developers.

Pasting any part of this into a Linux kernel mailing list may trigger several years of flame wars, philosophical debates, and intergenerational feuds among programming factions.

Proceed with caution. Or better yet — just don’t.
