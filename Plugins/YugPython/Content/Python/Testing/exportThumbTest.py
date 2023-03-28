import unreal
import requests

def getAssetsFromPath(path, bRecursive):
    asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_reg.get_assets_by_path(path, bRecursive)
    print(len(assets))

    dirPath = unreal.Paths.project_dir() + "Thumbnails/"
    
    print(dirPath)

    x = requests.get("https://xc3qhiayxd.execute-api.ap-south-1.amazonaws.com/production/editor/scene/v5?prefabId=G8S7coutUORdDg7m&platform=Windows")

    print(x.text)

    # for asset in assets:
    #     unreal.DTThumbnailBPLib.py_render_thumbnail(asset.get_asset(), 512)

    # exportThumbnail(assets, dirPath, False)
    # exportThumbnail(assets, dirPath, True)

def exportThumbnail(assets, dirPath, bShowNotification):
    print("Called Export Thumbnail")
    for asset in assets:
        unreal.DTThumbnailBPLib.py_export_object_thumbnail(asset.get_asset(), 512, dirPath, bShowNotification)

getAssetsFromPath('/YugPreLoader/MyAssets', True)