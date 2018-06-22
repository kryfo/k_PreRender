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
    PRE_BASE = CLASS_PRE_BASE()
    #设置线程
    for i in pm.ls(type="VRaySettingsNode"):
        if i.hasAttr("sys_max_threads"):
            i.sys_max_threads.set(30)
            PRE_BASE.log_scene_set("sys_max_threads","30")
