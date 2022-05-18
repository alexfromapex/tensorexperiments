import torch

def main():

    if torch.backends.mps.is_available():
        print("Congratulations, you have GPU support for PyTorch! \U0001F389")
        # device = torch.device("mps")
    else:
        print("Sorry, it looks like something isn't working right with PyTorch GPU support")