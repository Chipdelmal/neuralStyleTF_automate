import subprocess
import warnings
import inputDictionaries as inDict
warnings.filterwarnings("ignore")

IMG_SIZE = 4000
PATH = "/Users/sanchez.hmsc/Documents/GitHub/neuralStyleTF_automate/"
imagesDict = inDict.imgEcuador
PATH_OUT = PATH + "image_output/"

# Automation part
imgsN= len(imagesDict)
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
        "--device", "/cpu:0"
        # "--verbose",
        # "--original_colors"
    ]
    # Print state
    alert = "* [Running image {}/{} ({})]"
    print("-" * 100)
    print(alert.format(str(i + 1), str(imgsN), params["img"]))
    print("-" * 100)
    # Run command and wait until it finishes
    p = subprocess.Popen(cmd)
    p.wait()
