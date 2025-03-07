import json

f = open("daytime.json")

data = json.load(f)

for anno in data["annotations"]:
    with open(f"./data/labels/frame{anno['image_id']}.txt", "a") as txtFile:
        # class x_center y_center width height

        temp = -1
        if anno['category_id'] in [1, 2, 3, 4, 5, 8, 9, 11, 14, 21, 22]:
            temp = 1
        elif anno['category_id'] in [13, 20]:
            temp = 6
        elif anno['category_id'] in [26, 27]:
            temp = 7
        elif anno['category_id'] in [12, 15, 16, 17, 18, 19, 24, 25, 28, 29, 30]:
            temp = 5
        elif anno['category_id'] == 6:
            temp = 2
        elif anno['category_id'] == 7:
            temp = 3
        elif anno['category_id'] in [10, 23]:
            temp = 4
        txtFile.write(
            f"{temp} {int(anno['bbox'][0]) / 640} {int(anno['bbox'][1]) / 512} {int(anno['bbox'][2]) / 640} {int(anno['bbox'][3]) / 512}\n")

f.close()
