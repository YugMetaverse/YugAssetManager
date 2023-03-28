# UGC Example Quick Start
## Prerequisites
To follow along with this overview, you’ll need the following installed on your machine: 
- A source build of Unreal Engine 4.25.1 or higher (to recompile the AutomationTool project)
- Visual Studio 2019 Community or higher. Ensure you have the Visual Studio .NET desktop development component installed. 
- This project (UGCExample)

*If you’re comfortable in Visual Studio and want to skip looking at the example project, head straight to the [Adding Mod Support to Your Project](https://github.com/EpicGames/UGCExample/blob/release/Documentation/QuickStart.md#adding-mod-support-to-your-project
) section below.*
### Building the UGC Example Project
Before opening the UGC Example project, follow these steps to ensure everything is generated and built for the project:

1. Place the UGCExample project in a directory under your UE4 root directory (such as /Games or /Projects) and add the directory to **UE4Games.uprojectdirs** using your favorite text editor. Save this file.

![image](/Documentation/Images/image68.png)

![image](/Documentation/Images/image69.png)

![image](/Documentation/Images/image70.png)

2. Run **GenerateProjectFiles.bat** in your UE4 root directory.
3. Open **UE4.sln**.
4. If you haven't yet, build the **UE4** and **UnrealPak** projects. 
5. Verify that the build scripts are listed in the **Programs/Automation** directory

![image](/Documentation/Images/image13.png)

6. Open **Properties** for **SimpleUGC.Automation** and choose the **Build** tab on the left. Set the **Output Path** to your source build's **Engine\Binaries\DotNET\AutomationScripts\\** directory for **both Development and Debug Configurations**. The "Browse..." button makes this easy.

![image](/Documentation/Images/image71.png)

7. **Build** the **AutomationTool** project. 
8. **Build** the **UGCExample** project in the **Development** configuration.
9. **Build and run** the **UGCExample** project in the **Development Editor** configuration.
## UGC Example Project 
### Project Overview 
The UGC Example project is pretty basic. It has two Levels, a handful of Blueprints, and an example mod menu UI. 

![image](/Documentation/Images/image28.png)

If we use play-in-editor (PIE), we will go to the **MainMenu** Level that shows the available UGC packages (none as yet), and allows us to open **ExampleMap**.

![image](/Documentation/Images/image6.png)

**ExampleMap** isn’t much more sophisticated, and only has two different spawned Actors invoked by the Level Blueprint. 

![image](/Documentation/Images/image15.png)

On the toolbar, you’ll see the two new buttons mentioned above—**Create UGC** and **Package UGC**. Let’s see how they work. 
## Making a New Mod
### Creating a New Mod Plugin
Clicking the toolbar button **Create UGC** will open a wizard that you can use to generate a new UGC package. It generates a new content-only plugin (no C++ code modules), and places it in your **Mods** directory.

**NOTE**: In 4.25.0, mods are placed in the **Plugins** directory. We recommend upgrading to at least 4.25.1, or move the newly-created folder from Plugins to Mods in order for this to properly work! 

Give it a name, add your info, then click **Create Mod**.

![image](/Documentation/Images/image34.png)

The Content Browser view of the new Mod plugin will open, and you can add your content. You can add this folder to your favorites to more easily find it later.

![image](/Documentation/Images/image31.png)

I’ve added a simple Level based on the StarterContent Level **Minimal_Default**, a Blueprint Actor called **SilverBall**, and a Material, **SilverBallMat**, for our new object. 

SilverBall is an Actor with a scaled Sphere Component that has **Simulate Physics** checked and the SilverBallMat applied to the mesh. I’ve placed one in the Level, so when it is run, I can see it fall to the ground.

![image](/Documentation/Images/image14.png)

![image](/Documentation/Images/image1.png)

This is pretty basic, but we are now able to find this UGC package and play this new Level that uses the new Actor and Material in editor via the **UGCRegistry** functions. 

Let’s see how to test it in the main game using PIE. 
### Testing the New Mod
Open the **MainMenu** Level if it's not already open. When we start a PIE session, our new UGC shows up in the list of **UGC Packages**. That’s because the list is populated by plugins classified as **Mods** and located in the Mods project directory.

![image](/Documentation/Images/image21.png)

From here, we can select **Open** for your newly created level (mine was called NewTestLevel), then play the new Level in the editor. 

![image](/Documentation/Images/image25.png)

We’ve now shown a basic way to load a new Level (and the content associated with it) using PIE and some menu helpers. But what if we wanted the SilverBall Actor to be available for use inside the main game in traditional mod style?
### Overriding the Base Game
The Simple UGC module has two Components that make in-game object replacement pretty straightforward. If you take a look at the Sphere Actor, you’ll see a **MakeReplaceableActor** Component on it.

![image](/Documentation/Images/image33.png)

