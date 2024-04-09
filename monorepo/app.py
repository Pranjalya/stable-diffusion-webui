import os
import gradio as gr

# vars
clip_skip = 1
sd_checkpoint = "sd_xl_base_1.0_fp16_vae.safetensors" # https://huggingface.co/benjamin-paine/sd-xl-alternative-bases/resolve/main/sd_xl_base_1.0_fp16_vae.safetensors
sd_vae = "sd_xl_base_1.0_fp16_vae.safetensors" # Automatic
resize_mode = "Just resize"
inpainting_mask_invert = "Inpaint masked"
inpainting_fill = "fill"
inpaint_full_res = "Whole picture"
resize_mode = "Just resize" # "Crop and resize"
refiner_checkpoint = "sd_xl_base_1.0_fp16_vae.safetensors"
refiner_switch_at = 0.8
denoising_strength = 1

# Controlnet
self.enabled = True
self.type_filter = gr.Radio(["All", "Canny", "Depth"], label="Control Type", value="Canny")
self.upload_independent_img_in_img2img = True
self.module = "canny"
self.model = "controlnet-canny-sdxl-1.0"


with gr.Blocks() as demo:
    gr.Markdown("Automatic 1111 Stable Diffusion")
    init_img_inpaint = gr.Image(label="Image for img2img", show_label=False, source="upload", interactive=True, type="pil", elem_id="img_inpaint_base")
    init_mask_inpaint = gr.Image(label="Mask", source="upload", interactive=True, type="pil", image_mode="RGBA", elem_id="img_inpaint_mask")

    mask_blur = gr.Slider(label='Mask blur', minimum=0, maximum=64, step=1, value=4, elem_id="img2img_mask_blur")
    mask_alpha = gr.Slider(label="Mask transparency", visible=False, elem_id="img2img_mask_alpha")

    cfg_scale = gr.Slider(minimum=1.0, maximum=30.0, step=0.5, label='CFG Scale', value=7.0, elem_id="txt2img_cfg_scale")
