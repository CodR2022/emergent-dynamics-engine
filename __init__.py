[project]
name = "emergent-system"
version = "0.1.0"
description = "A modular emergent feedback simulation with attraction, repulsion, entropy, and finite propagation delay."
requires-python = ">=3.10"
dependencies = [
    "numpy",
    "matplotlib",
]

[tool.setuptools.packages.find]
where = ["."]
include = ["emergent*"]
