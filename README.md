# flappy.ps: Flappy Bird in PostScript

![Flappy Screenshot](screenshot.png?raw=true)

This was my entry for Devnology's CodeFest 2016. The objective was to write
Flappy Bird in your favorite uncommon or esoteric programming language.

Always up to a challenge, and wanting to up my concatenative language skills,
I did it in PostScript.

Notes to future historians: I'm not an experienced PostScript programmer! I just
threw something fun together for a coding challenge. My PostScript style is
probably completely crap, so don't try to learn anything from this code, maybe
other than a curiosity.

![(Short Presentation)](flappy_presentation.pdf?raw=true)

## How to run it

You'll need GhostScript (obviously). Then run

    ./run flappy.ps

To see pages rendered live (pressing ENTER all the while), or run

    ./export flappy.ps

To export to a PDF and viewing that in your favorite PDF viewer.

## How it works

Every frame of the game is rendered as a separate page in the output.

The locations of the pipes are generated based off a random seed you'll find at
the top of the file:

    /level 3582 def

Because PostScript has no user input, the frame numbers of where the user 
is going to jump are part of the program. Edit this to advance in the level
(hopefully):

    /jumps [
        30 35
    ] def

The game will then into a loop where the scene is drawn using various 
PostScript drawing commands, and the physics are calculated to update
Flappy's position.
