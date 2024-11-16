# AI Image Generator 🎨

A powerful image generation application powered by Stable Diffusion 2.1, featuring a user-friendly web interface built with Gradio.

## 🌟 Features

- Text-to-image generation using state-of-the-art Stable Diffusion 2.1
- Interactive web interface with Gradio
- Customizable image dimensions (256x256 to 1024x1024)
- GPU-accelerated image generation
- Real-time preview of generated images

## 🛠️ Prerequisites

- Python 3.x
- CUDA-compatible GPU
- PyTorch with CUDA support

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/imanoop7/Image-Genrator
cd Image-Genrator
```

2. Install the required packages:
```bash
pip install diffusers transformers accelerate torch bitsandbytes scipy safetensors xformers
```

## 🚀 Usage

1. Run the application:
```bash
python app.py
```

2. Open your web browser and navigate to the local URL provided by Gradio (typically http://127.0.0.1:7860)

3. Enter your prompt in the text box, adjust the image dimensions if desired, and click "Generate Image 🚀"

## 📓 Notebooks

The repository includes several Jupyter notebooks for different use cases:
- `image_generation_stable_diffusion.ipynb`: Local implementation of Stable Diffusion
- `image_generation_stable_diffusion_colab.ipynb`: Google Colab version optimized for cloud execution
- `saving-and-loading-model-local.ipynb`: Model management utilities

### 🌐 Using Google Colab (if you do not Have GPU in your systems)

If you don't have a GPU-enabled system, you can still use this image generator through Google Colab(Free tier GPU).:

1. Open the `image_generation_stable_diffusion_colab.ipynb` in Google Colab by clicking this button: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/imanoop7/Image-Genrator/blob/main/image_generation_stable_diffusion_colab.ipynb)

2. Benefits of using Colab:
   - Free GPU access (Tesla T4/P100)
   - No local installation required
   - Pre-configured environment
   - Run directly in your browser

3. Steps to use:
   - Click "Runtime" → "Change runtime type" → Select "GPU" as Hardware accelerator
   - Run all cells in sequence
   - Follow the prompts to generate images

Note: Google Colab's free tier has usage limits and may disconnect after extended periods. For consistent usage, consider the local installation with a GPU.

## 📄 License

This project is licensed under MIT, the terms included in the LICENSE file.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## ⭐ Show your support

Give a ⭐️ if this project helped you!
