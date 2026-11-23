"""Reference demo: comparing a target company against a peer benchmark.

Every sample name and figure in this file is invented.
The demo models the benchmark step described for Txvni, an AI deal
workspace that lists benchmarks among its features. It is not the
Txvni product and it makes no claim about real usage or outcomes.
"""

ALLOWED_METRICS = ["revenue_growth", "gross_margin", "ebitda_margin"]


def median(values):
    ordered = sorted(values)
    count = len(ordered)
    middle = count // 2
    if count % 2 == 1:
        return float(ordered[middle])
    return (ordered[middle - 1] + ordered[middle]) / 2.0


class BenchmarkComparator:
    def __init__(self, allowed_metrics):
        self.allowed_metrics = list(allowed_metrics)
        self.comparisons = []
        self.rejected = []

    def add_comparison(self, metric, target_value, peer_values, source):
        if metric not in self.allowed_metrics:
            self.rejected.append((metric, "unknown metric"))
            return False
        if not source or not source.strip():
            self.rejected.append((metric, "missing source"))
            return False
        if not peer_values:
            self.rejected.append((metric, "missing peers"))
            return False
        peer_median = median(peer_values)
        if target_value > peer_median:
            position = "above"
        elif target_value < peer_median:
            position = "below"
        else:
            position = "at"
        self.comparisons.append(
            {
                "metric": metric,
                "target": target_value,
                "peer_median": peer_median,
                "peer_count": len(peer_values),
                "position": position,
                "source": source,
            }
        )
        return True


SAMPLE_OBSERVATIONS = [
    ("revenue_growth", 25.0, [10.0, 14.0, 18.0, 22.0], "sample_financials.csv"),
    ("gross_margin", 39.0, [38.0, 40.0, 42.0, 44.0], "sample_financials.csv"),
    ("ebitda_margin", 20.0, [12.0, 15.0, 18.0, 21.0], ""),
    ("churn_rate", 5.0, [3.0, 4.0, 6.0, 7.0], "sample_peers.csv"),
]


def main():
    comparator = BenchmarkComparator(ALLOWED_METRICS)
    accepted = 0
    for metric, target_value, peer_values, source in SAMPLE_OBSERVATIONS:
        if comparator.add_comparison(metric, target_value, peer_values, source):
            accepted += 1

    total = len(SAMPLE_OBSERVATIONS)
    print(f"{total} observations received, {accepted} accepted, {len(comparator.rejected)} rejected")
    assert total == 4 and accepted == 2 and len(comparator.rejected) == 2

    reasons = sorted(reason for _, reason in comparator.rejected)
    print(f"rejection reasons: {reasons}")
    assert reasons == ["missing source", "unknown metric"]

    for item in comparator.comparisons:
        print(
            f"{item['metric']}: target {item['target']} percent, "
            f"peer median {item['peer_median']} percent from {item['peer_count']} peers, "
            f"position {item['position']}, source {item['source']}"
        )

    positions = [item["position"] for item in comparator.comparisons]
    print(f"positions: {positions}")
    assert positions == ["above", "below"]

    medians = [item["peer_median"] for item in comparator.comparisons]
    assert medians == [16.0, 41.0]

    print("all checks passed")


if __name__ == "__main__":
    main()
