# -*- coding: utf-8 -*-
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
OUT="/home/user/example-of-report/assets/diagrams"
fp="/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
font_manager.fontManager.addfont(fp)
plt.rcParams["font.family"]=font_manager.FontProperties(fname=fp).get_name()
plt.rcParams["axes.unicode_minus"]=False
NAVY="#13315F"; BLUE="#2563EB"; SKY="#4A90E2"; GOLD="#E8A23D"; GRAY="#5C6B82"

# ---- Chart A: 各学院督导评价次数 (示例) horizontal bar ----
colleges=["工商管理学院","经济学院","会计学院","金融学院","管理工程与电子商务学院",
          "法学院","外国语学院","统计与数学学院","信息与电子工程学院","食品与生物工程学院"]
vals=[42,38,35,29,26,22,19,17,14,11]
order=np.argsort(vals)
colleges=[colleges[i] for i in order]; vals=[vals[i] for i in order]
fig,ax=plt.subplots(figsize=(8.6,5.2),dpi=200)
cmap=plt.cm.Blues
colors=[cmap(0.45+0.5*v/max(vals)) for v in vals]
bars=ax.barh(colleges,vals,color=colors,edgecolor="white",height=0.66)
for b,v in zip(bars,vals):
    ax.text(v+0.6,b.get_y()+b.get_height()/2,str(v),va="center",fontsize=11,color=NAVY,fontweight="bold")
ax.set_xlabel("督导评价次数",fontsize=12,color=GRAY)
ax.set_title("各学院督导评价次数（示例 · 待接入真实数据）",fontsize=15,color=NAVY,fontweight="bold",pad=14)
ax.set_xlim(0,max(vals)*1.12)
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#D8E2F0"); ax.spines["bottom"].set_color("#D8E2F0")
ax.tick_params(colors=NAVY,labelsize=10.5)
plt.tight_layout(); plt.savefig(f"{OUT}/chart-college.png",facecolor="white"); plt.close()
print("wrote chart-college")

# ---- Chart B: 评分区间分布 (示例) vertical bar ----
bins=["4.5 - 5.0","4.0 - 4.5","3.5 - 4.0","3.0 - 3.5","< 3.0"]
cnt=[58,71,34,12,3]
fig,ax=plt.subplots(figsize=(6.2,5.2),dpi=200)
colors2=[BLUE,SKY,"#86B7EA",GOLD,"#D98A8A"]
bars=ax.bar(bins,cnt,color=colors2,edgecolor="white",width=0.62)
for b,v in zip(bars,cnt):
    ax.text(b.get_x()+b.get_width()/2,v+1.2,str(v),ha="center",fontsize=11,color=NAVY,fontweight="bold")
ax.set_ylabel("课程数",fontsize=12,color=GRAY)
ax.set_title("督导评分区间分布（示例）",fontsize=15,color=NAVY,fontweight="bold",pad=14)
ax.set_ylim(0,max(cnt)*1.16)
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.spines["left"].set_color("#D8E2F0"); ax.spines["bottom"].set_color("#D8E2F0")
ax.tick_params(colors=NAVY,labelsize=10.5)
plt.tight_layout(); plt.savefig(f"{OUT}/chart-scoredist.png",facecolor="white"); plt.close()
print("wrote chart-scoredist")
