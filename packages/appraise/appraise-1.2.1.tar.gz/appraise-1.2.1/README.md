# APPRAISE

***A***utomated ***P***air-wise ***P***eptide-***R***eceptor binding model ***A***nalys***I***s for ***S***creening ***E***ngineered proteins (***APPRAISE***) is a method that predicts the receptor binding propensity of engineered proteins based on high-precision protein structure prediction tools, such as AlphaFold2-multimer. This Python package includes tools for preparing input files and analyzing the modeled structures.

Author: Xiaozhe Ding (Email: dingxiaozhe@gmail.com, xding@caltech.edu; Twitter: [@DingXiaozhe](https://twitter.com/dingxiaozhe?lang=en))

## Getting started without installation

We recommend using APPRAISE remotely by running Colab_APPRAISE.ipynb notebook on Google Colaboratory. This allows you to perform APPRAISE step by step using a graphical interface, and the results will be stored in Google Drive. No local installation is needed when using this notebook.

The basic service of Google Colaboratory is free, although you can pay to get stable access to better hardwares.

**How to run Colab_APPRAISE notebook**
1. Go to [Google Colaboratory](https://colab.research.google.com/), and you will be prompted to open a notebook; If the splash page did not appear, Click "File --> Open notebook";
2. Click the "Github" tab, paste the link https://github.com/GradinaruLab/APPRAISE/blob/main/Colab_APPRAISE.ipynb, and click the search icon;
3. Go to "File --> save a Copy in Drive", and you can start playing with the notebook!

## Local installation

### Environment

Local APPRAISE 1.2 was tested with the following environment:

 - MacOS 10.14.6

 - Python 3.6.10

 - Alphafold-colabfold 2.1.14 (Available [here](https://github.com/sokrypton/ColabFold))

 - PyMOL 2.3.3 (Schrodinger LLC.)

 - Python packages:

    - scipy 1.4.1

    - numpy 1.18.2

    - pandas 1.1.5

    - matplotlib 3.2.1

    - seaborn 0.11.2


### Installation options

Installation of APPRAISE locally requires pip. In most cases, pip comes with your Python environment. If not, you can [follow the instructions here to install pip](https://pip.pypa.io/en/stable/installation/).

#### Option 1 (recommended)
Install the distribution from PyPI. In the terminal, run:

```
pip install appraise
```

#### Option 2 (back-up)
Download the repository to your local computer and unzip. In the terminal, [change the working folder](https://ss64.com/osx/cd.html) to the directory containing the appraise package folder and setup.py, and run the following line:

```
pip install -e .
```


## References

Manuscript:

Xiaozhe Ding\*, Xinhong Chen, Erin E. Sullivan, Timothy F Shay, Viviana Gradinaru\*. APPRAISE: Fast, accurate ranking of engineered proteins by receptor binding propensity using structural modeling. BioRxiv (2023). \* Corresponding authors.

[APPRAISE Github repository](https://github.com/xz-ding/APPRAISE)

(The repository contains the latest version of APPRAISE package and demo notebooks.)

[ColabFold Github repository](https://github.com/sokrypton/ColabFold)

(ColabFold provides a panel of user-friendly tools for structure modeling that are used by APPRAISE.)
