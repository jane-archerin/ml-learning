# PyTorch & Tensors

## What is PyTorch?
PyTorch is a Python library for building and training machine learning models. 
It is the most widely used framework in research, including for protein design 
tools like RFdiffusion.

## What is a Tensor?
A tensor is a generalization of arrays:

| Type | Dimensions | Example |
|------|-----------|---------|
| Scalar | 0D | `5.0` |
| Vector | 1D | `[1, 2, 3]` |
| Matrix | 2D | `[[1,2],[3,4]]` |
| Tensor | 3D+ | stack of matrices |

If you already know NumPy arrays, tensors are the same thing but with two 
superpowers:
1. **GPU acceleration** — tensors can run on a GPU, which is critical for 
training ML models fast
2. **Automatic gradients** — PyTorch tracks derivatives through tensors 
automatically, which is how neural networks learn

## Basic Example
```python
import torch

x = torch.tensor([1.0, 2.0, 3.0])
print(x)        # tensor([1., 2., 3.])
print(x.shape)  # torch.Size([3])
```

## Connection to Protein Design
In your DDPM project, everything was tensors under the hood — backbone 
coordinates, noise values, model weights. All of it.