![image](/Documentation/Images/image12.png)

This explicitly makes the SphereActor replaceable by user-generated content. In the Details panel, you’ll see a field for Compatible Replacement. This defines what type of Actor can replace it, as there may be compatibility concerns when swapping one Actor for another, and this must be set if you intend to make a Class overridable. For Robo Recall’s guns, for instance, this would be OdinGun, as most of the game called and reacted to functions or properties on OdinGun. For demonstration purposes, SphereActor just uses Actor as our Compatible Replacement base.

Now that we’ve managed to tell the game’s base class that it can be overridden by a mod, let’s make the SilverBall an override for that class. 

In the same vein as adding a **MakeReplaceableActor** Component to the original Class, let’s add a **ReplacementActor** Component to the Class we expect to replace it (the SilverBall) when the mod is active. 

![image](/Documentation/Images/image32.png)

Here, you’ll see that we have an **Actor Classes To Replace** array in the Details panel. This is where we define what this class is supposed to replace in the main game. I’ve added SphereActor to the list so that SilverBall knows to register itself as a replacement for SphereActor when our new mod is active. 
### Testing the Override Mod
If we PIE now, we can see ActorReplacements in the list and our SilverBall_C Blueprint class in the list. 

![image](/Documentation/Images/image8.png)

Clicking **Apply** or **Apply All** on the Class or on the Actor Replacements header will register the override, which is reflected in the **Registered Overrides** list. 

![image](/Documentation/Images/image39.png)

If we click **Open Example Map** now, we’ll see that SilverBall has replaced SphereActor in the Level.

![image](/Documentation/Images/image30.png)

This is an example of how to test Actor replacement in the editor before the mod is ready to ship. When everything is as desired, we can package the UGC using the second new toolbar button, **Package UGC**.
### Packaging Your New Mod
Packaging is a one-touch operation using the **Package UGC** option in the toolbar. If we click the button and select our mod from the list, a directory dialog opens for choosing where to save our UGC.

![image](/Documentation/Images/image18.png)

Afterwards, you’ll see a status indicator in the bottom right corner of the editor. 

![image](/Documentation/Images/image20.png)

![image](/Documentation/Images/image4.png)

Once complete, the cooked mod will be in a zipped folder where you saved to. 

![image](/Documentation/Images/image24.png)

## Playing Your New Mod
Now you can test your UGC in the actual game. We have included a zip of the packaged game for this purpose. 
### Running the Game
Head over to **UGCExample/Releases/UGCExampleGame_v1** and copy **PackagedExe.zip** to somewhere convenient. Unzip the PackagedExe.zip and you can run the (thrilling) game from the UGC Example project.

![image](/Documentation/Images/image3.png)

Run **UGCExample.exe**. 

As expected, there are no UGC Packages found. Let’s add the new mod. 
### Adding Your Packaged UGC to the Base Game
Extract your packaged mod to somewhere convenient. Copy the folder containing Content and the .uplugin file into a new Mods directory in the **UGCExample** game folder that you just extracted. Here’s what mine looks like:

![image](/Documentation/Images/image9.png)

_UGCExample game folder—note the Mods directory._

![image](/Documentation/Images/image10.png)

_MyFirstMod folder and contents in the Mods folder._

Now, when you play the game, you should see the UGC package show up in the list, with the content now made available the same way it was in the editor!
## Adding Mod Support to Your Project
### Project and Environment Setup
Now that you’ve seen how everything works together, let’s take a look at the pieces you need to add the same type of mod support to your games. **Note**: In order for the build scripts to be added to the AutomationTool, your project needs to be a code project. If it's currently a Blueprint only project, you can convert it by adding a new C++ class in the Content Browser. 

The majority of the heavy lifting takes place in the **SimpleUGC** plugin (found in **UGCExample/Plugins**.) This plugin contains two modules: **SimpleUGC** and **SimpleUGCEditor**.

![image](/Documentation/Images/image2.png)

SimpleUGC is a runtime module that includes Classes, Components, and functions that make it easy to find and use new content found in mods in your base game. Detailed information about these Classes can be found later on in this document.

![image](/Documentation/Images/image23.png)

The SimpleUGCEditor Editor module adds two toolbar and File menu dropdown buttons that automate the creation and packaging of mods, as well as a templates folder for populating the **New Mod Creation Wizard**.

![image](/Documentation/Images/image35.png)

The other important piece of the puzzle is the custom AutomationTool project found in the project, **SimpleUGC.Automation**. The important file here is **PackageSimpleUGCPlugin.cs**, which contains the command required to package our mods. 

![image](/Documentation/Images/image13.png)

Copy the following directories from the UGC Example to the same locations in your project: 

**UGCExample/Plugins/SimpleUGC**:

![image](/Documentation/Images/image29.png)

