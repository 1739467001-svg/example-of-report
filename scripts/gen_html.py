# -*- coding: utf-8 -*-
import base64, os
ROOT="/home/user/example-of-report"
A=f"{ROOT}/assets"

def b64(path):
    with open(path,"rb") as f:
        return "data:image/png;base64,"+base64.b64encode(f.read()).decode()

IMG={
 "cover":b64(f"{A}/diagrams/cover-bg.png"),
 "data":b64(f"{A}/diagrams/data-foundation.png"),
 "role":b64(f"{A}/diagrams/role-matrix.png"),
 "arch":b64(f"{A}/diagrams/architecture.png"),
 "eval":b64(f"{A}/diagrams/eval-system.png"),
 "loop":b64(f"{A}/diagrams/business-loop.png"),
 "radar":b64(f"{A}/diagrams/chart-eval-radar.png"),
 "dash":b64(f"{A}/screenshots/dashboard.png"),
 "rec":b64(f"{A}/screenshots/eval-record.png"),
 "item":b64(f"{A}/screenshots/eval-form-item.png"),
}

# ---- icon set (feather-style) ----
def icon(name):
    P={
     "filter":'<polyline points="22 3 2 3 10 12.5 10 19 14 21 14 12.5 22 3"/>',
     "calendar":'<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
     "clipboard":'<path d="M9 2h6a1 1 0 0 1 1 1v2H8V3a1 1 0 0 1 1-1z"/><rect x="4" y="4" width="16" height="18" rx="2"/><polyline points="9 14 11 16 15 11"/>',
     "chart":'<line x1="4" y1="20" x2="20" y2="20"/><rect x="6" y="11" width="3" height="7"/><rect x="11" y="7" width="3" height="11"/><rect x="16" y="13" width="3" height="5"/>',
     "bell":'<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/>',
     "users":'<path d="M17 21v-2a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v2"/><circle cx="10" cy="8" r="4"/><path d="M21 21v-2a4 4 0 0 0-3-3.87"/>',
     "book":'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
     "layers":'<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
     "target":'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
     "check":'<polyline points="20 6 9 17 4 12"/>',
     "rocket":'<path d="M5 13c-1.5 1.5-2 5-2 5s3.5-.5 5-2"/><path d="M14 4c3 0 6 3 6 3s-2 7-6 11l-4-1-3-3-1-4C10 6 11 4 14 4z"/><circle cx="15" cy="9" r="1.5"/>',
     "shield":'<path d="M12 2l8 3v6c0 5-3.5 8.5-8 11-4.5-2.5-8-6-8-11V5l8-3z"/><polyline points="9 12 11 14 15 10"/>',
    }
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg>'

def chip(t): return f'<span class="chip">{t}</span>'
def bullets(items):
    return '<ul class="bul">'+''.join(f'<li>{x}</li>' for x in items)+'</ul>'

SLIDES=[]
def slide(html, cls=""):
    SLIDES.append(f'<section class="slide {cls}">{html}</section>')

def header(tab, title, sub=""):
    s=f'<div class="shead"><div class="tab">{tab}</div><h2>{title}</h2>'
    if sub: s+=f'<p class="ssub">{sub}</p>'
    s+='</div>'
    return s

# 1. COVER
slide(f'''
<div class="cover" style="background-image:url('{IMG["cover"]}')">
  <div class="cov-inner">
    <div class="cov-badge">浙江工商大学 · 研究生院</div>
    <h1>研究生院督导系统<br><span class="cov-hl">建设成果汇报</span></h1>
    <div class="cov-line"></div>
    <p class="cov-sub">基于全校真实课表数据的研究生教学督导一体化平台</p>
    <div class="cov-meta">数据驱动 · 流程闭环 · 多角色协同</div>
  </div>
</div>''',"dark")

# 2. AGENDA
agenda=[("01","项目背景与目标","痛点与建设愿景","target"),
        ("02","系统概览 · 数据底座","真实数据一比一还原","book"),
        ("03","四类角色 · 权限体系","权限层层递进","users"),
        ("04","核心功能与评价体系","标准化督导评价","clipboard"),
        ("05","数据看板 · 业务闭环","看得见、管得住","chart"),
        ("06","建设成果与后续规划","成果小结与展望","rocket")]
