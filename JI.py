# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:27:44 2020

@author: casualfriday
"""
import matplotlib.pyplot as plt
import imageio
def plotter(room,where="couch"):
    
    plan_paths={"game room": "escape-room-plan-gameroom",
               "bedroom 1": "escape-room-plan-bedroom1",
               "bedroom 2": "escape-room-plan-bedroom2",
               "living room": "escape-room-plan-livingroom",
               "outside": "escape-room-plan-outside"
               }
    plan_path=plan_paths[room]

    plan = imageio.imread('./images/'+plan_path+'.jpg')
    pedro = imageio.imread('./images/pedro2.png')

    pedro_dict={"couch": [0.2675, 0.715, 0.09, 0.09],
                "piano": [0.33, 0.432, 0.09, 0.09],
                "queen bed": [0.475, 0.28, 0.09, 0.09],
                "double bed": [0.44, 0.56, 0.09, 0.09],
                "dresser": [0.520, 0.615, 0.09, 0.09],
                }

    if room=="game room":
        pedro_dict["door a"]=[0.33, 0.27, 0.09, 0.09]
    elif room=="bedroom 1":
        pedro_dict["door a"]=[0.41, 0.27, 0.09, 0.09]
        pedro_dict["door b"]=[0.48, 0.40, 0.09, 0.09]
        pedro_dict["door c"]=[0.5507, 0.27, 0.09, 0.09]
    elif room=="bedroom 2":
        pedro_dict["door b"]=[0.48, 0.51, 0.09, 0.09]
    elif room=="living room":
        pedro_dict["door c"]=[0.622, 0.27, 0.09, 0.09]
        pedro_dict["door d"]=[0.685, 0.715, 0.09, 0.09]
    elif room=="outside":
        pedro_dict["door d"]=[0.685, 0.815, 0.09, 0.09]
    
    plt.figure(figsize=(16,10))
    plt.rcParams["axes.edgecolor"] = "green"
    plt.rcParams["axes.linewidth"] = 2
    plt.xticks([])
    plt.yticks([])
    plt.imshow(plan)
    
    plt.axes(pedro_dict[str(where)])
    plt.xticks([])
    plt.yticks([])
    plt.imshow(pedro)
    plt.show()