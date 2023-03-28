import unreal

def my_function():
# your python function code here
print("Button Clicked!")

# create a new toolbar button
toolbar_button = unreal.ToolBarButton(
    name="Click Me",
tooltip="Click Me Button",
icon_path="",
group_index=0,
button_type=unreal.ButtonStyle.BUTTONSTYLE_ToolBarButton)

# add the button to the toolbar
unreal.PythonToolbarAPI.get_api().add_tool_bar_button(toolbar_button)

# link the button to your python function
toolbar_button.set_on_clicked_callable(my_function)