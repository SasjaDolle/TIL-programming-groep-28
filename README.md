# The impact of railway disruptions on traffic intensity on parallel highways

Group project for TIL Python Programming, TU Delft, MSc Transport, Infrastructure and Logistics.

**Group 28** · Max Bevelander, Mees van den Berg, Sasja Dollé, Jaime Ram, Victor Schretlen
**Date:** 6 November 2026 · **Repository:** https://github.com/SasjaDolle/TIL-programming-groep-28

## 1. Overview

This project investigates to what extent planned and unplanned railway closures affect the
traffic intensity on the motorway running alongside the closed line. Six complete closures of
several days were selected on three corridors, one planned and one unplanned on each: Utrecht
to 's-Hertogenbosch beside the A2, Lage Zwaluwe to Roosendaal beside the A17, and Maastricht to
Heerlen beside the A79. For each closure the hourly traffic intensity during the week of the
closure is compared with the same hours of an average week.

## 2. Repository content

| Path | What it is |
|---|---|
| `report.ipynb` | **the report.** Text only, with the figures linked from `figures/` |
| `main.ipynb` | the traffic analysis: reads the disruption archive and the Dexter exports, produces the corridor figures, and runs the statistical tests |
| `Actual_Services.ipynb` | the check on whether trains really stopped running, from the realised services archive |
| `Filtering_Service_data.ipynb` | filters the raw services archive down to the per-closure files in the root |
| `data/` | the Dexter traffic exports, one folder per corridor, plus the disruption archive |
| `figures/` | the figures the report shows, with a README naming each one |
| `archive/` | files that are no longer part of the analysis, with a README saying why each is there |
| `*-*.csv`, `2022-utr-db.csv.gz` | the filtered realised services per closure, named `<month>-<year>-<corridor>` |

The traffic data under `data/` is organised as `data/data_<corridor>/<Planned or Unplanned>/`,
and each of those holds `Average`, the reference weeks, and `Delay_week`, the week of the
closure. Inside is one ZIP per weekday, each containing the Excel workbook as Dexter delivers
it.

## 3. How the report is built up

`report.ipynb` is the deliverable and contains no code; the analysis lives in the notebooks
beside it. Its sections run:

| Section | What it does |
|---|---|
| Title, contribution statement | who did what |
| 1. Introduction and motivation | the situation, the question, the definition of a closure, why it matters, the approach |
| 2. Research objective and questions | the main question and four sub-questions |
| 3. Scope | the three corridors with a map, the period, the unit of analysis, what is left out |
| 4. Data used | the four sources, what each contains, and what one observation is |
| 5. Case selection | how the three corridors and six closures were chosen |
| 6. Method | the comparison, the capacity line, the assumptions |
| 7. Results | the national picture, then two figures per corridor with a reading |
| 8. Answering the sub-questions | one block per sub-question |
| 9. Conclusions | the answer to the main question |
| 10. Discussion | what it means, five limitations, next steps |
| References, appendix, AI disclosure | |

## 4. Data sources

| Data | Source |
|---|---|
| Unplanned disruption data | [Rijden de Treinen, disruption archive](https://www.rijdendetreinen.nl/en/open-data/disruptions) |
| Planned disruption data | [Rijden de Treinen, archive of engineering works](https://www.rijdendetreinen.nl/werkzaamheden/archief) |
| Realised train services | [Rijden de Treinen, train archive](https://www.rijdendetreinen.nl/en/open-data/train-archive) |
| Highway intensity data | [Dexter, NDW open data](https://dexter.ndw.nu/opendata/avg) |

## 5. Reproducing the analysis

```bash
git clone https://github.com/SasjaDolle/TIL-programming-groep-28.git
cd TIL-programming-groep-28
pip install pandas numpy matplotlib openpyxl jupyterlab
jupyter lab
```

Python 3.12. Run `main.ipynb` from top to bottom; it reads only from `data/` and produces the
eight figures of section 7. `Actual_Services.ipynb` reads the filtered services files in the
root and can be run independently. Nothing has to be downloaded: every data file used is in
this repository.

No student numbers appear anywhere in this repository, because it is public.
