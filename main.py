#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import aux
import sys
import subprocess


(PATH_IMG, PATH_STY, PATH_OUT) = (sys.argv[1], sys.argv[2], sys.argv[3])
(IMG_SIZE, ITERATIONS) = (sys.argv[4], sys.argv[5])

# Get styles paths and image base name
stylesPaths = aux.getFilesWithExt(PATH_STY)
(imgsN, imgName) = (
        len(stylesPaths),
        os.path.splitext(os.path.basename(PATH_IMG))[0]
    )

# Automation part
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
            "--max_iterations", str(ITERATIONS),
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
