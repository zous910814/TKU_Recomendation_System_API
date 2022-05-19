import torch
import sys
sys.path.append("/main.py")
from main import NFM,DNN,BiInteractionPooling,DenseFeat,SparseFeat


model = torch.load("./data/NFM.pth")
print()