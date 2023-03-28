// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class UGCExampleEditorTarget : TargetRules
{
	public UGCExampleEditorTarget( TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V2;
		ExtraModuleNames.AddRange( new string[] { "UGCExample" } );
	}
}
