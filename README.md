# App: Pup Slideshow with Feature Flag
![GIF Demo](https://haypublic.s3.amazonaws.com/ld.gif)
- [App: Pup Slideshow with Feature Flag](#app-pup-slideshow-with-feature-flag)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Running the Application](#running-the-application)
  - [Application Outline](#application-outline)
___
## Getting Started
### Prerequisites
To run `pup.py`, your Python version should be ≥ 3.6, and the following Python packages should be installed:
- requests>=2.25.1
- pillow>=8.1.2
- launchdarkly-server-sdk>=7.0.2

Authorization from LaunchDarkly is also required to toggle the feature flag. [Register for free now](https://app.launchdarkly.com/signup).
### Running the Application
To run `pup.py`, in Terminal/Command Line, run `python3 pup.py` (replace `python3` with your alias for Python ≥3.6).

___

## Application Outline

This application includes three functions:
- `get_dog_image()`
  - Sends a GET request to `https://dog.ceo/api/breeds/image/random`, which responds with a random image of a dog.
- `display_image()`
  - Accesses an image via its direct URL, and opens it as a Pillow Image object to display in application.
- `update()`
  - Updates the two labels with the current time and image pulled from API via `get_dog_image()`. `show_feature`, which is controlled by LaunchDarkly's feature flag determines whether an image is display or just text.
  - To disable the display of images and making requests to `https://dog.ceo/api/breeds/image/random` endpoint, we can make use of the feature flag `show-pup` on LaunchDarkly UI to enable/disable the feature.
  - The recursive `after()` at the end of the function runs the function again after 60 milliseconds.

From Lines 57 to 59, we are creating an instance of LaunchDarkly's Python SDK, and supplying it with the SDK key -- retrievable from [Account Settings](https://app.launchdarkly.com/settings/projects).

Lines 61 to 65 creates an instance of the tkinter class, and setting the height and width parameters of the application window. Lines 68 and 69 creates the white background as `canvas`, with the same dimensions of the application.

Lines 72 to 76 creates the upper frame that houses the current time, as updated by `update()`.

Lines 79 to 82 creates the lower frame that includes the image returned from `get_dog_image()` and `update()`.



