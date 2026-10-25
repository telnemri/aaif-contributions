I reproduced the documented checks at `25a47f6f9deeed4a6f6d43b6d8393205d0bc494f` on macOS arm64 with Python 3.12.13 and `cryptography==50.0.1` in a fresh virtual environment.

All three commands exited 0:

```sh
python3 test-kit/run.py
python3 test-kit/run.py --reader naive --expect-fail
python3 test-kit/generate.py --check
```

The reference reader matched all six expected answers. The naive reader differed on all four declared discriminating cases. Fixture regeneration matched. The upstream checkout remained unchanged.

One contribution-path question is reproducible. `TEMPLATE/mapping.md` directs a contributor to `test-kit/contributions/AGENT-OR-SDK-NAME/`, while `run.py` discovers only `test-kit/cases/`. In a temporary copy, I added the existing changed-ticket records and basis under `contributions/review-probe/`, with an intentionally wrong expected answer. The runner still reported six passing cases; it did not check that example. Moving the same example to `cases/review-probe/` produced `DIFF review-probe` and exit 1.

Could the contribution instructions state where a new example belongs and which command checks it? A documented run path would help the contributor workflow in #42 and #46. I have not assumed that every contribution should run automatically.

This used the kit's own reader and known expectations. It is not an independent reader implementation or answer-blind evaluation. The inputs are synthetic. The signature checks do not authenticate tenant metadata or establish real effects. I did not test runtime exports or full relationship coverage.

Evidence: [commands, raw outputs, input hashes, and reproduction script](https://github.com/telnemri/aaif-contributions/tree/c7ad56bd03cf8064f9f91a2eef3ee76ba8713fd9/evidence/pr57)

Prepared with Codex AI assistance and awaiting Tamer's review before posting.
