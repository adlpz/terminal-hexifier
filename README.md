terminal-hexifier
=================

So it happened to be true that I adopted a new ANSI color map for my Terminal.app.
So great was indeed the pleasure to my eyeballs that I decided to port it to The Desktop,
a Linux machine, that used the Unicode-Rxvt terminal emulator.

But turned to be a fact that Apple hath decided on using a convoluted shitfest to encode those
colors in the exportable pref file, maybe because of fear to them rival cultures or just because
they suck at their jobs, as true was the fact that the colors were encoded in a string of decimals
inside an opaque and undocumented binary struct, which was itself base64-encoded and appended into
a reasonably f*cked up XML plist.

Anyway, fear not for I is here to please you with a quick script that takes any *.terminal* preference
file and spits out a nice set of variables you can add to your .Xdefaults so urxvt looks nice.

If it doesn't work, or you want it for another terminal, or whatever, just fix it yourself, for $deity's sake.