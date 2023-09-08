# Batch Image Background Remover

With this simple script you can remove the background of all images in the ```target``` folder.

This script was created to exercise my docker skills and to use it in the [digi-api.com](https://digi-api.com) to assist with the cleanup process of the images.

This project uses [REMBG](https://github.com/danielgatis/rembg) check it out.
## Usage

There's 3 ways you can use it right out of the box, for all three you will need to put the images that need the background to be removed in the ```target``` folder.

Also you will need [Docker](https://www.docker.com/) installed for first two options.

#### Docker run

First build your docker image, inside the repository folder run the following command:
```bash
docker build -t batch-background-remover .
```

Now just run the following command to start the background removal process:
```bash
docker run --mount type=bind,src=./,dst=/app batch-background-remover /target /dest png
```
This command do a few things:
It create's an unnamed volume in the directory pointing to the ```/app``` directory.

Then set the desired image to use, in this case we will use the image created in the previous step ```batch-background-remover```.

***Finally it will take three arguments:***
- First argument is the ```target``` folder, where the images reside.
- Second is the ```dest``` folder where the images with no background will be saved.
- The last one is the image file extension that we will get from the ```target``` folder - we will only get the images that have the desired extension, in this case ```png```.
***By default it will take all the ```png``` images but you can change it to whanever you want.***

When the command finishes the processing we will have the images with no background in our ```dest``` folder.

### Docker compose

Just run the following command in the repository folder:
```bash
docker compose up
```

If you need to customize the arguments, just change the ```compose.yml``` file, there's three environment variables that work the same as the arguments in the previous option.

### Python

For this step you will need [Python](https://www.python.org/downloads/release/python-380/) installed, the recommended version for rembg is 3.8.

With python installed, run the following command in the repository folder;
```bash
python3 app.py /target /dest png
```

The arguments follows the same rule as the previous exemples.