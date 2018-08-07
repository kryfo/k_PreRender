#!/usr/bin/env python
#encoding:utf-8
# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os,sys,re
import time


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

    
    #关动力学
    mel.eval("putenv(\"MAYA_DISABLE_BATCH_RUNUP\",\"1\"); global proc dynRunupForBatchRender() {}; ")
    print ("Set MAYA_DISABLE_BATCH_RUNUP = 1 ")

    #设置当前帧 (对一些毛发没有跟随物体动的,而开场景却是动的)
    info_dict = args[0]
    
    # print (info_dict["user_id"]) #int
    # print (info_dict["start"])   #int
    # print (info_dict["mapping"]) #dict
    # print (info_dict["task_id"])  #int
    # print (info_dict["plugins"])  #dict
    # print (info_dict["rendersetting"]) #dict


    start = info_dict["start"]
    print int(start)
    cmds.currentTime(int(start)-1,edit=True)
    print "update frame"

    #切换渲染层
    mel.eval("fixRenderLayerOutAdjustmentErrors")
    #testgit