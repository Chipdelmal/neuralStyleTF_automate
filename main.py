#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import warnings
import inputDictionaries as inDict
warnings.filterwarnings("ignore")

(IMG_SIZE, SET) = (2000, 2)
PATH = "/Volumes/marshallShare/temp/nnTransfer/styles//"
PATH_OUT = PATH + "image_output/"

if SET == 1:
    imagesDict = inDict.imgEcuador
elif SET == 2:
    imagesDict = inDict.imgYoshi
elif SET == 3:
    imagesDict = inDict.imgGremlin
elif SET == 4:
    imagesDict = inDict.imgLogo

# Automation part
imgsN = len(imagesDict)
for (i, params) in enumerate(imagesDict):
    # Create output folder
    (imgN, styN) = (params["img"].split(".")[0], params["style"].split(".")[0])
    outFolder = PATH_OUT + "" + imgN + "-" + "" + styN
    subprocess.Popen(['mkdir', outFolder])
    # Generate bash command
    cmd = [
        "python", "neural_style.py",
        "--content_img", params["img"],
        "--style_imgs", params["style"],
        "--img_output_dir", outFolder,
        "--max_size", str(IMG_SIZE),
        "--max_iterations", params["iters"],
        "--device", "/cpu:0"#,
        # "--original_colors"
        # "--verbose"
    ]
    # Print state
    alert = "* [Running image {}/{} ({})]"
    print("-" * 100)
    print(alert.format(str(i + 1), str(imgsN), params["img"]))
    print("-" * 100)
    # Run command and wait until it finishes
    p = subprocess.Popen(cmd)
    p.wait()
