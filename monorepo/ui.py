# API Variable?	Setting	Value	Comments
# 	Interface	img2img > Inpaint Upload	
# 	Clip Skip	1	ignore, not useful in XL
# 	SD Checkpoint	sd_xl_base_1.0_fp16_vae.safetensors	sd_xl_turbo_1.0_fp16.safetensors seems less creative
# 	SD VAE	Automatic	always leave it on Automatic, VAE is required and it needs to match
# 	Resize Mode	Just resize	
# 	Mask blur	4	
# 	Mask mode	Inpaint masked	
# 	Maked content	fill	
# 	Inpaint Area	Whole picture

# 	Sampling method	DMP++ 2M SDE Karras	
# 	Sampling steps	50	
# 	Refiner Checkpoint	sd_xl_base_1.0_fp16_vae.safetensors	will also test refiner
# 	Refiner Switch At	0.8	
# x	CFG Scale	10	recommended 2.5 to 3, but higher numbers yield more realistic scenes
# 	Denoising Strength	1	dropping below one yields less creative results
			
# 	ControlNet v1.1.440		
# 	Enable	Yes	
# 	Upload independent control image	Enabled	
# 	Mask Upload	?	looks like no
# 	Control Type	Canny	
# 	Preprocessor / Model	canny / controlnet-canny-sdxl-10	there are several canny models, have not tried them all
			
# 	Control Weight	1	
# 	Starting Control Step	0	
# 	Ending Control Step	1	
# x	Canny Low Threshold	10	Default is 100 in RunDiffusion, but doesn't pick up fine details well
# x	Canny High Threshold	50	Default is 200 in RunDiffusion, but doesn't pick up fine details well
# 	Control Mode	Balanced	
# 	Preprocessor Resolution	1024	
# 	Resize Mode	Just Resize	Crop and Resize works just as well, might not matter. Resize and fill is bad.

with gr.TabItem('Inpaint upload', id='inpaint_upload', elem_id="img2img_inpaint_upload_tab") as tab_inpaint_upload:
                                init_img_inpaint = gr.Image(label="Image for img2img", show_label=False, source="upload", interactive=True, type="pil", elem_id="img_inpaint_base")
                                init_mask_inpaint = gr.Image(label="Mask", source="upload", interactive=True, type="pil", image_mode="RGBA", elem_id="img_inpaint_mask")


elif category == "inpaint":
                        with FormGroup(elem_id="inpaint_controls", visible=False) as inpaint_controls:
                            with FormRow():
                                mask_blur = gr.Slider(label='Mask blur', minimum=0, maximum=64, step=1, value=4, elem_id="img2img_mask_blur")
                                mask_alpha = gr.Slider(label="Mask transparency", visible=False, elem_id="img2img_mask_alpha")

                            with FormRow():
                                inpainting_mask_invert = gr.Radio(label='Mask mode', choices=['Inpaint masked', 'Inpaint not masked'], value='Inpaint masked', type="index", elem_id="img2img_mask_mode")

                            with FormRow():
                                inpainting_fill = gr.Radio(label='Masked content', choices=['fill', 'original', 'latent noise', 'latent nothing'], value='original', type="index", elem_id="img2img_inpainting_fill")

                            with FormRow():
                                with gr.Column():
                                    inpaint_full_res = gr.Radio(label="Inpaint area", choices=["Whole picture", "Only masked"], type="index", value="Whole picture", elem_id="img2img_inpaint_full_res")

                                with gr.Column(scale=4):
                                    inpaint_full_res_padding = gr.Slider(label='Only masked padding, pixels', minimum=0, maximum=256, step=4, value=32, elem_id="img2img_inpaint_full_res_padding")

with FormRow():
                            resize_mode = gr.Radio(label="Resize mode", elem_id="resize_mode", choices=["Just resize", "Crop and resize", "Resize and fill", "Just resize (latent upscale)"], type="index", value="Just resize")


if category == "sampler":
                        steps, sampler_name = create_sampler_and_steps_selection(sd_samplers.visible_sampler_names(), "img2img")

with gr.Column(elem_id="img2img_column_size", scale=4):
                                                width = gr.Slider(minimum=64, maximum=2048, step=8, label="Width", value=512, elem_id="img2img_width")
                                                height = gr.Slider(minimum=64, maximum=2048, step=8, label="Height", value=512, elem_id="img2img_height")


# ControlNet
with gr.Row(elem_classes=["controlnet_weight_steps", "controlnet_row"]):
            self.weight = gr.Slider(
                label="Control Weight",
                value=self.default_unit.weight,
                minimum=0.0,
                maximum=2.0,
                step=0.05,
                elem_id=f"{elem_id_tabname}_{tabname}_controlnet_control_weight_slider",
                elem_classes="controlnet_control_weight_slider",
            )
            self.guidance_start = gr.Slider(
                label="Starting Control Step",
                value=self.default_unit.guidance_start,
                minimum=0.0,
                maximum=1.0,
                interactive=True,
                elem_id=f"{elem_id_tabname}_{tabname}_controlnet_start_control_step_slider",
                elem_classes="controlnet_start_control_step_slider",
            )
            self.guidance_end = gr.Slider(
                label="Ending Control Step",
                value=self.default_unit.guidance_end,
                minimum=0.0,
                maximum=1.0,
                interactive=True,
                elem_id=f"{elem_id_tabname}_{tabname}_controlnet_ending_control_step_slider",
                elem_classes="controlnet_ending_control_step_slider",
            )

        # advanced options
        with gr.Column(visible=False) as self.advanced:
            self.processor_res = gr.Slider(
                label="Preprocessor resolution",
                value=self.default_unit.processor_res,
                minimum=64,
                maximum=2048,
                visible=False,
                interactive=True,
                elem_id=f"{elem_id_tabname}_{tabname}_controlnet_preprocessor_resolution_slider",
            )
            self.threshold_a = gr.Slider(
                label="Threshold A",
                value=self.default_unit.threshold_a,
                minimum=64,
                maximum=1024,
                visible=False,
                interactive=True,
                elem_id=f"{elem_id_tabname}_{tabname}_controlnet_threshold_A_slider",
            )
            self.threshold_b = gr.Slider(
                label="Threshold B",
                value=self.default_unit.threshold_b,
                minimum=64,
                maximum=1024,
                visible=False,
                interactive=True,
                elem_id=f"{elem_id_tabname}_{tabname}_controlnet_threshold_B_slider",
            )

        self.control_mode = gr.Radio(
            choices=[e.value for e in external_code.ControlMode],
            value=self.default_unit.control_mode.value,
            label="Control Mode",
            elem_id=f"{elem_id_tabname}_{tabname}_controlnet_control_mode_radio",
            elem_classes="controlnet_control_mode_radio",
        )

        self.resize_mode = gr.Radio(
            choices=[e.value for e in external_code.ResizeMode],
            value=self.default_unit.resize_mode.value,
            label="Resize Mode",
            elem_id=f"{elem_id_tabname}_{tabname}_controlnet_resize_mode_radio",
            elem_classes="controlnet_resize_mode_radio",
            visible=not self.is_img2img,
        )
