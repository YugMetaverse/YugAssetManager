import unreal

def createDataAsset(path, assetName, chunkId):
    # Get asset tools
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
 
    # Creates a Level Sequence - /Game/Test_LS
    primary_label = unreal.AssetTools.create_asset(asset_tools, asset_name = assetName, package_path = path, asset_class = unreal.PrimaryAssetLabel, factory = unreal.DataAssetFactory())

    custom_rule = primary_label.get_editor_property('rules')
    custom_rule.set_editor_property('chunk_id', chunkId)
    custom_rule.set_editor_property('apply_recursively', True)
    custom_rule.set_editor_property('cook_rule', ALWAYS_COOK)

    primary_label.set_editor_property('rules', custom_rule)
    primary_label.set_editor_property('label_assets_in_my_directory', True)


def getAssetsFromPath(path, bRecursive):
    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    #unreal.EditorAssetLibrary.make_directory(path+'/myFolder')

    for asset in assets:
        assetPath = unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name)
    #you could use isinstance unreal.SkeletalMesh, but let's build on what we learned
        if(unreal.EditorAssetLibrary.does_directory_exist(assetPath) == False):
            unreal.EditorAssetLibrary.make_directory(assetPath)
            unreal.EditorAssetLibrary.rename_asset(assetPath, assetPath + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
            createDataAsset(assetPath + "/", "Chunk_" + unreal.StringLibrary.conv_name_to_string(asset.asset_name), unreal.MathLibrary.random_integer_in_range(1000, 5000))
            #print(assetPath + " ::: " + assetPath + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))

getAssetsFromPath('/YugPreLoader/test', True)