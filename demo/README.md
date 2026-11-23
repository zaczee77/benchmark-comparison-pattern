# Demo: benchmark comparison

A small reference demo of the benchmark idea behind Txvni: each comparison names a metric, a target value, peer values, and a source, comparisons with no source or an unknown metric are rejected with a reason, and the peer median and the target position are computed from the supplied values only.

## How to run it

From the repository root, or from this folder:

```
python3 demo/benchmark_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. It feeds 4 invented observations into the comparator, covering revenue growth, gross margin, and EBITDA margin, plus one observation for an unknown metric.
2. It accepts 2 comparisons and rejects 2: one EBITDA margin observation with no source, and one churn rate observation whose metric is not in the fixed list.
3. It computes a peer median of 16.0 percent for revenue growth and 41.0 percent for gross margin, each from 4 peer values.
4. It reports the invented target as above the median on revenue growth and below the median on gross margin, with the source printed for each comparison.

## What it printed when it was tested

4 observations received, 2 accepted, 2 rejected with reasons missing source and unknown metric, peer medians 16.0 percent and 41.0 percent, positions above and below, and all checks passed.

## What the sample data is

Every company figure and document name in `benchmark_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real document, a real deal, a real peer group, a real user, or a real comparison. A real system would choose a peer group with care, build comparisons from real ingested documents, and keep human review before any comparison is used. None of that is modeled here.

## Files

1. `benchmark_demo.py`: the demo. The fixed metric list, the sample observations, the median function, the comparator, the rejection rules, and the built in assertions.
2. `README.md`: this file.
