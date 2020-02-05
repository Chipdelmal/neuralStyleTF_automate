import glob

# Styles dictionary!
imgEcuador = [
    {"img": "ecuador00.jpg", "style": "g4.jpg", "iters": "30"},
    {"img": "ecuador01.jpeg", "style": "g1.jpg", "iters": "75"},
    {"img": "ecuador03.jpeg", "style": "g5.jpg", "iters": "75"},
    {"img": "ecuador04.jpeg", "style": "g3.jpg", "iters": "200"},
    {"img": "ecuador05.jpeg", "style": "flowers.png", "iters": "150"},
    {"img": "ecuador06.jpeg", "style": "g6.jpg", "iters": "500"}
]


iterations = 2000
imgGremlin= [
    {"img": "gremlin.jpg", "style": "t_2.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_3.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_5.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_6.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_8.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_9.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_10.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_11.jpg", "iters": str(iterations)},
    {"img": "gremlin.jpg", "style": "t_13.jpg", "iters": str(iterations)}
]

styYoshi = glob.glob("/Users/sanchez.hmsc/Documents/GitHub/neuralStyleTF_automate/styles/*.jpg")
styYoshi2 = glob.glob("/Users/sanchez.hmsc/Documents/GitHub/neuralStyleTF_automate/styles/*.png")
styYoshi.extend(styYoshi2)
styYoshi = [i.split('/')[-1] for i in styYoshi]
iterations = 7500
# styYoshi = [
#     "t_22.jpg", "t_2.jpg", "t_3.jpg", "t_8.jpg", "t_5.jpg", "t_6.jpg",
#     "t_10.jpg", "t_11.jpg", "t_13.jpg", "t_15.jpg", "t_16.jpg", "t_17.jpg",
#     "t_19.jpg", "t_21.jpg", "t_22.jpg", "t_24.jpg", "starry-night.jpg",
#     #"t04.jpg", "t03.jpg", "t35.jpg", "t_27.jpg", "t_21.jpg"
# ]
imgYoshi = [{
        "img": "yoshiSide.png",
        "iters": str(iterations),
        "style": i
    } for i in styYoshi
]


iterations = 2000
imgLogo = [
    {"img": "mgBio.png", "style":"circuit.jpg", "iters":str(iterations)},
    {"img": "mgBio.png", "style":"circuit2.jpg", "iters":str(iterations)},
    {"img": "mgd00.png", "style":"circuit.jpg", "iters":str(iterations)},
    {"img": "mgd00.png", "style":"circuit2.jpg", "iters":str(iterations)}
]
