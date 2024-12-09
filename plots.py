import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager

doses = [0, 6, 36, 216]

ratios = {n: [] for n in doses}

# parsing

for i in doses:
    trpura_counts =[]
    csm_counts = []

    for j in range(1, 3):
        try:
            trpura_path = f"./data/{i}jm2-trpura{j}.csv"
            trpura_df = pd.read_csv(trpura_path)
            trpura_counts.append(len(trpura_df) - 1)

            csm_path = f"./data/{i}jm2-csm{j}.csv"
            csm_df = pd.read_csv(csm_path)
            csm_counts.append(len(csm_df) - 1)

        except FileNotFoundError:
            print("36 fell off ngl")

    for k, c in zip(trpura_counts, csm_counts):
        if(c > 0):
            ratio = k / c
            ratios[i].append(ratio)

        else:
            ratios[i].append(np.nan)


# plots

color1 = "#005088"
color2 = "darkred"

font = {'fontname':'Source Sans 3', 'fontsize':12}
font_properties = font_manager.FontProperties(
    family=font['fontname'], size=font['fontsize']
)

means = [np.nanmean(ratios[uv]) for uv in num]
maxes = [np.max(ratios[uv]) for uv in num]
mins = [np.min(ratios[uv]) for uv in num]

plt.plot(doses, means, color=color1, label="Mean line")
plt.fill_between(
    doses,
    mins,
    maxes,
    color=color1,
    alpha=0.3,
    label="Range between replicates"
)

once = 0
for uv in num:
    cnt = ratios[uv]
    gabel = f"Experimental data" if once == 0 else None
    once += 1
    plt.scatter(
        [uv]*len(cnt),
        cnt,
        color=color2,
        marker="x",
        alpha = 0.7,
        label=gabel
    )



plt.xlabel("UV Dosage (J/m^2)", **font)
plt.ylabel("Mating Efficiency (Mated-Unmated CFU Ratio)", **font)

plt.xticks(ticks=doses, **font)
plt.yticks(**font)

plt.title("Mating Efficiency by UV Dosage", **font)
plt.legend(prop=font_properties)

plt.savefig("./figures/scatter-range.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
