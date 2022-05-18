import torch

def main():

    if torch.has_mps:
        print("Congratulations, you have GPU support for PyTorch! \U0001F389")
    else:
        print("Sorry, it looks like something isn't working right with PyTorch GPU support")