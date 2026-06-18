from emergent import Params, Simulation
from emergent.utils import plot_snapshots, plot_metrics


def main():
    params = Params(
        alpha=0.60,
        beta=0.40,
        gamma=0.30,
        delta=0.20,
        delay=3,
        noise=0.01,
        instability_threshold=0.25,
        seed=42,
    )

    sim = Simulation(size=80, params=params, mode="layered")

    snapshots = sim.run(
        steps=300,
        capture_steps=[50, 150, 250, 300],
    )

    plot_snapshots(
        snapshots,
        title="Layered Emergent System",
        save_path="outputs/snapshots.png",
    )

    plot_metrics(
        sim.metrics,
        save_path="outputs/metrics.png",
    )

    print("Engine terms:", sim.engine.describe())
    print("Final metrics:", sim.metrics[-1])
    print("Saved outputs to outputs/")


if __name__ == "__main__":
    main()
