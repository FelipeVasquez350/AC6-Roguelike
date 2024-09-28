# Menu documentation, wait wha-
So Fromsoft was kind to us for some reason and instead of writing in code the menu stuff you see in the garage, they decided to use XML files instead, which we can access via WitchyBND very easily :D

In your unpacked game folder go to `menu\menusystem.menubnd.dcx` and unpack it, you'll find a bunch of XML files inside of it, but what we want to open is the `TopMenu.xml` file, which indicates the Layout of the main menu you see in the garage

This can be useful as it lets you set events flags from the menu to trigger EMEVD script, which can be useful for debugging or just to add some extra functionality to the game.


Here's an example of how you can add a button to the menu that triggers an event flag:
```xml
    <Cmd caption = "Trigger EventFlagId 9000" onclick="eventFlag/9000?value=1" />
```

This will add a button to the menu that when clicked will set the event flag 9000 to 1 (you can't go over 4 digits)

Then save the changes, go back to the folder and repack it with WitchyBND, and copy the file that comes out of it in you `/menu` mod folder (me personal advice here is to just copy the entire unpacked folder in that directory and just have witchybnd automatically replace the new version without needing to copy-paste every time)

Then launch the game via modengine2 and you'll find that the menu actually changed :D 