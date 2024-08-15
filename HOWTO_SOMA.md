# How-to run SAM-2 in soma (GPU nodes)

I recommend installing SAM-2 in a python `conda` environment of its own.   I am sharing my own conda environment inside this repository along with a Python wheel for SAM-2 that matches that environment. 

To create the environment I followed the installation steps in the the original GitHub repository :

```
git clone https://github.com/mpinb/segment-anything-2.git  mpinb-sam2
conda env create -n mpinb-sam2 -f mpinb-sam2/sam2-soma-env.yml
conda activate mpinb-sam2
python -m pip install mpinb-sam2/wheels/SAM_2-1.0-cp310-cp310-linux_x86_64.whl
```

# Running SAM-2 in soma

SAM-2  masks generation process is very GPU memory hungry.  I advise you to start with the base plus model and see if you are satisfied with the results before switching to the large model. 

There is also the `YOLO 8` model from ultralytics that has a lower memory footprint for inference.  You could consider using  `SAM-2` to train `YOLO 8`.