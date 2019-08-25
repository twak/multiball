'''
Randomly scramble streets, parcels, and rule parameters

You probably want to edit the output path and memory budget

Created on 24 Aug 2019

@author: twak
'''
from scripting import *

import random, math
import os

ce = CE()

print("starting...")

for i in range(0,50): 
    
    print("working on " + str(i) )
    
    objects = ce.getObjectsFrom(ce.scene, ce.isShape)
    ce.setAttribute( objects, '/ce/rule/autoDerive' , False )    
    ce.setRuleFile( objects, "non")

        
    for b in ce.getObjectsFrom(ce.scene, ce.isBlock):
        ce.setAttributeSource(b, "/ce/block/lotWidthMin", "USER")
        ce.setAttribute(b, "/ce/block/lotWidthMin",  random.gauss( 12, 5 ) )
        ce.setAttributeSource(b, "/ce/block/lotAreaMin", "USER")
        ce.setAttribute(b, "/ce/block/lotAreaMin",  random.gauss( 300, 100 ) )
        ce.setAttributeSource(b, "/ce/block/irregularity", "USER")
        ce.setAttribute(b, "/ce/block/irregularity",  math.fabs ( random.gauss( 0, 0.7 ) ) )
        ce.setAttributeSource(b, "/ce/block/seed", "USER")
        ce.setAttribute(b, "/ce/block/seed",  random.randint(0,100000) )
    
    
    for s in ce.getObjectsFrom(ce.scene, ce.isGraphSegment):
        ce.setAttributeSource(s, "/ce/street/streetWidth", "USER")
        ce.setAttribute(s, "/ce/street/streetWidth", random.gauss(5,2) )
        ce.setAttributeSource(s, "/ce/street/sidewalkWidthLeft", "USER")
        ce.setAttribute(s, "/ce/street/sidewalkWidthLeft", math.fabs ( random.gauss(1.5,1) ) )
        ce.setAttributeSource(s, "/ce/street/sidewalkWidthRight", "USER")
        ce.setAttribute(s, "/ce/street/sidewalkWidthRight", math.fabs ( random.gauss(1.5,1) ) )    

    objects = ce.getObjectsFrom(ce.scene, ce.isShape)
    ce.setAttributeSource(objects, "/ce/rule/randomSeed", "USER")
    ce.setRuleFile(objects, "muli.cga")
    for b in objects:
        ce.setAttribute(b, "/ce/rule/randomSeed",  random.randint(0,100000) )
    
    ce.setSelection(ce.getObjectsFrom(ce.scene()))
    
    settings = OBJExportModelSettings()
    path = "C:/Users/twak/Desktop/multiball/"+str(i)+"/"
    try:
        os.makedirs(path)
    except:
        pass
    settings.setOutputPath(path)
    settings.setBaseName("%d_multiball" % i)
    settings.setMemoryBudget(32000)
    ce.export(ce.getObjectsFrom(ce.scene()), settings)
