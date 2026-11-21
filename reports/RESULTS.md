# BinaryEmbeddingLab — measured local run

Sign quantization of synthetic vectors. Raw storage excludes index and metadata; no semantic-quality claim.

## Results

```json
{
  "recall_at_10": 0.306,
  "float_storage_bytes": 256000,
  "packed_storage_bytes": 8000,
  "storage_ratio": 32.0,
  "checks": [
    "Actual bit packing reduces raw vector storage 32x",
    "Real Hamming distances computed"
  ],
  "scope": "Sign quantization of synthetic vectors. Raw storage excludes index and metadata; no semantic-quality claim."
}
```

Local experiment assertions passed. This does not establish production readiness or performance on real customer data. Source fingerprints and dependency versions are in results.json.
