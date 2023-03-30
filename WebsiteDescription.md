# Stimage

## Our Goal
We want to create a small website where you are able to type in a prompt and get an AI-generated image of that prompt. We want to add examples and add the option to generate a random prompt. 

## Static part
AI image generation is a process where a computer program, or artificial intelligence (AI), creates new images by learning from a collection of existing images. Here's a simple breakdown of how it works:

### Training
The AI is fed with a large dataset of images. These images help the AI understand various patterns, shapes, colors, and textures that make up different objects and scenes.

### Learning
The AI uses a special type of algorithm called a neural network to learn from these images. This network mimics the way our brain processes information. It adjusts and refines its understanding of the images as it goes through the training dataset multiple times.

### Generating
Once the AI is trained, it can create new images based on what it has learned. It starts with random input and gradually refines the image, using its knowledge of patterns and features from the training dataset. The output is a new, unique image that resembles the images it has seen before but is not an exact copy of any of them.

A popular AI technique used for image generation is called GAN, or Generative Adversarial Network. It involves two neural networks, the generator and the discriminator, working together. The generator creates the images, and the discriminator tries to determine if the images are real or generated. This helps the AI improve its image generation capabilities over time, making the generated images more realistic and detailed.

## Dynamic Part
We're trying to build our own image generator with the pre made stable diffusion AI from hugging face. We are using pytorch to build and train the modell. In the end you should be able to write a text.
### Front-end
The front-end includes an input field for the user to enter text and a "Submit" button. When the button is clicked, the input text is sent to the back-end server. Next to the input field there's a dice button to generate a random prompt, and a button to show a few examples. The image will get displayed under the prompt.
### Back-end
The back-end server is a Flask app that loads the Stable Diffusion model from a CKPT file. When it receives the input text from the front-end, it generates an image using the model. The image is then converted to base64 format and sent back to the front-end. The dice button will try to make an english sentence out of random nouns and verbs, and the example option will just give you the ability to get a prompt out of a pre-defined array. 

## Milestones
We're trying to release the first prototye until the start of June, and we're going to expand on it until the end of the school year.

## Project Members
We are a team of two working together to create this website, and we're trying our best to split our work equally. Our project clients are Mr. Klewein and Mr. Schramml. 
