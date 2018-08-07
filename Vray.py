#!/usr/bin/env python
#encoding:utf-8
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
    #设置线程
    for i in pm.ls(type="VRaySettingsNode"):
        if i.hasAttr("sys_max_threads"):
            i.sys_max_threads.set(30)
            PRE_BASE.log_scene_set("sys_max_threads","30")
            
    #设置最大内存使用
    for i in pm.ls(type="VRaySettingsNode"):
        if i.hasAttr("srdml"):
            org_srdml = i.srdml.get()
            print "Your scens originalvray srdml is %s " % (org_srdml)
            if "vrayformaya" in info_dict["plugins"]:
                print type(info_dict["plugins"]["vrayformaya"])
                if info_dict["plugins"]["vrayformaya"] >= "3.10":
                    print "Your task vray version >= 3.10,set srdml to 0 "
                    i.srdml.set(0)
                else:
                    i.srdml.set(20480)
                    print "Your vray version lower than  3.10.01,set srdml to 20480MB"