# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os,sys,re
import time


for i in pm.ls(type="aiOptions"):
    #报错停止渲染
    if i.hasAttr("abortOnError"):
        i.abortOnError.set(0)
    #日志级别
    if i.hasAttr("log_verbosity"):
        i.log_verbosity.set(1)

    if i.hasAttr("autotx"):
        i.autotx.set(False)

    if i.hasAttr("textureMaxMemoryMB"):
        i.textureMaxMemoryMB.set(l=0)
        i.textureMaxMemoryMB.set(20480)

    if i.hasAttr("threads_autodetect"):
        i.threads_autodetect.set(0)

    if i.hasAttr("threads"):
        i.threads.set(30)
        PRE_BASE.log_scene_set("threads","30")

#arnold的 bbox
for i in pm.ls(type="aiStandIn"):
    if i.hasAttr("deferStandinLoad"):
        print "aiStandIn node"
        print "%s.deferStandinLoad 1" % (i)
        i.deferStandinLoad.set(0)

for i in pm.ls(type="pgYetiMaya"):
    if i.hasAttr("aiLoadAtInit"):
        print "pgYetiMaya node"
        print "%s.aiLoadAtInit 1" % (i)
        i.aiLoadAtInit.set(1)
        
        
    
    




