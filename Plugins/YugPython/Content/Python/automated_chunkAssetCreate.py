import unreal
import requests
import json

# User Id who will own the assets
user_Id = "sL7rbMVkPncnXh2MtWIz7Z1OqZA2"

def createDataAsset(path, assetName, chunkId):
    # Get asset tools
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
 
    # Creates a Level Sequence - /Game/Test_LS
    primary_label = unreal.AssetTools.create_asset(asset_tools, asset_name = assetName, package_path = path, asset_class = unreal.PrimaryAssetLabel, factory = unreal.DataAssetFactory())

    custom_rule = primary_label.get_editor_property('rules')
    custom_rule.set_editor_property('chunk_id', chunkId)
    custom_rule.set_editor_property('apply_recursively', True)
    custom_rule.set_editor_property('cook_rule', unreal.PrimaryAssetCookRule.ALWAYS_COOK)

    primary_label.set_editor_property('rules', custom_rule)
    primary_label.set_editor_property('label_assets_in_my_directory', True)

def createEditorItemOnServer(chunkId, assetName, assetType, assetPath):
    placeableStaticMesh = ""
    placeableBlueprint = ""
    asset = ""

    if(assetType == "StaticMesh"):
        placeableStaticMesh = assetType + "'" + assetPath + "/" + assetName + "." + assetName + "'"
    elif(assetType == "Blueprint"):
        placeableBlueprint = "BlueprintGeneratedClass" + "'" + assetPath + "/" + assetName + "." + assetName + "_C'"
    else:
        asset = ""

    createItem_url = "https://xc3qhiayxd.execute-api.ap-south-1.amazonaws.com/production/me/chunks/items"

    createItem_payload = json.dumps({
    "ownerId": user_Id,
    "itemName": assetName,
    "itemPakChunkData": {
        "chunkId": chunkId,
        "dependentChunkIds": [],
        "yugPlaceableStaticMesh": placeableStaticMesh,
        "yugPlaceableBlueprintAsset": placeableBlueprint,
        "yugAsset": asset
    },
    "itemType": assetType,
    "shortDescription": "Automated item for " + assetName + " " + assetType,
    "itemDescription": "<p>Automated item for " + assetName + " " + assetType + "</p>",
    "publishStatus": "published",
    "visibility": "public",
    "tags": [
        "automated_chunkAsset"
    ],
    "itemCategory": "editorItem",
    "itemImageUrl": "https://storage.googleapis.com/yug-meta-external-files/k1ArdLeo9DM0dJhd1678535566782.png",
    "galleryImages": []
    })

    createItem_headers = {
    'Content-Type': 'application/json'
    }

    createItem_response = requests.request("POST", createItem_url, headers=createItem_headers, data=createItem_payload)
    print("Create Editor Item for ", assetName," Response:: ", createItem_response.status_code)
    print("Create Editor Item for ", assetName," :: ", createItem_response.text)


def makeAssetsFromPath(path, bRecursive):
    if(user_Id == ""):
        print("User ID required to proceed!! Stopping....")
        return 
    
    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    # unreal.EditorAssetLibrary.make_directory(path+'/myFolder')

    for asset in assets:
        assetPath = (unreal.StringLibrary.conv_name_to_string(asset.package_path) + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
        matDir = path + "/Material_and_Texture"
        skeleDir = path + "/SkeletalMesh_and_Skeleton"

        if unreal.EditorAssetLibrary.does_directory_exist(matDir) == False:
            unreal.EditorAssetLibrary.make_directory(matDir)

        if unreal.EditorAssetLibrary.does_directory_exist(matDir) == False:
            unreal.EditorAssetLibrary.make_directory(matDir)

        # print(asset.asset_name, " :: " ,asset.asset_class_path.asset_name)

        if (asset.asset_class_path.asset_name == "Material" or asset.asset_class_path.asset_name == "Texture2D"):
            unreal.EditorAssetLibrary.rename_asset(assetPath,matDir + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
        elif(asset.asset_class_path.asset_name == "SkeletalMesh" or asset.asset_class_path.asset_name == "Skeleton"):
            unreal.EditorAssetLibrary.rename_asset(assetPath,skeleDir + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
        elif(asset.asset_class_path.asset_name == "StaticMesh" or asset.asset_class_path.asset_name == "Blueprint"):
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

                if unreal.EditorAssetLibrary.does_directory_exist(assetPath) == False:
                    unreal.EditorAssetLibrary.make_directory(assetPath)
                    unreal.EditorAssetLibrary.rename_asset(assetPath, assetPath + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
                    createDataAsset(assetPath + "/", "Chunk_" + unreal.StringLibrary.conv_name_to_string(asset.asset_name), chunkDataJson["chunkId"])
                    createEditorItemOnServer(chunkDataJson["chunkId"], unreal.StringLibrary.conv_name_to_string(asset.asset_name), unreal.StringLibrary.conv_name_to_string(asset.asset_class_path.asset_name), unreal.StringLibrary.conv_name_to_string(asset.package_path))
                    # print(assetPath + " ::: " + assetPath + "/" + unreal.StringLibrary.conv_name_to_string(asset.asset_name))
            else:
                print("Create Chunk Failed :: ", chunkData.status_code)
                return

makeAssetsFromPath('/YugPreLoader/MyAssets', True)