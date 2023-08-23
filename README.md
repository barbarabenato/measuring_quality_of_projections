# "Measuring the quality of projections of high-dimensional labeled data"

A Python implementation of the proposed metric for measuring the quality of labeled data projections [1]. We proposed a pseudo-labeling mechanism to assess visual separation using the performance of a semi-supervised optimum-path forest classifier (OPFSemi), measured by Cohen’s Kappa. Lower label propagation errors by OPFSemi in projections are related to higher data/visual separation. OPFSemi explores local and global information of data distribution when computing optimum connectivity between samples in a projection for label propagation. It is parameter-free, fast to compute, easy to implement, and generically handles any high-dimensional quantitative labeled dataset and projection technique. 

Data for 18 datasets and 39 projection techniques evaluated in [1] are also provided. 

[1] Benato, B. C., Falcão, A. X., Telea, A. C. "Measuring the quality of labeled data projections". SIBGRAPI 2023. ([pdf](https://www.sciencedirect.com/science/article/abs/pii/S0097849323001929))

## Installing

OPFSemi implementation is used from a precompiled file of PyIFT (see details [here](https://github.com/JoOkuma/PyIFT). A binary file is given in labeled_projection_quality/dist directory. We tested on Ubuntu 18.04 and Python 3.8. For installation purposes, a Dockerfile is provided. You can follow below OPFSemi installation via Dockerfile.

### Dockerfile 

First, we need to download the Dockerfile provided in this project.
```
curl -H 'Authorization: token ACCESS_TOKEN ' -H 'Accept: application/vnd.github.v3.raw' -O -L https://raw.github.com/barbarabenato/measuring_quality_of_projections/main/Dockerfile
```

Then, we build the image from the Dockerfile in the same folder we downloaded the Dockerfile and run the container. 

```
docker build -t projquality_img . && docker run -it projquality_img 
```

You can check the PyIFT installation by:
```
python
>>> import pyift.pyift as ift
>>>
```


### Assessing projection quality through OPFSemi
After running a container with PyIFT installed and labeled_projection_quality downloaded, we install our package by changing to the main directory and installing its dependencies:
```
cd assess_proj_quality/ && python -m pip install .
```

You can check the installation by:
```
python
>>> import assess_proj_quality
>>>
```

## Running
A running example is provided below. 
```
usage evaluate_by_opf.py <X_2d_data> <y_2d_data> <perc of sup samples>
```

You can run it by changing to deepfa directory and executing, for example:
```
python evaluate_by_opf.py ../data/proj_X_fashion_mnist_UMAP.csv ../data/proj_y_fashion_mnist_UMAP.csv 0.5 
```

## Citation
If you use the provided code, please cite the following article:
```
@article{BENATO:2023,
title = {Measuring the quality of projections of high-dimensional labeled data},
journal = {Computers & Graphics},
year = {2023},
issn = {0097-8493},
doi = {https://doi.org/10.1016/j.cag.2023.08.023},
url = {https://www.sciencedirect.com/science/article/pii/S0097849323001929},
author = {Bárbara C. Benato and Alexandre X. Falcão and Alexandru C. Telea},
keywords = {Quality of projections, Labeled data, Pseudo labeling},
}
```

