import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
from typing import Any

class GNNFaultModel(torch.nn.Module):
    def __init__(self, num_node_features: int, hidden_channels: int):
        super().__init__()
        self.conv1 = GCNConv(num_node_features, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, 2)

    def forward(self, x: torch.Tensor, edge_index: torch.Tensor) -> torch.Tensor:
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

def train_model(model: GNNFaultModel, data: Any, optimizer: torch.optim.Optimizer) -> float:
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)
    loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()
    return float(loss.item())

def predict(model: GNNFaultModel, data: Any) -> torch.Tensor:
    model.eval()
    with torch.no_grad():
        out = model(data.x, data.edge_index)
        return out.argmax(dim=1)