**UGCExample/Build/Scripts**:

![image](/Documentation/Images/image26.png)

If you went through the example above, you may need to remove the UGC Example project and **Rebuild the AutomationTool** project after you generate project files to ensure that there are no conflicts with the two SimpleUGC.Automation instances.

Alternatively, you can refactor the names in these build scripts to match your project as you’re likely going to make a number of project-specific changes by the time you ship your mod kit.

Take these steps for your project (just like above, see images for references):

1. Place your project in a directory under your UE4 root directory (such as /Games or /Projects) and add the directory to **UE4Games.uprojectdirs** using your favorite text editor. Save this file.

**NOTE**: If you cannot move your project's location for one reason or another, skip this step and move the SimpleUGC.Automation project and scripts to your Engine directory as oulined in the <a href="https://docs.unrealengine.com/en-US/Programming/BuildTools/AutomationTool/HowTo/AddingAutomationProjects/index.html" target="_blank">Adding Automation Projects documentation</a>.

2. Run **GenerateProjectFiles.bat** in your UE4 root directory.
3. Open the **Visual Studio solution**.
4. If you haven't yet, build the **UE4** and **UnrealPak** projects. 
5. Verify that the build scripts are listed in the **Programs/Automation** directory
6. Open **Properties** for **SimpleUGC.Automation** and choose the **Build** tab on the left. Set the **Output Path** to your source build's **Engine\Binaries\DotNET\AutomationScripts\\** directory for **both Development and Debug Configurations**. The "Browse..." button makes this easy.
7. **Build** the **AutomationTool** project.
8. **Build your project** in the **Development** configuration.
9. **Build and run your project** in the **Development Editor** configuration.

### Custom Game Instance
For discovering mod packages and tracking overrides, we need a place to create and store the UGCRegistry Class. We do this in a custom **GameInstance** Class, as GameInstance gets created early enough that mod packages can become available before the first UE4 Level is on the screen, but late enough that all content plugin packages have been mounted and are ready for use. 

If you are not using a custom GameInstance, select **UGCBaseGameInstance** in the **Maps and Modes** section inside **Project Settings**.

![image](/Documentation/Images/image11.png)

If you are using a custom GameInstance, reparent it to UGCBaseGameInstance in order for the UGCRegistry to be created and made available for use in your game.
### Making Actors Replaceable
For Actors in your game that you want to make replaceable by UGC, you’ll need to add a MakeReplaceableActor Component to the Actor. 

![image](/Documentation/Images/image19.png)

In the Details panel, you’ll see a field for **Compatible Replacement**. This defines what types of Actors are able to replace this Class when they’re registered as mod overrides. This should be a common base Class shared by the Actor you want to be replaced by a mod Class and the mod Class trying to replace it. 

![image](/Documentation/Images/image38.png)

For instance, in Robo Recall, we knew that OdinGun was the super Class that all guns derived from. When we would call events to fire, reload, drop, or throw guns, we called that functionality on OdinGun. If we were to add this Component to any original guns in the game, we would add OdinGun as the Compatible Replacement to ensure that new guns that replace original guns remain compatible with the assumptions that the game code makes.
### Handling Class Swapping
Now that an Actor knows that it can be replaced by certain types of new Actors, we need to ensure that we handle the replacement logic whenever the Actor is supposed to spawn. 

Where you spawn Actors that can be overridden instead of passing the Class straight into **SpawnActorFromClass**, call **GetOverrideForActorClass** on the UGCRegistry and pass the Class type in as the **ActorClass** parameter. This will return the original class if no valid overrides are registered, or the replacement class if an override has been registered.

![image](/Documentation/Images/image22.png)

### Avoiding Placed Actors
In the effort to keep this plugin simple and avoid any low-level engine changes, it does not support the replacement of Actors placed in Levels. That action would be better handled in the Level loading code instead, as it can be very expensive to tear down a bunch of instantiated Actors with Components just to recreate them in a timely manner before the player spawns into the Level. 

We encourage you to replace any placed Actors with spawning logic for performance reasons. In situations where you absolutely cannot spawn an Actor and it must be placed, you can perform the UGCRegistry check in the Level Blueprint and handle the replacement if necessary. We had to do this for the Robo Recall boss due to an issue with loading order for cinematics.
### Special Case for Player Pawn
Since player Pawn spawning is handled by the **GameMode** class, we can employ the same method for Actor replacement in our GameMode Class. Overriding **GetDefaultPawnClassForController** allows us to manage the class replacement logic like so:

![image](/Documentation/Images/image36.png)

### Add Methods to Find and Consume UGC
You will need to add mechanisms to discover and use UGC in your game. This could appear in many forms, such as a mods menu (as in Robo Recall), or systems that crawl new packages looking for new Assets of a certain type to use in existing systems. 

