# brownian-diffuser

Forward integrate torch neural networks

Similar to [`torchsde.sdeint`](https://github.com/google-research/torchsde) or [`torchdiffeq.odeint`](https://github.com/rtqichen/torchdiffeq) but for vanilla neural networks as implemented by [`TorchNets`](https://github.com/mvinyard/torch-nets/)

### Example usage

**`BrownianDiffuser`**
```python
from brownian_diffuser import BrownianDiffuser

diffuser = BrownianDiffuser()
```

```python
from torch_nets import TorchNet
import torch

net = TorchNet(50, 50, [400, 400])
X0 = torch.randn([200, 50])
t = torch.Tensor([2, 4, 6])
```

```python
X_pred = diffuser(net, X0, t, n_steps=40, stdev=0.5, max_steps=None, return_all=False)
X_pred.shape
```
```
torch.Size([3, 200, 50])
```

**`BrownianMotion`**
```python
from brownian_diffuser import BrownianMotion

X_state = torch.randn([400, 50])

BM = BrownianMotion(X_state, stdev=0.5, n_steps=40)
Z = BM()
Z.shape
```
```
torch.Size([40, 400, 50])
```

### Installation

```
pip install brownian-diffuser
```
