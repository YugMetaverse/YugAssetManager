// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

class FToolBarBuilder;
class FMenuBuilder;

class FYugEditorUtilityModule : public IModuleInterface
{
public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
	
	/** This Function is Called When the Plugin Button is Clicked */
	void PluginButtonClicked() const;
	
private:

	/* This Function Registers the Menu Button */
	void RegisterMenus();


private:
	/* This Holds the Reference to Plugin Commands */
	TSharedPtr<class FUICommandList> PluginCommands;
};
