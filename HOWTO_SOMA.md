# How-to run SAM-2 in soma (GPU nodes)

I recommend installing SAM-2 in a python `conda` environment of its own.   I am sharing my own conda environment inside this repository along with a Python wheel for SAM-2 that matches that environment. 

To create the environment I followed the installation steps in the the original GitHub repository :

```
git clone https://github.com/mpinb/segment-anything-2.git  mpinb-sam2
CONDA_OVERRIDE_CUDA="12.2" conda env create -n mpinb-sam2 -f mpinb-sam2/sam2-soma-env.yml
conda activate mpinb-sam2
python -m pip install mpinb-sam2/wheels/SAM_2-1.0-cp310-cp310-linux_x86_64.whl
python -m ipykernel install --user --name mpinb-sam2 --display-name mpinb-sam2
```

# Running SAM-2 in soma

SAM-2  masks generation process is very GPU memory hungry.  I advise you to start with the base plus model and see if you are satisfied with the results before switching to the large model. 

It is also possible to use `YOLO 8` segmentation model from ultralytics that has a lower memory footprint for inference. You might consider using `SAM-2` to train `YOLO 8` and then switch models.

__NOTE:__ The [conda environment](sam2-soma-env.yml) has also the 'YOLO 8` ultralytics module installed for convenience.

To run the notebooks inside this repository using the soma `GPU` nodes (the nodes from the `GPU-interactive` partition are not recommended since they are constrained in memory.)

```
