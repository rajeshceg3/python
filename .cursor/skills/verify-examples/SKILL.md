---
name: verify-examples
description: Verify the python example collection's safe arithmetic journey and syntax, and expose external-script prerequisites without sending messages or using accounts.
---
# Verify Python examples

## Launch

Requires Python3. Run `python3 .cursor/skills/verify-examples/helpers/drive.py` from root. The collection has unrelated examples, not one app. Safe local surface: pytest/sumproduct.py. It has no dependencies. Other surfaces need requests/provider keys, MySQL, microphone, plotting packages or external browser accounts; do not import them merely to test syntax because top-level code performs effects.

## Doctor

Parse all nine current product Python files using ast, without importing them. Then copy only the pure arithmetic module/test into isolated scratch. The directory named pytest is source, not an installed pytest runner; `python -m pytest` may resolve to it and fail. The helper explicitly imports the actual shipped test by path instead.

## Drive

Actual sumproduct(3,2), zero, negative and fractional inputs must return expected tuples; then execute the existing test_sumproduct function. No mock arithmetic. The feature map records separate unmet preconditions for other scripts. No database/network/browser/microphone interaction is launched by this helper.

## Evidence

`artifacts/verification/python-examples.json` records hashes/syntax results, actual arithmetic child stdout/stderr/exit and explicit unverified surfaces. A pass means syntax plus arithmetic only, not all examples verified. Do not count blocked external workflows as behavior passes. Never record secrets, account handles, messages or private database rows in evidence.

## Cleanup

Bound arithmetic child to15seconds; write proof before removing only owned scratch. Proof survives and is checked. No server, data store or external session is created.

## Helpers

`python3 .cursor/skills/verify-examples/helpers/drive.py` is the safe initial verification command. Use `/maintain-verification-skill` when examples change. Add isolated external-service tests only when prerequisites and effect authority are grounded; never weaken failed contracts to mark the repo fully covered.
