#!/usr/bin/env python
#encoding:utf-8
# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os,sys,re
import time


def main(*args):
    #关动力学
    mel.eval("putenv(\"MAYA_DISABLE_BATCH_RUNUP\",\"1\"); global proc dynRunupForBatchRender() {}; ")
    print ("Set MAYA_DISABLE_BATCH_RUNUP = 1 ")

    #设置当前帧 (对一些毛发没有跟随物体动的,而开场景却是动的)
    info_dict = args[0]
    start = info_dict["start"]
    print int(start)
    cmds.currentTime(int(start)-1,edit=True)
    print "update frame"