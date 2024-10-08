# %%
from PIL import Image
import numpy as np

frames = []

with Image.open(
    "/Users/jacfger/qmk_firmware/keyboards/splitkb/kyria/keymaps/jacfger/guraw.gif"
) as im:
    while True:
        try:
            im.seek(im.tell() + 1)
            print(im.info["duration"])
        except EOFError:
            break
        frames.append(np.array(im))
# %%
import matplotlib.pyplot as plt

filtered_frames = []
for frame in frames :
    filtered_frames.append(Image.fromarray(((frame > 90) * 255).astype(np.uint8)))


# %%
filtered_frames[0].save("guraw_filtered.gif", save_all=True, append_images=filtered_frames[1:], loop=0, duration=100)