#!/usr/bin/env python
#encoding:utf-8
# -*- coding: utf-8 -*-
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os,sys,re
import time
import maya.OpenMaya as om

#切换渲染层
mel.eval("fixRenderLayerOutAdjustmentErrors")


#删除多余的渲染层
render_layer= cmds.listConnections("renderLayerManager.renderLayerId")
all_layer = cmds.ls(type ='renderLayer')

#print render_layer
#print all_layer

for layer in all_layer:
    if layer in render_layer:
        print layer
    else:
        cmds.delete(layer)

#修复默认渲染层
def edo_renameDefualtRenderLayerName(newname='defaultRenderLayer'):
    drl=cmds.listConnections('renderLayerManager.rlmi[0]',s=0,d=1)[0]
    if not drl=='defaultRenderLayer':
        try:
            cmds.delete('defaultRenderLayer')
        except:
            print 'defaultRenderLayer is not found!'
    cmds.select(drl,r=1)
    msl=om.MSelectionList()
    mg=om.MGlobal()
    mg.getActiveSelectionList(msl)
    msl.length()
    mobj=om.MObject()
    msl.getDependNode(0,mobj)
    mfndn=om.MFnDependencyNode(mobj)
    mfndn.setName(newname)