import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import gradio as gr

# Clear GPU cache
torch.cuda.empty_cache()

# Load the model
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

# Image generation function
def image_generator(prompt, width=512, height=512):
    """
    Generates an image from the given prompt using Stable Diffusion.
    
    Parameters:
        prompt (str): The text prompt to generate the image.
        width (int): The width of the output image.
        height (int): The height of the output image.
    
    Returns:
        PIL.Image: The generated image.
    """
    image = pipe(prompt, width=width, height=height).images[0]
    return image

# Define Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🚀 AI-Powered Art Generator
        Enter a prompt below to create stunning images with **Stable Diffusion**.
        Customize the dimensions and see your imagination come to life! 🎨
        """
    )

    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(
                label="Enter Your Prompt",
                placeholder="e.g., A serene mountain landscape at sunset",
                lines=2,
            )
            width_slider = gr.Slider(
                minimum=256, maximum=1024, value=512, step=64, label="Image Width"
            )
            height_slider = gr.Slider(
                minimum=256, maximum=1024, value=512, step=64, label="Image Height"
            )
            generate_button = gr.Button("Generate Image 🚀")

        with gr.Column():
            output_image = gr.Image(label="Generated Image")

    generate_button.click(
        fn=image_generator,
        inputs=[prompt_input, width_slider, height_slider],
        outputs=output_image,
    )

# Launch the app
demo.launch()
