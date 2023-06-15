# Final Report: AI Image Generation Project

## Introduction

Our AI Image Generation project aimed to develop a user-friendly website interface that utilizes artificial intelligence to generate images based on textual prompts provided by the user or randombly generated. The project involved integrating an AI image generator model with a web platform, creating a system that can receive and generate textual prompts and display generated images for the user.

## Goals

The key goals of the project were:

1. **AI Image Generation**: Develop an AI-based system that can generate images based on textual prompts.

2. **Website Interface**: Design and implement a user-friendly website interface with a task bar to input textual prompts. The interface should also have a “generate” button to trigger image generation and a “random prompt” button to generate a random prompt in the task bar.

3. **Public Accessibility through API**: Make the AI Image Generation tool accessible to the public via a web API.

4. **Response Time**: The system should generate images within approximately 20 seconds after the user clicks the "generate" button.

5. **Image Display and Download**: Once an image is generated, it should be displayed on the website and be available for download by the user.

## Achievements

1. **AI Image Generation**: We successfully integrated an AI image generation model using Python from Hugging Face. The model uses stable diffusion techniques to create high-quality images based on the textual prompts provided. We made this using a server at home that will be connected to in the website. 

2. **Website Interface**: The website interface was developed with an aesthetically pleasing design, incorporating HTML and CSS. The task bar for inputting textual prompts, the “generate” button, and the “random prompt” button were successfully implemented as per the project goals.

3. **Random Prompt Generation**: We used GPT-2, also from Hugging Face, to generate random textual prompts. The model was integrated using Python and connected to the image generator through JavaScript.

4. **Response Time**: Our system was able to generate images within the target time frame of approximately 20 seconds by utilizing the server's graphics card, instead of having in run on the CPU, which would have caused the generation time per image to skyrocket at around 30 minutes. 

5. **Image Display and Download**: The generated images are displayed on the website, and users can easily download them by right-clicking.

6. **Partial Achievement - Public Accessibility through API**: While the original goal was to make the website public through a web API, we were able to achieve this only partially. We used ngrok to create an API, but it's limited to only one image at once and without the ability to generate random prompts. 

## How it Works

1. When you want generate an image the prompt will be sent to a server where the image will be generated using Stable Diffusion on an NVIDIA RTX 2060. 
2. After it's done generating the image will be sent back to the user and displayed on the website. 
3. If the user decides to generate a random prompt, a seperate Python script will try to generate a prompt using an API of a different AI model called GPT-2. You are also able to view the prompt as it's being generated.
4. You can make any changes you like to generated prompts or generate a new one before you decide to submit it.
## Conclusion

The AI Image Generation project was a success in meeting most of its goals. The website, with its user-friendly interface, effectively utilizes AI models for generating high-quality images based on textual prompts. 