# modelprocessing

A selection of scripts used for processing planetary plasma model outputs from RHybrid, BATSRUS, and HELIOSARES in a 1-1 manner. 

## Installation

The best way to use these files at the moment is with a working anaconda installation. After cloning the repository (``git clone git@github.com:brain-group/modelprocessing.git``), go to the directory (``cd modelprocessing``) and do ``conda develop .``

You can test that this works by starting python from any directory and entering ``import sliceplot``

In the future it would be nice to have this be an actually working anaconda package, but I do not have time to make it work like this yet!

## Making a pull request

If you change the code and want these changes to be available to other users its time to make a pull request. The recommended way to do this is to first fork the repository so you have your own copy to work with (there is a button at the top of the page). You should then modify the .git/config (or reclone your forked copy) such that this repository (under brain-group) is set as the upstream while your repository is set as the origin. See (https://help.github.jp/enterprise/2.11/user/articles/changing-a-remote-s-url/). You can then safely push and pull changes to your personal repository without affecting the development pipeline for other users.

When your code is in a place where a feature is ready then you can create a pull request from your local repository to this central repository (https://opensource.com/article/19/7/create-pull-request-github). I recommend squashing all the changes to make the history of this repo a little cleaner, but really that ship has sailed with all my garbage commits from early on :)

Everyone should have access to merge in pull requests to this repo

## Features/General about

There are a lot of scripts here, some of which are documented. Quick explanation of each of the major features:

- Conversion scripts: used to convert the various outputs into a common h5 format. The rest of the scripts only work on h5 files so these should be run first
- Plotting scripts: sliceplot, phaseplot, whisker_plot, flythrough_compare etc. Used to directly create plots, see below for paradigms
- General Functions: I need to split this out, about half of these are just general helper functions and half are functions I created to automagically load all the datasets for a given project. These will not work for other users and I should probably change or delete them.
- xdmf writer: this will create an xdmf file to go along with the h5 file, this can then be used to make fancy/exploratory visuals in paraview
- spherical_flux: this will go calculate quantities over a spherical slice and save the outputs to a csv if required. These quantities do not all need to be fluxes despite the name
- colorbar only: just makes a colorbar on its own, sometimes its faster to just manually make your plot afterwards rather than fight matplotlib for a million years.

### Plotting Paradigm

All the plotting scripts are setup so that if you can use them as scripts or just import the base functions. To get a feel for how to use the base functions look in the main/make_plot functions. Because I was just designing this for myself using them as scripts does work behind the scenes to load all the datasets you're interested in automatically, many of these functions will not work for other users. Take a look at the usage at the top, if it directly references one dataset on disk then it will probably work for you. Either way you can directly import the base functions and use them yourself.

### Workflow Advice

You can chose to ignore this, but I find this workflow useful :)

At the start of a new project you'll probably not know exactly what kind of plots you want and will need to be doing a lot of exploratory visualizations. This is what jupyter notebooks excel at. To use these functions in your notebook you'll just want to import the relevant bits, use them, and create the visualizations inline.

At some point, generally when you're nailing down what figures you'll want in your paper, it's a really good idea to create scripts that generate each of your figures rather than using a notebook. While notebooks are really good for exploration, they do not version control particularly well, have a lot of weird state dependent problems, etc. that can make it really hard to regenerate exactly the figure you want a couple months down the line when you get reviewer comments. At this point you should make your own (different from this) repository with 1 script/figure (or roughly that) that should load the data, do whatever analysis you need, and generate the figure with no additional input from you. The easiest way to do this is to just copy the bits from your jupyter notebook into a file and then save the figure to disk rather that showing it inline. 