cards=''.join(f'''<div class="ag-card"><div class="ag-no">{n}</div>
  <div class="ag-ic">{icon(ic)}</div>
  <div class="ag-tx"><h3>{t}</h3><p>{d}</p></div></div>''' for n,t,d,ic in agenda)
slide(header("目录","汇报内容","CONTENTS")+f'<div class="ag-grid">{cards}</div>')

# 3. BACKGROUND
pains=[("找课难","课程分散在多学院、两校区，含单双周，督导专家难快速定位目标课"),
       ("评价散","依赖纸质评价表，填写、收集、归档环节多，结果难沉淀"),
       ("统计弱","评价数据散落纸面，学院与研究生院缺乏全局视图"),
       ("反馈慢","评价结果向学院/研究生院传递链路长，难成质量改进闭环")]
pc=''.join(f'<div class="pain"><h4>{t}</h4><p>{d}</p></div>' for t,d in pains)
goal='''<div class="goalbox"><div class="goal-t">建设目标</div>
<div class="goal-c">打造一个 <b>数据驱动 · 流程闭环 · 多角色协同</b> 的研究生教学督导一体化平台，
把"全校总课表"变成 <b>可检索、可督导、可评价、可统计</b> 的在线平台。</div></div>'''
slide(header("01 项目背景","为什么要建这个系统","传统研究生教学督导面临四大痛点")+
      f'<div class="two-col"><div class="pain-grid">{pc}</div><div class="goal-wrap">{goal}</div></div>')

# 4. OVERVIEW + DATA
slide(header("02 系统概览","一个面向真实业务的督导平台",
      "课程、教师、学院、校区、排课规则全部来源于学校真实数据")+
      f'''<div class="quote">系统完全以学校《全校总课表》《角色信息表》《课程评价表》搭建，<b>所见即真实业务</b>，开箱即用。</div>
      <img class="bigimg" src="{IMG["data"]}" alt="数据底座">''')

# 5. ROLES
slide(header("03 角色与权限","四类角色 · 权限层层递进",
      "数据隔离 · 只读保护 · 逐级汇总，贴合研究生院真实管理结构")+
      f'<img class="bigimg tall" src="{IMG["role"]}" alt="角色权限">')

# 6. CORE FEATURES OVERVIEW
feats=[("filter","全校课程多维筛选","按周次/星期/学院/校区/教师组合筛选，与课表一致"),
       ("calendar","听课计划管理","待办 + 日历视图，课前自动站内提醒"),
       ("clipboard","标准化课程评价","复刻现行评价表，20 项定量 + 定性，支持草稿"),
       ("chart","数据看板与统计","关键指标一屏总览，图形化展示评价分布"),
       ("bell","消息通知与提醒","评价提交后自动通知学院与研究生院"),
       ("users","工号登录与用户管理","工号唯一凭证，可自助改密，角色管理")]
fc=''.join(f'''<div class="feat"><div class="feat-ic">{icon(ic)}</div>
  <h4>{t}</h4><p>{d}</p></div>''' for ic,t,d in feats)
slide(header("04 核心功能","六大核心功能模块","覆盖督导工作全流程")+f'<div class="feat-grid">{fc}</div>')

# 7. EVALUATION SYSTEM
slide(header("04 核心功能","标准化课程评价体系",
      "完全复刻学校现行《课程评价表》：20 项定量 + 定性，系统自动计算综合评分")+
      f'<img class="bigimg tall" src="{IMG["eval"]}" alt="评价体系">')

# 8. EVAL RECORD UI
slide(header("04 核心功能","评价记录与界面",
      "评价详情清晰呈现各维度得分、综合评分与星级")+
      f'''<div class="ui-row">
      <figure><img src="{IMG["rec"]}" alt="评价记录详情"><figcaption>课程评价记录详情页</figcaption></figure>
      <figure class="small"><img src="{IMG["item"]}" alt="评价表项"><figcaption>标准化评价表项（分级评分）</figcaption></figure>
      </div>''')

# 9. DASHBOARD + RADAR
slide(header("05 数据看板","研究生院主管工作台 · 数据可视化",
      "关键指标一屏总览（全校课程 / 已完成评价 / 督导专家 / 覆盖学院），评价结果多维度图形化")+
      f'''<div class="ui-row">
      <figure style="flex:1.5"><img src="{IMG["dash"]}" alt="仪表盘"><figcaption>研究生院主管数据看板（真实界面）</figcaption></figure>
      <figure style="flex:1"><img src="{IMG["radar"]}" alt="雷达图"><figcaption>课程评价多维度可视化（示例）</figcaption></figure>
      </div>''')

