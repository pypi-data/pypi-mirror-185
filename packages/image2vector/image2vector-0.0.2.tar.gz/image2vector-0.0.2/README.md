# image2vector

## Introduce

Transforming images into 512-dimensional vectors by residual neural networks

⭐️ 🌟 ✨ ⚡️ ☄️ 💥

## Installation

Package is uploaded on PyPI.

You can install it with pip:

```shell
pip install image2vector
```

## Requirements

Python -- one of the following:

- CPython : 3.8 and newer ✅
- PyPy : Software compatibility not yet tested ❓

## Documentation

📄 Intensified preparation in progress

## Example

### Create it

```python
from pathlib import Path
from iv import ResNet, l2

resnet = ResNet(weight_file='weight/gl18-tl-resnet50-gem-w-83fdc30.pth')


vector = resnet.gen_vector('resources/images/baku.jpg')

print('distance is ', l2(vector, vector))

```
