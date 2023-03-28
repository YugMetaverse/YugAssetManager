// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class UGCExampleTarget : TargetRules
{
	public UGCExampleTarget( TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V2;
		ExtraModuleNames.AddRange( new string[] { "UGCExample" } );
	}
}
