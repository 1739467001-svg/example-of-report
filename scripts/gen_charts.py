# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np, os

OUT="/home/user/example-of-report/assets/diagrams"
# register CJK font
fp="/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
font_manager.fontManager.addfont(fp)
prop=font_manager.FontProperties(fname=fp)
plt.rcParams["font.family"]=prop.get_name()
plt.rcParams["axes.unicode_minus"]=False

NAVY="#13315F"; BLUE="#2563EB"; SKY="#4A90E2"

# ---- Radar: evaluation dimensions (illustrative single course) ----
labels=["教学内容","学生状态","课程内容","教学过程","教学方法","科研教学融合"]
vals=[5.0,5.0,4.6,4.8,4.7,4.5]
N=len(labels)
ang=np.linspace(0,2*np.pi,N,endpoint=False).tolist(); ang+=ang[:1]
v=vals+vals[:1]
fig=plt.figure(figsize=(7.2,6.4),dpi=200)
ax=fig.add_subplot(111,polar=True)
ax.set_theta_offset(np.pi/2); ax.set_theta_direction(-1)
ax.set_ylim(0,5)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(labels,fontsize=15,color=NAVY)
ax.set_yticks([1,2,3,4,5]); ax.set_yticklabels(["1","2","3","4","5"],fontsize=10,color="#8A98AD")
ax.plot(ang,v,color=BLUE,linewidth=2.5)
ax.fill(ang,v,color=SKY,alpha=0.28)
for a,val in zip(ang[:-1],vals):
    ax.text(a,val+0.28,f"{val}",ha="center",va="center",fontsize=12,color=BLUE,fontweight="bold")
ax.set_title("评价维度雷达图（单门课程 · 示例）",fontsize=18,color=NAVY,fontweight="bold",pad=24)
ax.grid(color="#D8E2F0")
ax.spines["polar"].set_color("#D8E2F0")
plt.tight_layout()
plt.savefig(f"{OUT}/chart-eval-radar.png",dpi=200,bbox_inches="tight",facecolor="white")
print("wrote chart-eval-radar")
