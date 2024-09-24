from modules.shared import opts
from modules.processing import Processed, process_images
import modules.scripts as scripts
import gradio as gr

class Script(scripts.Script):
    def title(self):
        return "Test Prompts"

    def ui(self, is_img2img):

        pose1 = gr.Checkbox(label="Fruits on a table", value=True)
        pose2 = gr.Checkbox(label="Majestic landscape", value=False)
        pose3 = gr.Checkbox(label="Modern cityscape at night", value=False)
        pose4 = gr.Checkbox(label="Evil Dragon", value=False)
        pose5 = gr.Checkbox(label="Posing woman", value=False)
        pose6 = gr.Checkbox(label="Posing man", value=True)
        pose7 = gr.Checkbox(label="Random Location", value=False)

        prompt_group = [pose1, pose2, pose3, pose4, pose5, pose6, pose7]
	
        with gr.Box():
		      
            options_header = gr.Markdown("<br>Options")
            nsfw = gr.Checkbox(label="NSFW content", value=False)
            sfw = gr.Checkbox(label="SFW content", value=True)
            
        return prompt_group + [nsfw, sfw]

    def run(self, p, pose1, pose2, pose3, pose4, pose5, pose6, pose7, nsfw, sfw):

        prompts = []
        negative_prompts = []
        
        if pose1:
            prompts.append("photo of fruits on top of a table")
            negative_prompts.append("(drawing, painting, deformed, mutated, drawing, anime, ugly, worse photo, worse proportions)")

        if pose2:
            prompts.append("majestic landscape with mountains, rivers, and a sunset")
            negative_prompts.append("(overexposed, underexposed, low resolution, unnatural colors, digital art, painting, drawing)")

        if pose3:
            prompts.append("modern cityscape at night with bright lights and tall buildings")
            negative_prompts.append("(blurry, overexposed, underexposed, low resolution, painting, drawing, anime, empty streets)")

        if pose4:
            prompts.append("a dangerous looking evil dragon is in a close distance in front of a natural cataclysm")
            negative_prompts.append("(low resolution, blurry, overexposed, underexposed, cartoonish, rendering, 3dcg, uncanny valley, manga, comic, painting, wrong looking bodyparts, deformed, stupid)")

        if pose5:
            prompts.append("full-body photo of a posing beautiful woman in a photoshooting")
            negative_prompts.append("(cat, horns, deformations, mutations, painting, any worse face, worse human, anime, invisible head, invisible body)")

        if pose6:
            prompts.append("full-body photo with a posing male man in a photoshooting")
            negative_prompts.append("(worse bodyshape, deformations, mutations, painting, cartoon, any worse human-body, anime, invisible head, invisible body)")
            
        if pose7:
            prompts.append("at a {outdoor hotel enviroment|castle tower roof|wintergarden with lots of windows|wildlife nationalpark|acient egyptian temple near a pyramide|random interesting location}")
            negative_prompts.append("human mutations, human deformations, bad combination of told prompts, worse proportions")
            
        if nsfw:
            prompts.append("naughty, nudity, NSFW")
            negative_prompts.append("bad faces, fat, lowres, poorly drawn, worse, blurry, sfw")

        if sfw:
            prompts.append("sfw")
            negative_prompts.append("porn, erotic, lowres, poorly drawn, nudity, nsfw, nudity")
            
        p.prompt = ", ".join(prompts)
        p.negative_prompt = ", ".join(negative_prompts)

        proc = process_images(p)
        return Processed(p, proc.images, p.seed, all_prompts=proc.all_prompts, infotexts=proc.infotexts)
