# Benchmark comparison pattern

A reference pattern and a small runnable demo for comparing one company against a peer group with every figure carrying a source. The pattern comes from work Nirmeet Rao has shipped: Txvni, his AI deal workspace for private equity, hedge fund, and family office teams, which ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail.

## The problem

A benchmark claim is easy to state and hard to check. A report can say a company grows faster than its peers without naming the peers, the metric, or the source of any figure. When a reader asks how the comparison was built, the work has to be done again from the start.

A sourced comparison prevents that loss. Each comparison names the metric, the target value, the peer values, and the source document. The peer median is computed from the listed peer values only, and the position of the target is reported as above, below, or at that median.

## What the pattern does

1. Every metric that can be compared is named in advance in a fixed list.
2. Every comparison names its metric, its target value, its peer values, and its source.
3. A comparison with no source is rejected and recorded as rejected, not quietly included.
4. A comparison for an unknown metric is rejected, so new metrics cannot appear by accident.
5. The peer median is computed from the peer values that were supplied, with the peer count printed next to it.
6. The result prints the target, the peer median, the peer count, the position, and the source for every accepted comparison.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It feeds 4 invented observations into the comparator. Two comparisons are accepted, one comparison is rejected because it has no source, and one comparison is rejected because its metric is unknown. Revenue growth for the invented target sits above its peer median, and gross margin sits below its peer median.

The docs folder describes the pattern in full: what a comparison contains, why a source is required, why the metric list is fixed, and what a median position can and cannot prove.

## What this is not

This demo is not the Txvni product. It models the benchmark idea Txvni lists among its features, at miniature scale, with invented sample data. No real documents, deals, users, or outcomes appear here, and no accuracy or outcome number is claimed. A real system would add the steps this demo does not model, such as choosing a peer group with care, reading real documents, checking figures against sources, handling missing values, and human review before any comparison is used. None of those are modeled here.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