# 10. BUSINESS LOOP
slide(header("05 业务闭环","督导业务闭环",
      "从找课到改进，串成一条可沉淀、可统计、可追溯的数字化链路")+
      f'<img class="bigimg" src="{IMG["loop"]}" alt="业务闭环">')

# 11. ARCHITECTURE
slide(header("技术架构","系统架构（简要）",
      "前后端分离 · 数据驱动 · 真实课表自动解析建库")+
      f'<img class="bigimg tall" src="{IMG["arch"]}" alt="系统架构">')

# 12. ACHIEVEMENTS
ach=[("book","真实数据驱动","1,344 门课 · 22 学院 · 2 校区 · 595 教师 · 58 用户"),
     ("users","角色全覆盖","四类角色权限清晰，数据隔离到位"),
     ("target","流程全闭环","找课—听课—评价—统计—反馈一站打通"),
     ("clipboard","评价标准化","复刻现行评价表，定量+定性，支持草稿与算分"),
     ("shield","质量有保障","全部单元测试通过 · TypeScript 零类型错误"),
     ("layers","多端可用","电脑 / 平板 / 手机响应式适配")]
acc=''.join(f'<div class="ach"><div class="ach-ic">{icon(ic)}</div><div><h4>{t}</h4><p>{d}</p></div></div>' for ic,t,d in ach)
slide(header("06 建设成果","建设成果小结","六个维度，系统已具备真实可用能力")+f'<div class="ach-grid">{acc}</div>')

# 13. DEV APPROACH
slide(header("开发方式","AI 辅助 + 数据驱动的敏捷开发","让“真实数据 → 可用系统”更快、更贴合一线需求")+
      f'''<div class="dev-row">
      <div class="dev-step"><div class="dev-no">1</div><h4>真实数据自动建库</h4><p>直接以学校 Excel 课表为输入，自动解析建立业务数据库，省去大量人工录入与结构设计</p></div>
      <div class="dev-arr">{icon('check')}</div>
      <div class="dev-step"><div class="dev-no">2</div><h4>快速搭建可用系统</h4><p>四类角色、核心功能、商务蓝界面一次成型，前后端分离、PostgreSQL 稳定选型</p></div>
      <div class="dev-arr">{icon('check')}</div>
      <div class="dev-step"><div class="dev-no">3</div><h4>真实反馈快速迭代</h4><p>围绕督导专家与研究生院真实使用反馈多轮打磨，持续修复优化，贴合实际</p></div>
      </div>
      <div class="quote light">显著压缩了从需求到可用系统的周期，使平台快速进入真实业务可用状态。</div>''')

# 14. VALUE
val=[("users","督导专家","找课快、评价简、记录全；听课计划与提醒不漏听"),
     ("layers","学院","本院督导进度与评价质量一目了然"),
     ("chart","研究生院","全局数据看板，督导工作有数可依、有据可查"),
     ("rocket","学校","研究生教学质量保障工作的数字化升级")]
vc=''.join(f'<div class="val"><div class="val-ic">{icon(ic)}</div><h4>{t}</h4><p>{d}</p></div>' for ic,t,d in val)
slide(header("应用价值","为不同角色创造价值","一套系统，四方受益")+f'<div class="val-grid">{vc}</div>')

# 15. ROADMAP
road=[("角色扩展","增加分管院长等角色"),
      ("课程扩展","导入 MBA 等专业学位课程及评价表"),
      ("报表导出","一键导出 PDF / Excel 评价报告，便于学期末汇总"),
      ("智能增强","探索语音评价自动转写打分，降低填写成本"),
      ("分析升级","教师评价趋势、同学院对标分析等高级图表")]
rc=''.join(f'<div class="road"><div class="road-dot"></div><div class="road-tx"><h4>{t}</h4><p>{d}</p></div></div>' for t,d in road)
slide(header("06 后续规划","下一步规划","让平台持续生长，覆盖更广、用得更深")+f'<div class="road-list">{rc}</div>')

