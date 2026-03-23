# py-plottr

A simple CLI function plotter made with Python.

## Usage

The `plot` function in `plottr.py` can be invoked to plot a function on the terminal, or save the output to a file. 

## Preview

`plot.txt` has an example outputted plot.\* 

And here's a screenshot of the plot of `sin(x)` :

<img width="600" alt="Code_XGrUFT2WqK" src="https://github.com/user-attachments/assets/d4d79abf-ea95-4030-a7a0-f593086d3420" />

`plot(np.sin, xmin=-6.28, xmax=6.28, ymin=-1.5,ymax=1.5, res=1/16)`

\**The braille blank character appears to have a slightly lesser width than the other characters, making the curve distorted, not sure how this can be fixed.*

## Smoothing

When y values are spaced far apart, the graph looks discontinuous between far-spaced points, to fill these gaps use the `smooth` parameter. Here are some before and after screenshots:


| Before   | After    |
| :------: | :------: |
| <img width="500" alt="image" src="https://github.com/user-attachments/assets/688d0282-eddf-415a-a1e7-9709972afbfc" /> | <img width="500" alt="image" src="https://github.com/user-attachments/assets/3e9cac45-1e2c-40be-99e0-6aabca63e5a8" /> |
| <img width="500" alt="image" src="https://github.com/user-attachments/assets/99481f0f-a375-4f63-8d66-7b7c65eecae2" /> | <img width="500" alt="image" src="https://github.com/user-attachments/assets/9779c748-cda4-4ac4-8e08-19ad1c817c40" /> |

