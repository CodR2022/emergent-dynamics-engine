from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def ensure_output_dir(path: str | Path = "outputs") -> Path:
    """
    Ensure the output directory exists.
    """
    output_dir = Path(path)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def plot_snapshots(
    snapshots,
    title: str = "Emergent System Snapshots",
    save_path: str | Path | None = None,
):
    """
    Plot captured simulation snapshots.
    """
    if not snapshots:
        return None

    count = len(snapshots)

    fig, axes = plt.subplots(1, count, figsize=(4 * count, 4))

    if count == 1:
        axes = [axes]

    for index, snapshot in enumerate(snapshots):
        axes[index].imshow(snapshot)
        axes[index].set_title(f"Snapshot {index + 1}")
        axes[index].axis("off")

    fig.suptitle(title)
    fig.tight_layout()

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150)

    plt.show()

    return fig


def plot_metrics(metrics, save_path: str | Path | None = None):
    """
    Plot simulation metrics over time.
    """
    if not metrics:
        return None

    steps = [item["step"] for item in metrics]
    means = [item["mean"] for item in metrics]
    stds = [item["std"] for item in metrics]
    collapses = [item["collapse_count"] for item in metrics]
    strength_means = [item["strength_mean"] for item in metrics]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(steps, means, label="mean")
    ax.plot(steps, stds, label="std")
    ax.plot(steps, strength_means, label="strength_mean")
    ax.plot(steps, collapses, label="collapse_count")

    ax.set_title("Simulation Metrics")
    ax.set_xlabel("Step")
    ax.legend()
    fig.tight_layout()

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150)

    plt.show()

    return fig
