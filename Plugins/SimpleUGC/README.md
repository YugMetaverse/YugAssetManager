# SimpleUGC plugin and UGCExample for *Unreal Engine 5*

-----

## NOTE:
**This is a port/migration of the original *SimpleUGC* plugin and sample, that was made for *Unreal Engine 4*, to work with *Unreal Engine 5*.**

- The original was made by Epic / the guys from Robo Recall - so all credit for the actual work goes there!
- "Only" the port/migration of the original plugin and sample to work with UE5 has be done by me, [**Michael a.k.a. "Hellcat"**](https://twitter.com/TheRealHellcat) from the [**Spaceflower**](https://twitter.com/SpaceflowerDE) studio.

While, at the time of writing these lines, everything that worked on UE4 should now also work on UE5, with this version, please consider this still to be

==>> **WORK IN PROGRESS :-)** <<==

All the original documentation should still apply, with one exception: I changed the UGC registry to be a subsystem - check the sample on how to use it.

Also, something that does not work (didn't on the original UE4 version, already) is putting C++ code into mods - THAT is something I'd **LOVE** to add, so if you have any tips on how to get built C++ code packaged into mods, PLEASE let's talk about this!

### The future of *Hellcat's SimpleUGC port for UE5*

I plan to keep working on this some more, there's a few ideas of things and features I might wanna add, tweak other things to make them more stable, usable or fix them to work at all, etc.

One of the first things to come is to change the UAT calls for packaging the mods, so a source build of the engine won't be needed, anymore, and some configurability for the supplied mod templates of your modkit.

So, yah, we're not done here, yet - if you like this, feel free to get in touch via the Twitter links above and/or on the Unreal Developer Community forum.

-----

# /!\ ATTENTION:
## **The documentation is incorrect in some places in regards to this UE5 version of the plugin!**
**I haven't gotten to update the documentation, yet!**

Here's some noteworthy differences:

- The UAT extensions (that used to be in the *Build/Scripts* folder) are NOT needed anymore (and have thus been deleted)! **No source build of the engine is required, anymore!** :-)
- The UGC registry has been moved into a subsystem, a custom GameInstance is no longer needed.
- The *AssetRegistry.bin* in the *Releases* folder goes into a *"Windows"* subfolder, not *"WindowsNoEditor"*.
- The directory under ".../Releases" is no longer hard coded and determined automatically based on where the packager finds an "AssetRegistry.bin", i.e. if you properly set up your releases directory, it'll automatically be found, no matter it's name.
- Mod templates are now automatically read from the templates directory for populating the "new mod" dialog; you can also add a .TXT file (same name as the template dir plus .txt extension) to customize the shown name and description (see sample template).

-----

# UGC (original docs)

The **UGC** (user-generated content) **Example** project is a custom plugin and build scripts created to facilitate adding mod support to **~~Unreal Engine 4~~** **Unreal Engine 5** titles. 

Loosely based on the work done for Robo Recall, It includes:

- A runtime game module for game integration
- An editor module for new toolbar buttons and commands
- An AutomationTool project for packaging mods
- An example ~~UE4~~ UE5 project demonstrating all aspects working together. 

Follow the [**Quick Start Guide**](Documentation/QuickStart.md) for a comprehensive look at the UGC Example project and for instructions to add mod support to your own projects.
