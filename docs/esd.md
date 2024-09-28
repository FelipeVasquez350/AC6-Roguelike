# ESD Documentation
As of writing there are no official tools for esd editing, therefore this is a guide for the few who dare to still go though it and myself in a few months when I forget how to do it.

## How to
First download the following repo:
- [ESDLang](https://github.com/FelipeVasquez350/ESDLang) My fork of ESDLang with some edits to make it work with ac6, this was possible only thanks to the work done byy thefifthmatt during one of his streams.

Then you just need to follow the original guide from the ESDLang repo in order to extract and repack the esd files.

- [TKGP's doc](https://docs.google.com/document/d/1wQxPBk8R73Tweu86woXm_U2fHhe9oJh5MXymLa9rMB4) This is a collection of notes from TKGP regarding some functions of esd.

## Notes

The "main function" `def t001000000_0():` seems to be running all the time, it is the main loop of the esd file.

Instead `def t001000000_1000():`only runs once when the player enters the garage, so for example from here you can set some events that apply changes that should only happen once given a condition.

A limitation given by the game is that you can't have very long or complex functions if they take considerable time, otherwise you'll just break the game and be stuck in the garage forever.

A very useful tip regarding debugging is to constantly compare the original edit of the file and the decompiled version after you applied the changes to the original file, this way you can see if you made any mistakes or of the compiler "corrected" some inaccuracies in your code (for example calling a function and expecting to wait until it expires without using assert).

Also if you try to have a function that communicates back and forward with EMEVD, like setting a certain flag, try to give the esd script a loooooong span of time to execute (like at the beginning of `t001000000_1000():`), otherwise the game will probably go over with before the EMEVD script can go over it.