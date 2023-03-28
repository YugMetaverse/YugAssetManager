// Copyright Epic Games, Inc. All Rights Reserved.

#include "YugEditorUtility.h"
#include "YugEditorUtilityStyle.h"
#include "YugEditorUtilityCommands.h"
#include "Misc/MessageDialog.h"
#include "ToolMenus.h"

static const FName YugEditorUtilityTabName("YugEditorUtility");

#define LOCTEXT_NAMESPACE "FYugEditorUtilityModule"

void FYugEditorUtilityModule::StartupModule()
{
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module

	/* This initializes the Editor Style and registers it with the Slate Style Registry */
	FYugEditorUtilityStyle::Initialize();

	/* This registers the Editor Style Set with the Slate Style Registry */
	FYugEditorUtilityStyle::ReloadTextures();

	/*
	 * We Register our Command with Engine and
	 * then bind it UI Command Variable called as Plugin Actions
	 * 
	 */
	/* This registers our commands with the engine */
	FYugEditorUtilityCommands::Register();
	/* This creates a new UI Command List */
	PluginCommands = MakeShareable(new FUICommandList);
	/* This maps our commands to the UI Command List */
	PluginCommands->MapAction(
		FYugEditorUtilityCommands::Get().PluginAction,
		FExecuteAction::CreateRaw(this, &FYugEditorUtilityModule::PluginButtonClicked),
		FCanExecuteAction());
	
	/* This registers the callback for the menu */
	UToolMenus::RegisterStartupCallback(FSimpleMulticastDelegate::FDelegate::CreateRaw(this, &FYugEditorUtilityModule::RegisterMenus));
}

void FYugEditorUtilityModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.

	UToolMenus::UnRegisterStartupCallback(this);

	UToolMenus::UnregisterOwner(this);

	FYugEditorUtilityStyle::Shutdown();

	FYugEditorUtilityCommands::Unregister();
}

void FYugEditorUtilityModule::PluginButtonClicked() const
{
	// Put your "OnButtonClicked" stuff here
	const FText DialogText = FText::Format(
							LOCTEXT("PluginButtonDialogText", "Add code to {0} in {1} to override this button's actions"),
							FText::FromString(TEXT("FYugEditorUtilityModule::PluginButtonClicked()")),
							FText::FromString(TEXT("YugEditorUtility.cpp"))
					   );
	FMessageDialog::Open(EAppMsgType::Ok, DialogText);
}

void FYugEditorUtilityModule::RegisterMenus()
{
	// Owner will be used for cleanup in call to UToolMenus::UnregisterOwner
	FToolMenuOwnerScoped OwnerScoped(this);

	{
		UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Window");
		{
			FToolMenuSection& Section = Menu->FindOrAddSection("WindowLayout");
			Section.AddMenuEntryWithCommandList(FYugEditorUtilityCommands::Get().PluginAction, PluginCommands);
		}
	}

	{
		UToolMenu* ToolbarMenu = UToolMenus::Get()->ExtendMenu("LevelEditor.LevelEditorToolBar.PlayToolBar");
		{
			FToolMenuSection& Section = ToolbarMenu->FindOrAddSection("PluginTools");
			{
				FToolMenuEntry& Entry = Section.AddEntry(FToolMenuEntry::InitToolBarButton(FYugEditorUtilityCommands::Get().PluginAction));
				Entry.SetCommandList(PluginCommands);
			}
		}
	}
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FYugEditorUtilityModule, YugEditorUtility)