# import unreal
# 
# def my_function():
#     print("Button Clicked!")
# 
# # create a new toolbar button
# toolbar_button = unreal.ToolBarButton(
#     name="Click Me",
#     tooltip="Click Me Button",
#     icon_path="",
#     group_index=0,
#     button_type=unreal.ButtonStyle.BUTTONSTYLE_ToolBarButton)
# 
# # add the button to the toolbar
# unreal.PythonToolbarAPI.get_api().add_tool_bar_button(toolbar_button)
# 
# # link the button to your python function
# toolbar_button.set_on_clicked_callable(my_function)

# import unreal
# 
# 
# print("Creating Menus!")
# menus = unreal.ToolMenus.get()
# 
# # Find the 'Main' menu, this should not fail,
# # but if we're looking for a menu we're unsure about 'if not'
# # works as nullptr check,
# main_menu = menus.find_menu("LevelEditor.MainMenu")
# if not main_menu:
#     print("Failed to find the 'Main' menu. Something is wrong in the force!")
# 
# print("Creating Menu Entry!")
# 
# entry = unreal.ToolMenuEntry(
#     name="Python.Tools",
#     # If you pass a type that is not supported Unreal will let you know,
#     type=unreal.MultiBlockType.MENU_ENTRY,
#     # this will tell unreal to insert this entry into the First spot of the menu
#     insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
# )
# entry.set_label("YourMenuItemName")
# # this is what gets executed on click
# entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, custom_type='Test', string=("from bitbake import build;build()"))
# script_menu = main_menu.add_sub_menu(main_menu.get_name(), "BitCakeTools", "BitCake", "BitCake")
# # add our new entry to the new menu
# script_menu.add_menu_entry("Scripts",entry)
# # refresh the UI
# menus.refresh_all_widgets()
