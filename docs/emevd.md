# EMEVD Documentation

I have no idea what EMEVD even stands for but who cares here's some docs

Like for ESD, at the moment there are no official tools for EMEVD editing, so you'll have to do it programmatically using the [Soulsformats](https://github.com/soulsmods/SoulsFormatsNEXT) library.

Also you'll need to use the [ELDEN RING'S EMEDF for DarkScript3](https://soulsmods.github.io/emedf/er-emedf.html) as there's no version for AC6 yet, which contains the definitions for the EMEVD instructions, most of which work but not all of them (like GiveItemDirectly, which is implemented in ESD)

For some examples on how to use the library you can check [my edits](../EMEVD_Edits.cs)

Its important to mention that setting event flags during a mission won't carry over when going back to the garage, so if you want to have a way to check later for some condition i suggest to give the player some invisible items that you can later detect in the game via `IfPlayerHasdoesntHaveItem` 