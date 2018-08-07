# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os,sys,re
import time

from PreRender import PreRenderBase as CLASS_PRE_BASE


def main(*args):
    print ("custome prerender  start ----------- ")
    info_dict = args[0]
    print (info_dict) #prerender  info   dict
    print (info_dict["user_id"]) #int
    print (info_dict["start"])   #int
    print (info_dict["mapping"]) #dict
    print (info_dict["task_id"])  #int
    print (info_dict["plugins"])  #dict
    print (info_dict["rendersetting"]) #dict

    PRE_BASE = CLASS_PRE_BASE()

    #设置初始帧
    info_dict = args[0]
    start_frame = info_dict["start"]

    if start:
        cmds.currentTime(int(start), edit=True)
        print "update frame"

    for i in pm.ls(type="aiOptions"):
        #报错停止渲染
        if i.hasAttr("abortOnError"):
            i.abortOnError.set(0)
            print ('abortOnError is %s') %i.abortOnError.get()
        #日志级别
        if i.hasAttr("log_verbosity"):
            i.log_verbosity.set(1)
            print ('log_verbosity is %s') %i.log_verbosity.get()

        if i.hasAttr("autotx"):
            i.autotx.set(False)

        if i.hasAttr("textureMaxMemoryMB"):
            i.textureMaxMemoryMB.set(l=0)
            i.textureMaxMemoryMB.set(20480)
        #关闭自动获取最大线程数
        if i.hasAttr("threads_autodetect"):
            i.threads_autodetect.set(0)
        #设置线程数
        if i.hasAttr("threads"):
            i.threads.set(30)
            PRE_BASE.log_scene_set("threads","30")

    #arnold的 bbox 避免边框扫描不正确
    for i in pm.ls(type="aiStandIn"):
        if i.hasAttr("deferStandinLoad"):
            print "aiStandIn node"
            print "%s.deferStandinLoad 1" % (i)
            i.deferStandinLoad.set(0)

    #arnold初始化, 解决部分yeti出不来临时缓存问题
    for i in pm.ls(type="pgYetiMaya"):
        if i.hasAttr("aiLoadAtInit"):
            print "pgYetiMaya node"
            print "%s.aiLoadAtInit 1" % (i)
            i.aiLoadAtInit.set(1)
        
        
    
    




