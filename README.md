# BRE-model
Business Rules Engine (BRE) for loan disbursement using mathematical scoring models and a set of if-else rules. This BRE will calculate a Loan Eligibility Score (LES) based on input parameters, and determine the maximum loan amount as a multiple of net monthly income, scaled by risk.


Loan Disbursement Model –  Document
1. Purpose
This document outlines the rationale, assumptions, and methodology behind the creation of a mathematical rule-based model (BRE) for determining the maximum loan disbursement amount based on individual and household financial data.

2. Overview
Given the absence of large-scale training data, a deterministic scoring model has been designed. This model incorporates domain-driven rules and business logic to assign a Loan Eligibility Score (LES) to each applicant. Based on the LES, a risk category is determined, which guides the maximum permissible loan amount.

3. Key Decision-Making Factors
The model considers 13 core variables, grouped under key themes relevant to creditworthiness. Each factor was assigned a relative weight based on its impact on loan repayment behavior as commonly observed in the financial sector.

3.1. Income Stability (15%)
Long-term, steady employment is a key signal of financial reliability.

Short employment durations often correlate with high turnover and potential payment gaps.

3.2. Bank Statement Insights (10%)
Frequent deposit gaps and low month-end balances may indicate poor cash flow management or financial distress.

These indicators help filter out temporarily overleveraged applicants.

3.3. Household Income (10%)
An additional income source in the household increases the buffer against default.

It reflects a more robust support system for managing EMIs.

3.4. FOIL – Fixed Obligations to Income Level (15%)
This ratio evaluates the affordability of new EMIs given existing financial responsibilities.

FOIL thresholds are aligned with commonly accepted lending standards.

3.5. Residence Stability (5%)
Frequent relocations can signal job instability, financial stress, or non-rooted behavior, which may increase lending risk.

3.6. Sector-wise Risk Evaluation (5%)
Certain sectors (e.g., IT, banking) have historically lower volatility, while others (e.g., informal labor) may be risk-prone.

3.7. Alternate Data Signals (5%)
Mobile recharge patterns act as indirect proxies for income consistency, especially in underbanked populations.

3.8. Location Risk (5%)
Regional economic factors (e.g., default rates, unemployment) significantly influence loan recovery probabilities.

3.9. Credit Bureau Score (20%)
A widely accepted indicator of past repayment behavior and overall creditworthiness.

3.10. Career Progression & Company Loyalty (10%)
Upward movement in a single organization suggests long-term growth potential and stable cash flows.

Long company tenures often indicate lower career volatility.

4. Scoring and Thresholds
Each factor is scored based on fixed ranges, producing a Loan Eligibility Score (LES) between 0 and 100.

LES Range	Risk Category	Max Loan Multiplier
85–100	Low Risk	20 × Net Monthly Income
65–84	Medium Risk	15 × Net Monthly Income
45–64	High Risk	10 × Net Monthly Income
Below 45	Rejected	0

Net Monthly Income = Monthly Income – Fixed Obligations

This ensures loans are sized according to real repayment capacity.