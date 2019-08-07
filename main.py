import subprocess
import warnings
warnings.filterwarnings("ignore")

PATH = "/Users/sanchez.hmsc/Documents/GitHub/neuralStyleTF_automate/"
PATH_OUT = PATH + "image_output/"
IMG_SIZE = 1000

# Styles dictionary!
imagesDict = [
    {"img": "quito.jpg", "style": "g4.jpg", "iters": "500"},
    {"img": "ecuador01.jpeg", "style": "g1.jpg", "iters": "500"},
    {"img": "ecuador03.jpeg", "style": "g5.jpg", "iters": "500"},
    {"img": "ecuador04.jpeg", "style": "g3.jpg", "iters": "500"},
    {"img": "ecuador05.jpeg", "style": "flowers.png", "iters": "500"},
    {"img": "ecuador06.jpeg", "style": "g6.jpg", "iters": "500"}
]

# Automation part
imgsN= len(imagesDict)
for (i, params) in enumerate(imagesDict):
    # Create output folder
    (imgN, styN) = (params["img"].split(".")[0], params["style"].split(".")[0])
    outFolder = PATH_OUT + imgN + "_" + styN
    subprocess.Popen(['mkdir', outFolder])
    # Generate bash command
    cmd = [
        "python", "neural_style.py",
        "--content_img", params["img"],
        "--style_imgs", params["style"],
        "--img_output_dir", outFolder,
        "--max_size", str(IMG_SIZE),
        "--max_iterations", params["iters"],
        "--device", "/cpu:0",
        "--verbose",
        "--original_colors"
    ]
    # Print state
    alert = "* [Running image {}/{} ({})]"
    print("-" * 100)
    print(alert.format(str(i + 1), str(imgsN), params["img"]))
    print("-" * 100)
    # Run command and wait until it finishes
    p = subprocess.Popen(cmd)
    p.wait()
