import ldclient
from ldclient.config import Config
import os
import tkinter as tk
import requests
import datetime
import io
from PIL import Image, ImageTk


def get_dog_image():
    """Requests randomized dog images from endpoint

    Returns:
        str: Image direct URL
    """
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    if r.status_code == 200:
        return(r.json()['message'])
    else:
        print(f'Request {r.status_code}. {r.text}')


def display_image(url):
    """Reads image from direct URL

    Args:
        url (str): Image direct URL

    Returns:
        PIL.ImageTk.PhotoImage
    """
    size = 250, 250
    im = Image.open(requests.get(url, stream=True).raw)
    im.thumbnail(size, Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im)
    return image


def update():
    """Updates label_time and label_main with text or image depending on feature flag enablement
    """
    # LaunchDarkly feature flag name, user, default value
    show_feature = ld_client.variation('show-pup', {'key': 'hayman'}, False)
    label_time.config(text=f'{datetime.datetime.now().strftime("%A %b %d %Y")}\n{datetime.datetime.now().strftime("%H:%M:%S")}')
    if show_feature:
        url = get_dog_image()
        image = display_image(url)
        label_main.config(image=image)
        label_main.image = image
    else:
        label_main.config(image='', text='No more pups :(', fg='#22313F', bg='#ECF0F1', font=('Ariel', 12, 'italic'))
    app.after(60, update)


if __name__ == '__main__':
    launchdarkly_sdk_key = os.environ['ld_prod']
    ldclient.set_config(Config(launchdarkly_sdk_key))
    ld_client = ldclient.get()

    app = tk.Tk()
    HEIGHT = 600
    WIDTH = 600
    app.geometry(f'{HEIGHT}x{WIDTH}')
    app.resizable(width=0, height=0)

    # Constructing canvas
    canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH, bg='white')
    canvas.pack(expand=True)

    # Constructing upper frame and contents
    upper_frame = tk.Frame(app,  bg='#ECF0F1')
    upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    label_time = tk.Label(upper_frame, padx=10, pady=10, bg='#ECF0F1', fg='#22313F')
    label_time.pack(expand=True)

    # Constructing lower frame and contents
    lower_frame = tk.Frame(app, bg='#ECF0F1')
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label_main = tk.Label(lower_frame, anchor='center', padx=10, pady=10)
    label_main.pack(expand=True)

    update()

    app.mainloop()
