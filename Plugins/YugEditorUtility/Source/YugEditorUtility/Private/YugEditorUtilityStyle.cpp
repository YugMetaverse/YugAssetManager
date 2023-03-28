// Copyright Epic Games, Inc. All Rights Reserved.

#include "YugEditorUtilityStyle.h"
#include "YugEditorUtility.h"
#include "Framework/Application/SlateApplication.h"
#include "Styling/SlateStyleRegistry.h"
#include "Slate/SlateGameResources.h"
#include "Interfaces/IPluginManager.h"
#include "Styling/SlateStyleMacros.h"

#define RootToContentDir Style->RootToContentDir

TSharedPtr<FSlateStyleSet> FYugEditorUtilityStyle::StyleInstance = nullptr;

void FYugEditorUtilityStyle::Initialize()
{
	if (!StyleInstance.IsValid())
	{
		StyleInstance = Create();
		FSlateStyleRegistry::RegisterSlateStyle(*StyleInstance);
	}
}

void FYugEditorUtilityStyle::Shutdown()
{
	FSlateStyleRegistry::UnRegisterSlateStyle(*StyleInstance);
	ensure(StyleInstance.IsUnique());
	StyleInstance.Reset();
}

FName FYugEditorUtilityStyle::GetStyleSetName()
{
	static FName StyleSetName(TEXT("YugEditorUtilityStyle"));
	return StyleSetName;
}


const FVector2D Icon16x16(16.0f, 16.0f);
const FVector2D Icon20x20(20.0f, 20.0f);

TSharedRef< FSlateStyleSet > FYugEditorUtilityStyle::Create()
{
	TSharedRef< FSlateStyleSet > Style = MakeShareable(new FSlateStyleSet("YugEditorUtilityStyle"));
	Style->SetContentRoot(IPluginManager::Get().FindPlugin("YugEditorUtility")->GetBaseDir() / TEXT("Resources"));

	Style->Set("YugEditorUtility.PluginAction", new IMAGE_BRUSH_SVG(TEXT("PlaceholderButtonIcon"), Icon20x20));
	return Style;
}

void FYugEditorUtilityStyle::ReloadTextures()
{
	if (FSlateApplication::IsInitialized())
	{
		FSlateApplication::Get().GetRenderer()->ReloadTextureResources();
	}
}

const ISlateStyle& FYugEditorUtilityStyle::Get()
{
	return *StyleInstance;
}
