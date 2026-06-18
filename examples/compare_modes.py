from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_snapshots(snapshots, title="Emergent Simulation", save_path=None):
    """
    Plot a row of snapshots.
    """
    if not snapshots:
        raise ValueError("No snapshots to plot.")

    fig, axs = plt.subplots(1, len(snapshots), figsize=(4 * len(snapshots), 4))

    if len(snapshots) == 1:
        axs = [axs]

    for i, snap in enumerate(snapshots):
        axs[i].imshow(snap, cmap="viridis")
        axs[i].set_title(f"Frame {i}")
        axs[i].axis("off")

    plt.suptitle(title)
    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=160)

    return fig


def plot_metrics(metrics, save_path=None):
    """
    Plot standard deviation and collapse count over time.
    """
    if not metrics:
        raise ValueError("No metrics to plot.")

    steps = [m["step"] for m in metrics]
    std = [m["std"] for m in metrics]
    collapses = [m["collapse_count"] for m in metrics]

    fig, ax1 = plt.subplots(figsize=(9, 4))

    ax1.plot(steps, std)
    ax1.set_xlabel("Step")
    ax1.set_ylabel("State Std Dev")

    ax2 = ax1.twinx()
    ax2.plot(steps, collapses, linestyle="--")
    ax2.set_ylabel("Collapse Count")

    plt.title("System Activity Metrics")
    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=160)

    return fig


def save_array(array: np.ndarray, path):
    """
    Save a numpy array.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    np.save(path, array)