# 16. CLOSING
slide(f'''
<div class="cover closing" style="background-image:url('{IMG["cover"]}')">
  <div class="cov-inner center">
    <h1 class="thanks">谢 谢</h1>
    <div class="cov-line center"></div>
    <p class="cov-sub">浙江工商大学研究生院督导系统</p>
    <div class="cov-meta">数据驱动 · 流程闭环 · 多角色协同</div>
  </div>
</div>''',"dark")

# ---------- assemble ----------
N=len(SLIDES)
slides_html="\n".join(SLIDES)
HTML=f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>浙江工商大学研究生院督导系统 · 建设成果汇报</title>
<style>
:root{{--navy:#0E2A56;--navy2:#13315F;--blue:#2563EB;--blue2:#1E5BC6;--sky:#4A90E2;
--bg:#EEF3FB;--card:#fff;--text:#1F2A44;--gray:#5C6B82;--gold:#E8A23D;--line:#DCE6F4;--green:#2BA873;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{height:100%;background:#0a1830;font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB","Source Han Sans SC","Noto Sans CJK SC","WenQuanYi Zen Hei",sans-serif;color:var(--text)}}
#stage{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}}
.slide{{position:absolute;width:1280px;height:720px;background:var(--bg);overflow:hidden;
display:none;flex-direction:column;border-radius:8px;box-shadow:0 30px 80px rgba(0,0,0,.45)}}
.slide.active{{display:flex}}
.slide.dark{{background:var(--navy)}}
/* header */
.shead{{padding:48px 60px 0}}
.tab{{display:inline-block;background:linear-gradient(90deg,var(--blue),var(--sky));color:#fff;
font-size:16px;font-weight:bold;padding:6px 16px;border-radius:20px;letter-spacing:1px}}
.shead h2{{font-size:40px;color:var(--navy);margin-top:16px;font-weight:800;letter-spacing:.5px}}
.ssub{{color:var(--gray);font-size:19px;margin-top:8px}}
.shead::after{{content:"";display:block;width:64px;height:5px;border-radius:3px;
background:linear-gradient(90deg,var(--blue),var(--sky));margin-top:14px}}
.slide>:not(.shead):not(.cover){{margin:0 60px}}
.bigimg{{margin-top:22px!important;width:calc(100% - 120px);max-height:480px;object-fit:contain;align-self:center}}
.bigimg.tall{{max-height:520px}}
/* cover */
.cover{{width:100%;height:100%;background-size:cover;background-position:center;display:flex;align-items:center}}
.cov-inner{{padding:0 96px;max-width:980px}}
.cov-inner.center{{margin:0 auto;text-align:center}}
.cov-badge{{display:inline-block;border:1px solid rgba(255,255,255,.45);color:#cfe0ff;
font-size:18px;padding:7px 18px;border-radius:24px;letter-spacing:2px;margin-bottom:30px}}
.cover h1{{color:#fff;font-size:68px;line-height:1.18;font-weight:800;letter-spacing:1px}}
.cov-hl{{color:#7fb2ff}}
.cov-line{{width:90px;height:6px;border-radius:3px;background:var(--gold);margin:30px 0}}
.cov-line.center{{margin:30px auto}}
.cov-sub{{color:#dbe7fb;font-size:26px;font-weight:500}}
.cov-meta{{color:#8fb0e6;font-size:19px;margin-top:18px;letter-spacing:3px}}
.thanks{{font-size:96px;letter-spacing:18px}}
.closing .cov-sub{{margin-top:6px}}
/* agenda */
.ag-grid{{display:grid;grid-template-columns:1fr 1fr;gap:22px 28px;margin-top:36px!important}}
.ag-card{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px;
display:flex;align-items:center;gap:18px;box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.ag-no{{font-size:34px;font-weight:800;color:#cdd9ee;min-width:54px}}
.ag-ic{{width:50px;height:50px;border-radius:12px;background:linear-gradient(135deg,var(--blue),var(--sky));
display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.ag-ic svg{{width:26px;height:26px;color:#fff}}
.ag-tx h3{{font-size:23px;color:var(--navy);font-weight:700}}
.ag-tx p{{font-size:16px;color:var(--gray);margin-top:3px}}
/* background slide */
.two-col{{display:flex;gap:34px;margin-top:26px!important}}
.pain-grid{{flex:1.1;display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.pain{{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--blue);
border-radius:12px;padding:18px 20px;box-shadow:0 6px 18px rgba(14,42,86,.05)}}
.pain h4{{font-size:22px;color:var(--blue2);margin-bottom:6px}}
.pain p{{font-size:16px;color:var(--gray);line-height:1.5}}
.goal-wrap{{flex:.9;display:flex}}
.goalbox{{background:linear-gradient(135deg,var(--navy),#1c3e76);border-radius:18px;padding:34px 30px;
color:#fff;display:flex;flex-direction:column;justify-content:center}}
.goal-t{{font-size:24px;font-weight:800;color:var(--gold);margin-bottom:16px;letter-spacing:1px}}
.goal-c{{font-size:21px;line-height:1.7;color:#e8f0ff}}
.goal-c b{{color:#fff}}
.quote{{background:#E8F0FF;border-left:5px solid var(--blue);border-radius:10px;padding:16px 22px;
font-size:20px;color:var(--navy2);margin-top:18px!important;line-height:1.6}}
.quote b{{color:var(--blue2)}}
.quote.light{{background:#FFF7EA;border-color:var(--gold);margin-top:26px!important;text-align:center}}
/* features */
.feat-grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;margin-top:34px!important}}
.feat{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:26px 24px;
box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.feat-ic{{width:56px;height:56px;border-radius:14px;background:#EAF1FF;display:flex;align-items:center;
justify-content:center;margin-bottom:16px}}
.feat-ic svg{{width:30px;height:30px;color:var(--blue)}}
.feat h4{{font-size:23px;color:var(--navy);margin-bottom:8px}}
.feat p{{font-size:16px;color:var(--gray);line-height:1.55}}
/* image side */
.img-side{{display:flex;gap:26px;margin-top:20px!important;align-items:center}}
.img-side .grow{{flex:1.6;width:100%;max-height:430px;object-fit:contain}}
.img-side .side{{flex:1;text-align:center}}
.img-side .side img{{width:100%;max-height:380px;object-fit:contain}}
.cap{{font-size:15px;color:var(--gray);margin-top:6px}}
/* ui screenshots */
.ui-row{{display:flex;gap:26px;margin-top:24px!important;align-items:flex-start;justify-content:center}}
.ui-row figure{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;
box-shadow:0 12px 30px rgba(14,42,86,.10);flex:1}}
.ui-row figure.small{{flex:.66}}
.ui-row figure.wide{{flex:1;max-width:1000px}}
.ui-row img{{width:100%;border-radius:8px;display:block}}
.ui-row figcaption{{text-align:center;font-size:16px;color:var(--gray);margin-top:10px}}
/* achievements */
.ach-grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px 26px;margin-top:30px!important}}
.ach{{display:flex;gap:16px;align-items:center;background:var(--card);border:1px solid var(--line);
border-radius:14px;padding:18px 22px;box-shadow:0 6px 18px rgba(14,42,86,.05)}}
.ach-ic{{width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,var(--green),#37b98a);
display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.ach-ic svg{{width:26px;height:26px;color:#fff}}
.ach h4{{font-size:21px;color:var(--navy)}}
.ach p{{font-size:16px;color:var(--gray);margin-top:3px}}
/* dev */
.dev-row{{display:flex;align-items:stretch;gap:14px;margin-top:30px!important}}
.dev-step{{flex:1;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:26px 22px;
box-shadow:0 8px 22px rgba(14,42,86,.06);position:relative}}
.dev-no{{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--sky));
color:#fff;font-size:24px;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:14px}}
.dev-step h4{{font-size:22px;color:var(--navy);margin-bottom:8px}}
.dev-step p{{font-size:16px;color:var(--gray);line-height:1.55}}
.dev-arr{{display:flex;align-items:center;color:var(--green)}}
.dev-arr svg{{width:30px;height:30px}}
/* value */
.val-grid{{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:20px;margin-top:34px!important}}
.val{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:26px 18px;text-align:center;
box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.val-ic{{width:60px;height:60px;border-radius:50%;background:#EAF1FF;display:flex;align-items:center;
justify-content:center;margin:0 auto 14px}}
.val-ic svg{{width:30px;height:30px;color:var(--blue)}}
.val h4{{font-size:22px;color:var(--navy);margin-bottom:8px}}
.val p{{font-size:15px;color:var(--gray);line-height:1.5}}
/* roadmap */
.road-list{{margin-top:26px!important;display:flex;flex-direction:column;gap:14px}}
.road{{display:flex;align-items:center;gap:20px;background:var(--card);border:1px solid var(--line);
border-radius:12px;padding:16px 24px;box-shadow:0 5px 15px rgba(14,42,86,.05)}}
.road-dot{{width:14px;height:14px;border-radius:50%;background:var(--blue);flex:0 0 auto;
box-shadow:0 0 0 5px rgba(37,99,235,.15)}}
.road-tx{{display:flex;align-items:baseline;gap:18px}}
.road-tx h4{{font-size:22px;color:var(--navy);min-width:130px}}
.road-tx p{{font-size:17px;color:var(--gray)}}
.bul{{list-style:none;margin-top:14px}}
.bul li{{font-size:19px;color:var(--text);padding:8px 0 8px 28px;position:relative;line-height:1.5}}
.bul li::before{{content:"";position:absolute;left:4px;top:16px;width:9px;height:9px;border-radius:50%;background:var(--blue)}}
/* footer + nav */
.foot{{position:absolute;bottom:18px;left:60px;right:60px;display:flex;justify-content:space-between;
align-items:center;font-size:14px;color:#9fb0c8}}
.slide.dark .foot{{color:#5f7bab}}
.pbar{{position:absolute;top:0;left:0;height:4px;background:linear-gradient(90deg,var(--blue),var(--sky));transition:width .3s}}
.nav{{position:fixed;bottom:22px;right:26px;display:flex;gap:10px;z-index:10}}
.nav button{{width:44px;height:44px;border-radius:50%;border:none;background:rgba(255,255,255,.14);
color:#fff;font-size:20px;cursor:pointer;backdrop-filter:blur(6px)}}
.nav button:hover{{background:var(--blue)}}
.counter{{position:fixed;bottom:30px;left:26px;color:#cdd9ee;font-size:15px;z-index:10;letter-spacing:1px}}
.hint{{position:fixed;top:18px;right:24px;color:#7e93b5;font-size:13px;z-index:10}}
@media print{{.nav,.counter,.hint{{display:none}}}}
</style></head>
<body>
<div id="stage">{slides_html}</div>
<div class="counter"><span id="cur">1</span> / {N}</div>
<div class="nav"><button onclick="go(-1)">‹</button><button onclick="go(1)">›</button></div>
<div class="hint">← / → 翻页 · F 全屏</div>
<script>
var slides=document.querySelectorAll('.slide');var i=0;var N={N};
function fit(){{var s=Math.min(window.innerWidth/1280,window.innerHeight/720);
document.querySelectorAll('.slide').forEach(function(el){{el.style.transform='scale('+s+')';}});}}
function show(n){{i=Math.max(0,Math.min(N-1,n));
slides.forEach(function(el,k){{el.classList.toggle('active',k===i);
var existing=el.querySelector('.foot');if(!existing){{var f=document.createElement('div');f.className='foot';
f.innerHTML='<span>浙江工商大学研究生院督导系统 · 建设成果汇报</span><span>'+(k+1)+' / '+N+'</span>';
if(!el.classList.contains('dark')||true){{el.appendChild(f);}}
var p=document.createElement('div');p.className='pbar';el.appendChild(p);}}}});
document.getElementById('cur').textContent=i+1;
var pb=slides[i].querySelector('.pbar');if(pb)pb.style.width=((i+1)/N*100)+'%';fit();}}
function go(d){{show(i+d);}}
document.addEventListener('keydown',function(e){{
if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown')go(1);
else if(e.key==='ArrowLeft'||e.key==='PageUp')go(-1);
else if(e.key==='Home')show(0);else if(e.key==='End')show(N-1);
else if(e.key==='f'||e.key==='F'){{if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}}}});
window.addEventListener('resize',fit);
show(0);
</script>
</body></html>'''

os.makedirs(f"{ROOT}/slides",exist_ok=True)
with open(f"{ROOT}/slides/督导系统建设成果汇报.html","w",encoding="utf-8") as f:
    f.write(HTML)
print("wrote HTML deck:",N,"slides, size",round(len(HTML)/1024),"KB")
