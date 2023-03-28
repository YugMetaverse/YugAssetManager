// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Framework/Commands/Commands.h"
#include "YugEditorUtilityStyle.h"

class FYugEditorUtilityCommands : public TCommands<FYugEditorUtilityCommands>
{
public:

	FYugEditorUtilityCommands()
		: TCommands<FYugEditorUtilityCommands>(TEXT("YugEditorUtility"), NSLOCTEXT("Contexts", "YugEditorUtility", "YugEditorUtility Plugin"), NAME_None, FYugEditorUtilityStyle::GetStyleSetName())
	{
	}

	// TCommands<> interface
	virtual void RegisterCommands() override;

public:
	TSharedPtr< FUICommandInfo > PluginAction;
};