In general, it’s important to remember that mods are just big lumps of extra content, and it is up to you, the game’s creator, to decide how it best fits into your world. 

The UGC Example project has some examples of use in a mod menu, but here are some UGCRegistry properties and functions that will help you along the way: 

|  Name | Description |
| ----------- | ----------- |
| UGCPackages | Array of found UGC Packages. This is populated when UGCBaseGameInstance is initialized. |
| GetAllClassesInPackage | Returns all new classes in the UGC Package provided. This includes Classes with and without ReplacementActor Components for overrides. |
| GetMapsInPackage | Returns all Maps (Levels) found in a package. NOTE: This will even return Levels that you only intend to use as sublevels, so you should add special filtering on your map names if you want modders to make only certain Levels available. |
| GetActorClassesWithReplacementActorComponentsInPackage | Only returns Actor Classes that have ReplacementActorComponents on them, meaning they are meant to override the original game. |
| ApplyAllOverridesInPackage | Registers overrides for all Classes with ReplacementActorComponents in the UGC Package provided. |
| ApplyOverridesForActorClass | Like ApplyOverridesForActorClass, but just registers Overrides for the Actor Class passed in. |
| ClearOverrideForClass | Removes the override that is registered for the origin Class passed in. |
### Packaging UGC Setup
Now that your game supports newly discovered packaged mods, you’ll need to prepare the editor environment for mods to be appropriately created, packaged and distributed. There are a few things required to make this work. 
#### Asset Registry from Packaged Game
Mods for packaged games require a packaged game, right? 

When your game is packaged, you’re going to need a few files generated and stored in the project **Saved** directory. This is needed in the UGC packaging step so it’s generating the appropriate data for the appropriately supported release of the game. 

The files you need are the **AssetRegistry.bin** and the **Metadata** folder found in **Saved/Cooked/WindowsNoEditor/<ProjectName>**

![image](/Documentation/Images/image17.png)

Make a new **Releases** directory in your project root. Inside it, add another folder for your supported release. The name of this folder is important, as this directory will be referenced by your packaging script. For the UGC Example project, I just named it **UGCExample_v1** to keep things simple. Inside that folder, add a **WindowsNoEditor** folder and put the AssetRegistry.bin and the Metadata folder copied from the Saved/Cooked directory inside.

![image](/Documentation/Images/image16.png)

Best practice is to have this accounted for in your build system so that it would generate this folder and copy these over for you. It is currently hardcoded in our example as we anticipate that everyone is going to have slightly different needs and tools for this process. 
#### Updating Packaging Scripts
For the sake of simplicity, for the UGCExample project, we hardcoded the project's release folder name. If you copied the SimpleUGC plugin and SimpleUGC automation scripts into your own project then you'll need to change a couple places in code.

The hardcoded "UGCExampleGame_v1" folder name is referenced in by two variables in code:
- ReleaseVersion in **SimpleUGCPackager.cpp** (line 109)
- ReleaseVersion in **PackageSimpleUGCPlugin.cs** (line 38)

These strings must match the name of the Releases sub-folder that you created in the previous step. If you change these strings, make sure rebuild your projects in Visual Studio -- both **AutomationTool** and **your project**.

As mentioned above, ideally, these are read from an area that is generated by your build system (such as an .ini file) whenever you are preparing your editor for release. We left this hardcoded here so as to not be presumptive of your setup.

At this point, you have everything moved over and you can test. Remember to add **ReplaceableActorComponents** to new Actors you want to override original content with, and set the properties as mentioned above!
### Further Customization
Now that you’re up and running, let’s take a look at a few things you might want to customize for your game. 
#### Templates
The New Mod Wizard pulls from a Templates folder in the SimpleUGC plugin. We’ve included an empty, content-only plugin as a starting point. If you look over at the source for Robo Recall, you’ll see that we have a bunch of starting templates that have jumping-off points for creating new types of mods. You will want to account for these in the custom **IPluginWizardDefinition** in the SimpleUGCEditor module so that they properly populate in the list of templates. See the Robo Recall source for a good reference on how that can be handled.

![image](/Documentation/Images/image27.png)

#### Icons
Replace our basic icons out and add your own to flavor to your mod editor! These are found in the **Resources** folder in the SimpleUGC plugin. 

![image](/Documentation/Images/image5.png)

#### Other Asset Types
All Assets inside each UGC package get added into the mod .pak file when we package. These are available for use as soon as the game runs, though the current UGCRegistry Class has helper functions for handling Class and Level discovery. If you want to provide easier access to other Asset types such as materials, textures, and sounds, **UUGCRegistry::GetMapsInPackage** is a good reference for how you can crawl package paths for specific Asset types. Instead of adding **UWorld::StaticClass()->GetFName()** to the **ARFilter.ClassNames**, add the type that you’d like to filter for.
