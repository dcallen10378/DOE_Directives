# DOE EVMS Gold Card — Earned Value Management System (EVMS) Gold Card

- **Document:** DOE EVMS Gold Card
- **Type:** Quick-reference card
- **Cite as:** the DOE EVMS Gold Card
- **Official source:** https://www.energy.gov/projectmanagement/articles/earned-value-management-system-evms-gold-card
- **Pages:** 1  •  **Extraction:** OCR of the single-page graphical card, then hand-cleaned for
  readability. Formulas verified against standard DOE EVMS definitions; if a value matters,
  confirm against the official card image at the source link above.

---

[p. 1]

## Performance Baseline Components (acronyms)

The Performance Baseline must clearly document scope and the CD-4 date.

- **AUW** = Authorized Unpriced Work (contractually approved, but not yet negotiated)
- **CA** = Control Account (includes AUW) = WPs + PPs
- **CBB** = Contract Budget Base = PMB + MR; valid when 1 contract to 1 project; else use PBB
- **CP** = Contract Price = CBB + Profit/Fee
- **MR** = Management Reserve — held by the **contractor** (Contingency is held by **DOE**)
- **NCC** = Negotiated Contract Cost = Contract price less Profit/Fee
- **ODC** = Other Direct Costs
- **OTB** = Over Target Baseline — an established performance budget that exceeds the value of the negotiated contract
- **PB** = Performance Baseline (TPC) = CP + Contingency + DOE ODC
- **PBB** = Project Budget Base = PMB + MR; valid when 1 contract to multiple projects
- **PMB** = Performance Measurement Baseline = CAs + UB + SLPP
- **PP** = Planning Package (far-term activities within a CA)
- **SLPP** = Summary Level Planning Package
- **TAB** = Total Allocated Budget = CBB + OTB (or PMB + MR + OTB)
- **TPC** = Total Project Cost
- **UB** = Undistributed Budget (activities not yet distributed to a CA)
- **WP** = Work Package (near-term, detail-planned activities within a CA)

> Note: AUW funding is authorized by an NTE (not-to-exceed) value and added to CP. The amount of
> AUW budget added to the CBB/PBB depends on the estimate for the authorized scope; the full amount
> of the scope does not increase the CP until negotiated.

## EVMS Basic Components

- **AC** = Actual Cost = ACWP = Actual Cost of Work Performed
- **EV** = Earned Value = BCWP = Budgeted Cost for Work Performed
- **PV** = Planned Value = BCWS = Budgeted Cost for Work Scheduled
- **BAC** = Budget at Completion = sum of all BCWS (total Planned Value)
- **EAC** = Estimate at Completion = ACWP + Estimate to Complete (ETC)

## Variances

- **CV** = EV − AC = BCWP − ACWP = **Cost Variance**
- **SV** = EV − PV = BCWP − BCWS = **Schedule Variance**
- **CV%** = (EV − AC)/EV = (BCWP − ACWP)/BCWP = Cost Variance (%)
- **SV%** = (EV − PV)/PV = (BCWP − BCWS)/BCWS = Schedule Variance (%)
- **VAC** = BAC − EAC = **Variance at Completion**

## Overall Status

- **% scheduled** = PVcum/BAC = BCWScum/BAC
- **% complete** = EVcum/BAC = BCWPcum/BAC
- **% budget spent** = ACcum/BAC = ACWPcum/BAC
- **Work Remaining (WR)** = BAC − EVcum = BAC − BCWPcum

## Performance Indices (favorable is > 1.0, unfavorable is < 1.0)

- **CPI** = EV/AC = BCWP/ACWP = Cost Performance Index
- **SPI** = EV/PV = BCWP/BCWS = Schedule Performance Index
- **TCPIeac** = WR/(EAC − ACcum) = EAC-based To-Complete Performance Index

## Estimate at Completion (EAC) formulae

- **EAC (general)** = BAC/CPIcum
- **EAC (CPI)** = ACcum + WR/CPIcum
- **EAC (composite)** = ACcum + WR/(CPIcum × SPIcum)
- **EAC (3-Mo. CPI)** = ACcum + WR/CPI3mo
  - where **CPI3mo** = (IncEVn + IncEVn-1 + IncEVn-2) / (IncACn + IncACn-1 + IncACn-2)
