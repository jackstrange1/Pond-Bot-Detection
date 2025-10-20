# Pond Bot Detection — README

> **One-stop repo template & step-by-step guide** to build a dataset + method submission for the Pond bounty (Bot & Sybil detection). Use this as your repo README, edit where needed, and include your Pond profile URL below.

**Pond profile URL:** https://cryptopond.xyz/developer/fe5ce854-6b5f-11f0-a1f3-024775222cc3

---

## 1. Project Title & Short Summary

**Title:** Example: `SybilWallets-Detector`

**One-line summary:** `A reproducible pipeline to detect Sybil wallet clusters using transaction and interaction graph features.`

---

## 2. Problem definition & threat model

* **Problem:** Detect Sybil wallets that participate in bounty/reward-farming.
* **Scope:** Arbitrum + Ethereum L2s (example). Focus on on-chain behavioral signals (no PII).
* **Threat model:** Attackers create many wallets to farm rewards and interact in coordinated ways. Goal is to flag accounts for manual review.

---

## 3. Repo structure (create these files & folders)

