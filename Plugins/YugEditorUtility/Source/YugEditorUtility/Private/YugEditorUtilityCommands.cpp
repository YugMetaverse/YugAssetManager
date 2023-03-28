// Copyright Epic Games, Inc. All Rights Reserved.

#include "YugEditorUtilityCommands.h"

#define LOCTEXT_NAMESPACE "FYugEditorUtilityModule"

void FYugEditorUtilityCommands::RegisterCommands()
{
	UI_COMMAND(PluginAction, "YugEditorUtility", "Execute YugEditorUtility action", EUserInterfaceActionType::Button, FInputChord());
}

#undef LOCTEXT_NAMESPACE
