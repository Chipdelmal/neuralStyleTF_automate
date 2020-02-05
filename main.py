#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import aux
import subprocess


# Setup simulation parameters and paths
(IMG_SIZE, iterations) = (2000, 7500)
(PATH_STY, PATH_OUT, PATH_IMG) = (
        '/Volumes/marshallShare/temp/nnTransfer/styles/',
        '/Volumes/marshallShare/temp/nnTransfer/out/',
        '/Volumes/marshallShare/temp/nnTransfer/yoshiSide.png'
    )

# Get styles paths
stylesPaths = aux.getFilesWithExt(PATH_STY)

# Automation part
imgsN = len(stylesPaths)
imgName = os.path.splitext(os.path.basename(PATH_IMG))[0]
for (i, imgSty) in enumerate(stylesPaths):
    # Create output folder
    styName = os.path.splitext(os.path.basename(imgSty))[0]
    outFolder = PATH_OUT + "" + imgName + "-" + "" + styName
    subprocess.Popen(['mkdir', outFolder])
    # Generate bash command
    cmd = [
        "python", "neural_style.py",
        "--content_img", PATH_IMG,
        "--style_imgs", imgSty,
        "--img_output_dir", outFolder,
        "--max_size", str(IMG_SIZE),
        "--max_iterations", str(iterations),
        "--device", "/cpu:0"
        # "--original_colors"
        # "--verbose"
    ]
    # Print state
    alert = "* [Running image {}/{} ({})]"
    print("*" * 150)
    print(alert.format(str(i + 1), str(imgsN), outFolder))
    print("*" * 150)
    # Run command and wait until it finishes
    p = subprocess.Popen(cmd)
    p.wait()
