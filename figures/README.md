# figures

The nine figures the report shows. `report.ipynb` links to them by these exact names, so
saving a figure under a different name breaks the image in the report.

| File | In the report | Comes from | Shows |
|---|---|---|---|
| `00_chosen_corridors.jpg` | Figure 2, section 3 | the midterm presentation, slide 10 | the three corridors, railway against motorway |
| `01_duration_threshold.png` | Figure 1, introduction | `main.ipynb`, the scatter of duration against start date | how rare disruptions over three days are |
| `02_causes.png` | Figure 3, section 5 | `main.ipynb`, the bar chart of causes | which causes dominate the long disruptions |
| `03_utrecht_planned.png` | Figure 4 | `read_folder_plot_data('Utrecht-Den Bosch', 'Planned')` | closure week against average week |
| `04_utrecht_unplanned.png` | Figure 5 | `read_folder_plot_data('Utrecht-Den Bosch', 'Unplanned')` | the same, unplanned |
| `05_dordrecht_planned.png` | Figure 6 | `read_folder_plot_data('Dordrecht-Roosendaal', 'Planned')` | |
| `06_dordrecht_unplanned.png` | Figure 7 | `read_folder_plot_data('Dordrecht-Roosendaal', 'Unplanned')` | |
| `07_maastricht_planned.png` | Figure 8 | `read_folder_plot_data('Maastricht-Heerlen', 'Planned')` | |
| `08_maastricht_unplanned.png` | Figure 9 | `read_folder_plot_data('Maastricht-Heerlen', 'Unplanned')` | |

## How to get them here without touching the code

Run the cell in `main.ipynb`, then right click the figure in the output and choose
"Save image as", into this folder, under the name in the table above. Eight times.

Saving them from the code instead is one line per figure, `fig.savefig(...)`, if the group
prefers that.
