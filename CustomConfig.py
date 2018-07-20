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

    #maya 颜色空间管理
    os.environ['MAYA_COLOR_MANAGEMENT_POLICY_LOCK'] = '1'
    os.environ['MAYA_RENDER_SETUP_INCLUDE_ALL_LIGHTS'] = '0'
    os.environ['MAYA_RENDER_SETUP_USE_UNTITLED_COLLECTIONS'] = '0'
    #os.environ['OCIO'] = r'D:\work\OpenColorIO-Configs-master\aces_1.0.3\config.ocio'
    os.environ['OCIO_ACTIVE_DISPLAYS'] = 'ACES'
    os.environ['OCIO_ACTIVE_VIEWS'] = 'Rec.709:Raw'

    #maya2018经常会渲染崩溃, 设置Viewport 2.0 中渲染时始终使用 DirectX 11  会减少崩溃现象
    os.environ['MAYA_OPENCL_IGNORE_DRIVER_VERSION'] = '1'
    os.environ['MAYA_VP2_DEVICE_OVERRIDE'] = 'VirtualDeviceDx11'

    #关闭当前maya 重启一个新的maya 等待60秒
    os.system(r'wmic process where name="maya.exe" delete')
    print "kill maya.exe process"
    manager_exe = "C:/Program Files/Autodesk/Maya2018/bin/maya.exe"
    os.system('start "" "%s"' % manager_exe)
    print "run C:/Program Files/Autodesk/Maya2018/bin/maya.exe"
    time.sleep(60)
    print "waiting for 60 seconds"

    #结束rlm进程
    os.system(r'wmic process where name="rlm.exe" delete')

    #拷贝文件夹
    srcDir1=r"B:/AMPED"  
    dstDir1=r"C:/AMPED"
    os.system ("robocopy /s  %s %s" % (srcDir1, dstDir1))
    #启动指定进程
    os.system(r'start C:/AMPED/rlm.exe')



def set_env(env,val):
    """添加环境变量的函数"""
    env_val = os.environ.get(env)
    os.environ[env] = (env_val  + r";"  if env_val else "") + val
    print "the env %s is %s" % (env, os.environ[env])
    return os.environ[env]