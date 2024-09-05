"Test Prompts" Script for Stable Diffusion A1111/Forge WebUI

The Script let you select simple predefined prompts for Stable Diffusion A1111/Forge without a modifcation of the existing prompt / negative prompt fields.

You can use a dynamic (-1) or a fixed Seed to use it. It also works in a text2img batch. The selections are combinable. By default it is set to be (mostly) SFW but you can change that.
*mostly because it depends on your choosen model how it react because it can just generate content only by predefined selected prompts without the usage of something like ex. nudenet as a filter. (You also can modify the script to make your own "predefined" Prompts if you dislike the current examples).

Just put the Script into your Scripts Folder of your A1111 WebUI (or Forge WebUI) and restart the UI, select it in the "Scripts" Section of the User Interface to play around with.

The idea was to find a test solution using "predefined" prompts just while you edit your regular prompt / negative prompt to find out how your cfg/dimensions/aspectratio/model would react to different prompts of the one you just create without a modification of your prompt / negativ prompt fields.

Install: To install the script for your Stable Diffusion Forge/Automatic1111 WebUI just select "Install from URL" in your Extensions Tab. Restart the WebUI and select the Script at Scripts Section of the Txt2Img or Img2Img Tab.

To disable the script and go back to the editing of your regular prompt just unselect the script.

Interface:

![script_preview](https://github.com/user-attachments/assets/b3b1f623-7137-4b7f-b1fe-3abfc2b22850)

Example:

![test_generation](https://github.com/user-attachments/assets/992d6a04-abc4-4141-a773-c711569d27d7)

Parameters by the script for this example was: photo of fruits on top of a table, full-body photo with a posing male man in a photoshooting, sfw Negative prompt: (drawing, painting, deformed, mutated, drawing, anime, ugly, worse photo, worse proportions), (worse bodyshape, deformations, mutations, painting, cartoon, any worse human-body, anime, invisible head, invisible body), porn, erotic, nudity, nsfw, naked Steps: 32, Sampler: Heun, Schedule type: Automatic, CFG scale: 7, Seed: 1030965220, Face restoration: CodeFormer, Size: 640x640, Model hash: e8d5d0b55b, Model: NCHS-3, Clip skip: 3, Version: f2.0.1v1.10.1-previous-223-g86ee2d94

Source: https://github.com/zeittresor/sd-test-prompts
