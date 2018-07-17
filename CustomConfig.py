#encoding:utf-8
import sys
import os

def doConfigSetup(*args):
    print (r'args[0] is %s') %args[0]
    clientInfo = args[0]
    print ("config stratr")

    #获取maya版本号
    SWV=clientInfo.swVer()
    print (r'maya ver is %s') %SWV

    custom_app = r"B:\custom_config\1865943\MAYA_HOME"

    if SWV=='2017':
        #修改maya文档路径   原路径 C:/Users/dengtao/Documents/maya
        os.environ["MAYA_APP_DIR"] = custom_app
        print ("Set MAYA_APP_DIR => %s") %custom_app

        #启用 旧版的 render layer 模式
        os.environ['MAYA_ENABLE_LEGACY_RENDER_LAYERS'] = '1'
        print ('render layer is enable')