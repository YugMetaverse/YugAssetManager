import unreal

def getAssetsFromPath(path, bRecursive):
    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    #unreal.EditorAssetLibrary.make_directory(path+'/myFolder')

    for asset in assets:
        assetPath = unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name)
        print(unreal.StringLibrary.conv_name_to_string(asset.asset_name) + " - " + unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name) + " :: " + unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name) + "'" + unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name) + "'")

        if(asset.asset_class_path.asset_name == "PrimaryAssetLabel"):
            primaryAssetLabel = asset.get_asset()
            print(primaryAssetLabel.get_editor_property('rules').get_editor_property('chunk_id'))

def getAssetDependencies(path, bRecursive):
    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    for asset in assets:
       assetPath = unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name)

       if(asset.asset_class_path.asset_name != "PrimaryAssetLabel" and asset.asset_class_path.asset_name != "Material" and asset.asset_class_path.asset_name != "Texture2D"):
        print(asset_reg.get_dependencies(assetPath, unreal.AssetRegistryDependencyOptions()))  # Returns the assets that are referenced by 'this' asset
        # print(asset_reg.get_referencers(assetPath, unreal.AssetRegistryDependencyOptions())) # Returns Assets that reference 'this' asset

# getAssetsFromPath('/YugPreLoader/MyAssets', True)
getAssetDependencies('/YugPreLoader/MyAssets', True)