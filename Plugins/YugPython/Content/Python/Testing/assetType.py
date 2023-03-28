import unreal
import requests
import json

def createEditorItemOnServer(chunkId, assetName, assetType, assetPath):
    placeableStaticMesh = ""
    placeableBlueprint = ""
    asset = ""

    if(assetType == "StaticMesh"):
        placeableStaticMesh = assetType + "'" + assetPath + "/" + assetName + "." + assetName + "'"
        print(placeableStaticMesh)
    elif(assetType == "Blueprint"):
        placeableBlueprint = "BlueprintGeneratedClass" + "'" + assetPath + "/" + assetName + "." + assetName + "_C'"
        print(placeableBlueprint)
    else:
        asset = ""

def makeAssetsFromPath(path, bRecursive):
    # User Id who will own the assets
    user_Id = "sL7rbMVkPncnXh2MtWIz7Z1OqZA2"

    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    # unreal.EditorAssetLibrary.make_directory(path+'/myFolder')

    for asset in assets:
        assetPath = (unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
        matDir = path + "/Material_and_Texture"

        if unreal.EditorAssetLibrary.does_directory_exist(matDir) == False:
            unreal.EditorAssetLibrary.make_directory(matDir)

        # print(asset.asset_name, " :: " ,asset.asset_class_path.asset_name)
        chunkPayload = json.dumps(
            {
                "ownerId": user_Id,
                "itemName": unreal.StringLibrary.conv_name_to_string(asset.asset_name),
                "itemDescription": "Automated Chunk Data for " + unreal.StringLibrary.conv_name_to_string(asset.asset_name) + " " + unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name)
            }
        )
        chunkHeaders = {"Content-Type": "application/json"}

        chunkData = requests.request("POST", "https://xc3qhiayxd.execute-api.ap-south-1.amazonaws.com/production/me/chunks", headers=chunkHeaders, data=chunkPayload)

        if(chunkData.status_code >= 200 and chunkData.status_code < 300):
            chunkDataJson = chunkData.json()
            print(chunkDataJson)
            print("Data Chunk Id :: ", chunkDataJson["chunkId"])

            if (asset.asset_class_path.asset_name == "Material"or asset.asset_class_path.asset_name == "Texture2D"):
                unreal.EditorAssetLibrary.rename_asset(assetPath,matDir + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
            else:
                if unreal.EditorAssetLibrary.does_directory_exist(assetPath) == False:
                    unreal.EditorAssetLibrary.make_directory(assetPath)
                    unreal.EditorAssetLibrary.rename_asset(assetPath, assetPath + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
                    # createDataAsset(assetPath + "/", "Chunk_" + unreal.StringLibrary.conv_name_to_string(asset.asset_name), unreal.MathLibrary.random_integer_in_range(1000, 5000))
                    # print(assetPath + " ::: " + assetPath + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
        else:
            print("Create Chunk Failed :: ", chunkData.status_code)
            return
        
def checkAssetTypes(path, bRecursive):
    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    for asset in assets:
        assetPath = (unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
        # print(unreal.StringLibrary.conv_name_to_string(asset.asset_name) + " - " + unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name) + " :: " + unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name) + "'" + unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name) + "." + unreal.StringLibrary.conv_name_to_string(asset.asset_name) + "'")
        createEditorItemOnServer(2215, unreal.StringLibrary.conv_name_to_string(asset.asset_name), unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name), unreal.StringLibrary.conv_name_to_string(asset.package_path))

# makeAssetsFromPath("/YugPreLoader/MyAssets", True)
checkAssetTypes("/YugPreLoader/MyAssets", True)
