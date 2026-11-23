# The benchmark comparison pattern

## Where the pattern comes from

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. Its own description lists document and spreadsheet ingestion, cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail. Benchmarks sit in the middle of that chain. Earlier steps extract figures from documents, and later steps such as IC memos use the comparison when they explain why a deal deserves attention.

The same need appears wherever one company is judged against a group. If the metric, the peer values, and the source travel with the claim, a reader can check the claim in one step. If they do not, checking means redoing the research.

## The comparison

A comparison holds a metric name, a target value, a list of peer values, and a source name. The metric name says what is being measured. The target value is the figure for the company under review. The peer values are the same metric for each company in the peer group. The source name is the document the figures came from, named exactly as it was ingested, so a reader can find it again.

The comparator computes one summary figure from the peer values: the median. The median is used because a single very large or very small peer value moves it less than it moves an average. The comparator then reports whether the target sits above, below, or at that median.

## The four rules

1. A source is required. A comparison with an empty source is rejected and the rejection is recorded with its reason. A claim that cannot be traced is not included quietly and is not fixed by guessing a source.
2. Metrics are fixed in advance. The comparator holds the list of metric names it accepts. A comparison naming a metric outside that list is rejected, so the report keeps the shape the team expects and new metrics cannot appear by accident.
3. Peers must be present. A comparison with no peer values is rejected, because a median with no peers behind it would be a claim with no group behind it.
4. The peer count stays visible. Printing the count next to the median makes the strength of the comparison plain. A median from four peers and a median from forty peers should not read the same way.

## Design principles

1. Comparison is not judgment. The comparator reports a position against a median. It does not say whether that position is good, bad, or important. That judgment stays with human review.
2. Rejection is information. The rejected list, with reasons, tells the team exactly what work remains: find a source for one figure, or decide whether a new metric truly belongs in the list.
3. A median is a narrow claim. It describes the middle peer value in the group that was supplied. It does not prove the group was chosen well, the figures are correct, or the target will keep its position. Those judgments stay outside the comparator.
4. The source stays visible in the output. Printing the source with each comparison makes checking cheap for the reader and keeps the habit of sourcing strong for the writer.

## What the demo shows, and what it does not show

The demo shows the pattern at miniature scale: 4 invented observations, 2 accepted, 2 rejected with reasons, peer medians of 16.0 percent and 41.0 percent, and positions above and below. It does not show real documents, real extraction, real peer selection, real figures, or the Txvni product, and it claims no accuracy or outcome result. It is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
