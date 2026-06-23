# -*- coding: utf-8 -*-
import base64, os
ROOT="/home/user/example-of-report"
A=f"{ROOT}/assets"
def b64(path):
    with open(path,"rb") as f:
        return "data:image/png;base64,"+base64.b64encode(f.read()).decode()
IMG={k:b64(f"{A}/{p}") for k,p in {
 "cover":"diagrams/cover-bg.png","data":"diagrams/data-foundation.png","role":"diagrams/role-matrix.png",
 "arch":"diagrams/architecture.png","eval":"diagrams/eval-system.png","loop":"diagrams/business-loop.png",
 "radar":"diagrams/chart-eval-radar.png","college":"diagrams/chart-college.png","scoredist":"diagrams/chart-scoredist.png",
 "dash":"screenshots/dashboard.png","rec":"screenshots/eval-record.png","item":"screenshots/eval-form-item.png",
}.items()}

def icon(name):
    P={"filter":'<polyline points="22 3 2 3 10 12.5 10 19 14 21 14 12.5 22 3"/>',
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
     "lock":'<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
     "image":'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><polyline points="21 15 16 10 5 21"/>',
     "help":'<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12" y2="17"/>'}
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg>'

N_TOTAL=23
SLIDES=[]
def slide(html, cls=""): SLIDES.append(f'<section class="slide {cls}">{html}</section>')
def header(tab,title,sub=""):
    s=f'<div class="shead"><div class="tab">{tab}</div><h2>{title}</h2>'
    if sub: s+=f'<p class="ssub">{sub}</p>'
    return s+'</div>'
def bullets(items):
    return '<ul class="bul">'+''.join(f'<li>{x}</li>' for x in items)+'</ul>'
def placeholder(label):
    return f'''<div class="ph">{icon("image")}<b>建议替换为真实截图</b><span>{label}</span></div>'''
def fdetail(tab,title,sub,bullet_items,right_html,n,note=""):
    extra=f'<p class="fnote">{note}</p>' if note else ""
    slide(header(tab,title,sub)+
      f'<div class="fdetail"><div class="ftext">{bullets(bullet_items)}{extra}</div>'
      f'<div class="fvis">{right_html}</div></div>')
def shotfig(img,cap):
    return f'<figure class="shotfig"><img src="{img}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'

# 1 COVER
slide(f'''<div class="cover" style="background-image:url('{IMG["cover"]}')"><div class="cov-inner">
  <div class="cov-lock"><div class="cov-mark">{icon("book")}</div>
    <div class="cov-org"><b>浙江工商大学 · 研究生院</b><span>ZHEJIANG GONGSHANG UNIVERSITY · GRADUATE SCHOOL</span></div></div>
  <h1>研究生院督导系统<br><span class="cov-hl">建设成果汇报</span></h1>
  <div class="cov-line"></div>
  <p class="cov-sub">基于全校真实课表数据的研究生教学督导一体化平台</p>
  <div class="cov-meta">数据驱动 · 流程闭环 · 多角色协同</div>
</div></div>''',"dark")

# 2 AGENDA
agenda=[("01","项目背景与目标","痛点与建设愿景","target"),("02","系统概览 · 数据底座","真实数据一比一还原","book"),
        ("03","四类角色 · 权限体系","权限层层递进","users"),("04","六大核心功能详解","逐项展开核心能力","clipboard"),
        ("05","业务闭环与系统架构","看得见、管得住","layers"),("06","成果 · 价值 · 规划","小结与展望","rocket"),
        ("07","答辩 Q&A","常见问题预演","help")]
cards=''.join(f'<div class="ag-card"><div class="ag-no">{n}</div><div class="ag-ic">{icon(ic)}</div>'
              f'<div class="ag-tx"><h3>{t}</h3><p>{d}</p></div></div>' for n,t,d,ic in agenda)
slide(header("目录","汇报内容","CONTENTS")+f'<div class="ag-grid ag7">{cards}</div>')

# 3 BACKGROUND
pains=[("找课难","课程分散在多学院、两校区，含单双周，难快速定位目标课"),
       ("评价散","依赖纸质评价表，填写、收集、归档环节多，结果难沉淀"),
       ("统计弱","评价数据散落纸面，学院与研究生院缺乏全局视图"),
       ("反馈慢","评价结果传递链路长，难成质量改进闭环")]
pc=''.join(f'<div class="pain"><h4>{t}</h4><p>{d}</p></div>' for t,d in pains)
goal='''<div class="goalbox"><div class="goal-t">建设目标</div><div class="goal-c">打造一个
<b>数据驱动 · 流程闭环 · 多角色协同</b> 的研究生教学督导一体化平台，把"全校总课表"变成
<b>可检索、可督导、可评价、可统计</b> 的在线平台。</div></div>'''
slide(header("01 项目背景","为什么要建这个系统","传统研究生教学督导面临四大痛点")+
      f'<div class="two-col"><div class="pain-grid">{pc}</div><div class="goal-wrap">{goal}</div></div>')

# 4 OVERVIEW + DATA
slide(header("02 系统概览","一个面向真实业务的督导平台","课程、教师、学院、校区、排课规则全部来源于学校真实数据")+
      f'''<div class="quote">系统完全以学校《全校总课表》《角色信息表》《课程评价表》搭建，<b>所见即真实业务</b>，开箱即用。</div>
      <img class="bigimg" src="{IMG["data"]}" alt="数据底座">''')

# 5 ROLES
slide(header("03 角色与权限","四类角色 · 权限层层递进","数据隔离 · 只读保护 · 逐级汇总，贴合研究生院真实管理结构")+
      f'<img class="bigimg tall" src="{IMG["role"]}" alt="角色权限">')

# 6 FEATURES OVERVIEW
feats=[("filter","全校课程多维筛选","按周次/星期/学院/校区/教师组合筛选"),
       ("calendar","听课计划管理","待办 + 日历视图，课前自动提醒"),
       ("clipboard","标准化课程评价","20 项定量 + 定性，支持草稿"),
       ("chart","数据看板与统计","关键指标总览，图形化展示"),
       ("bell","消息通知与提醒","评价提交后自动通知"),
       ("lock","工号登录与用户管理","工号唯一凭证，角色权限控制")]
fc=''.join(f'<div class="feat"><div class="feat-ic">{icon(ic)}</div><h4>{t}</h4><p>{d}</p></div>' for ic,t,d in feats)
slide(header("04 核心功能","六大核心功能模块","覆盖督导工作全流程，下面逐项展开")+f'<div class="feat-grid">{fc}</div>')

# 7 功能① 筛选
fdetail("04 核心功能 · 功能①","全校课程多维筛选","按多维度精确定位目标课程，与原始课表完全一致",
        ["全校 <b>1,344 门课程</b> 在线检索，告别翻纸质课表","支持 <b>周次 / 星期 / 学院 / 校区 / 教师</b> 多维组合筛选",
         "筛选逻辑与原课表一致（如“会计学院 + 第 3 周”精确联动）","督导专家可快速锁定“本周哪天、哪个学院、哪位老师”有课"],
        placeholder("全校课程 · 筛选页面"),7)

# 8 功能② 听课计划
fdetail("04 核心功能 · 功能②","听课计划 · 待办与日历视图","把有意向的课程一键纳入计划，按周直观安排",
        ["一键将课程加入 <b>听课计划</b>（类似待办清单）","<b>日历视图</b>：以“节次 × 星期”网格展示当周安排",
         "待听课 / 已评价 / 已取消 三种状态 <b>不同颜色区分</b>","课前自动 <b>站内提醒</b>，避免漏听"],
        placeholder("听课计划 · 日历视图"),8)

# 9 功能③ 评价体系
slide(header("04 核心功能 · 功能③","标准化课程评价体系","完全复刻学校现行《课程评价表》：20 项定量 + 定性，系统自动计算综合评分")+
      f'<img class="bigimg tall" src="{IMG["eval"]}" alt="评价体系">')

# 10 评价记录与界面（真实截图）
slide(header("04 核心功能 · 功能③","评价记录与界面","评价详情清晰呈现各维度得分、综合评分与星级")+
      f'''<div class="ui-row">
      <figure><img src="{IMG["rec"]}" alt="评价记录详情"><figcaption>课程评价记录详情页（真实界面）</figcaption></figure>
      <figure class="small"><img src="{IMG["item"]}" alt="评价表项"><figcaption>标准化评价表项（分级评分）</figcaption></figure></div>''')

# 11 功能④ 数据看板
slide(header("04 核心功能 · 功能④","研究生院主管工作台 · 数据可视化","关键指标一屏总览，评价结果多维度图形化呈现")+
      f'''<div class="ui-row">
      <figure style="flex:1.5"><img src="{IMG["dash"]}" alt="仪表盘"><figcaption>研究生院主管数据看板（真实界面）</figcaption></figure>
      <figure style="flex:1"><img src="{IMG["radar"]}" alt="雷达图"><figcaption>课程评价多维度可视化（示例）</figcaption></figure></div>''')

# 12 学院评价统计
slide(header("04 核心功能 · 功能④","学院评价统计分析","按学院展示督导评价次数与评分分布，支撑质量决策")+
      f'''<div class="ui-row">
      <figure style="flex:1.25"><img src="{IMG["college"]}" alt="各学院评价次数"></figure>
      <figure style="flex:1"><img src="{IMG["scoredist"]}" alt="评分分布"></figure></div>
      <p class="cap center">※ 上图为示例数据，接入真实评价数据后自动生成</p>''')

# 13 功能⑤ 通知
notify_flow='''<div class="nflow">
  <div class="nf-node nf-blue"><div class="nf-ic">✎</div><div><b>督导专家提交评价</b><span>完成课程评价</span></div></div>
  <div class="nf-arrow">▼</div>
  <div class="nf-node nf-sky"><div class="nf-ic">🔔</div><div><b>系统自动推送通知</b><span>无需人工传递</span></div></div>
  <div class="nf-arrow">▼</div>
  <div class="nf-split">
    <div class="nf-node nf-teal sm"><div><b>研究生院主管</b><span>全局知晓</span></div></div>
    <div class="nf-node nf-gold sm"><div><b>对应学院教学秘书</b><span>本院知晓</span></div></div>
  </div></div>'''
fdetail("04 核心功能 · 功能⑤","消息通知与提醒","打通“评价完成 → 学院/研究生院知晓”的反馈链路",
        ["评价提交后 <b>自动通知</b> 研究生院主管与对应学院教学秘书","听课计划 <b>课前自动站内提醒</b>，避免漏听",
         "通知可点击直达评价详情，<b>反馈即时</b>","让质量改进闭环 <b>真正跑起来</b>"],
        notify_flow,13)

# 14 功能⑥ 登录与用户管理
fdetail("04 核心功能 · 功能⑥","工号登录与用户管理","以工号为唯一凭证，角色权限清晰可控",
        ["全体用户以 <b>工号</b> 作为唯一登录凭证","初始密码即工号，支持 <b>首次登录后自助改密</b>",
         "基于角色的 <b>权限控制与数据隔离</b>（如学院秘书仅见本院）","研究生院主管可进行 <b>用户与角色管理</b>"],
        placeholder("工号登录页面"),14)

# 15 BUSINESS LOOP
slide(header("05 业务闭环","督导业务闭环","从找课到改进，串成一条可沉淀、可统计、可追溯的数字化链路")+
      f'<img class="bigimg" src="{IMG["loop"]}" alt="业务闭环">')

# 16 ARCHITECTURE
slide(header("05 技术架构","系统架构（简要）","前后端分离 · 数据驱动 · 真实课表自动解析建库")+
      f'<img class="bigimg tall" src="{IMG["arch"]}" alt="系统架构">')

# 17 ACHIEVEMENTS
ach=[("book","真实数据驱动","1,344 门课 · 22 学院 · 2 校区 · 595 教师 · 58 用户"),
     ("users","角色全覆盖","四类角色权限清晰，数据隔离到位"),("target","流程全闭环","找课—听课—评价—统计—反馈一站打通"),
     ("clipboard","评价标准化","复刻现行评价表，定量+定性，支持草稿与算分"),
     ("shield","质量有保障","全部单元测试通过 · TypeScript 零类型错误"),("layers","多端可用","电脑 / 平板 / 手机响应式适配")]
acc=''.join(f'<div class="ach"><div class="ach-ic">{icon(ic)}</div><div><h4>{t}</h4><p>{d}</p></div></div>' for ic,t,d in ach)
slide(header("06 建设成果","建设成果小结","六个维度，系统已具备真实可用能力")+f'<div class="ach-grid">{acc}</div>')

# 18 DEV
slide(header("06 开发方式","AI 辅助 + 数据驱动的敏捷开发","让“真实数据 → 可用系统”更快、更贴合一线需求")+
      f'''<div class="dev-row">
      <div class="dev-step"><div class="dev-no">1</div><h4>真实数据自动建库</h4><p>直接以学校 Excel 课表为输入，自动解析建立业务数据库，省去大量人工录入与结构设计</p></div>
      <div class="dev-arr">{icon('check')}</div>
      <div class="dev-step"><div class="dev-no">2</div><h4>快速搭建可用系统</h4><p>四类角色、核心功能、商务蓝界面一次成型，前后端分离、PostgreSQL 稳定选型</p></div>
      <div class="dev-arr">{icon('check')}</div>
      <div class="dev-step"><div class="dev-no">3</div><h4>真实反馈快速迭代</h4><p>围绕督导专家与研究生院真实使用反馈多轮打磨，持续修复优化，贴合实际</p></div></div>
      <div class="quote light">显著压缩了从需求到可用系统的周期，使平台快速进入真实业务可用状态。</div>''')

# 19 VALUE
val=[("users","督导专家","找课快、评价简、记录全；听课计划与提醒不漏听"),("layers","学院","本院督导进度与评价质量一目了然"),
     ("chart","研究生院","全局数据看板，督导工作有数可依、有据可查"),("rocket","学校","研究生教学质量保障工作的数字化升级")]
vc=''.join(f'<div class="val"><div class="val-ic">{icon(ic)}</div><h4>{t}</h4><p>{d}</p></div>' for ic,t,d in val)
slide(header("06 应用价值","为不同角色创造价值","一套系统，四方受益")+f'<div class="val-grid">{vc}</div>')

# 20 ROADMAP
road=[("角色扩展","增加分管院长等角色"),("课程扩展","导入 MBA 等专业学位课程及评价表"),
      ("报表导出","一键导出 PDF / Excel 评价报告，便于学期末汇总"),
      ("智能增强","探索语音评价自动转写打分，降低填写成本"),("分析升级","教师评价趋势、同学院对标分析等高级图表")]
rc=''.join(f'<div class="road"><div class="road-dot"></div><div class="road-tx"><h4>{t}</h4><p>{d}</p></div></div>' for t,d in road)
slide(header("06 后续规划","下一步规划","让平台持续生长，覆盖更广、用得更深")+f'<div class="road-list">{rc}</div>')

# 21-22 Q&A
def qa_page(tab,title,sub,items,n):
    cards=''.join(f'<div class="qa"><div class="q"><span class="qb">Q</span><span>{q}</span></div>'
                  f'<div class="a">{a}</div></div>' for q,a in items)
    slide(header(tab,title,sub)+f'<div class="qa-grid">{cards}</div>')
qa_page("07 答辩 Q&A","常见问题预演（一）","建设与数据",[
  ("数据来源是否可靠？如何保证与真实课表一致？","全部数据来源于学校《全校总课表》等真实文件，自动解析建库（1,344 门课、22 学院、595 名教师），筛选逻辑与原课表一致，可随新学期课表定期更新。"),
  ("评价数据安全吗？会不会被篡改？","工号唯一登录 + 角色权限控制；学院秘书对评价为只读、不可修改删除；数据存于 PostgreSQL，操作可追溯。"),
  ("评价标准如何统一？","评价表完全复刻学校现行《课程评价表》，20 项定量 + 定性，系统自动计算综合评分，口径一致、结果可比。"),
  ("能否与现有信息化系统对接？","前后端分离、以工号为唯一标识，预留数据导入与接口能力，可逐步与研究生管理等系统对接。"),
],21)
qa_page("07 答辩 Q&A","常见问题预演（二）","应用与推广",[
  ("老师上手难不难？","工号即账号、初始密码为工号；多维筛选快速找课，日历视图 + 课前提醒，评价支持保存草稿分次完成，上手成本低。"),
  ("研究生院如何掌握全校督导情况？","主管数据看板一屏总览（课程数、已完成评价、督导专家数、覆盖学院），并按学院图形化展示评价次数与评分分布。"),
  ("能否支持 MBA 等其他课程？","可扩展。后续计划导入 MBA 等专业学位课程及对应评价表。"),
  ("下一步规划是什么？","分管院长角色、PDF/Excel 报表导出、语音评价自动打分、教师评价趋势与同学院对标分析。"),
],22)

# 23 CLOSING
slide(f'''<div class="cover closing" style="background-image:url('{IMG["cover"]}')"><div class="cov-inner center">
  <h1 class="thanks">谢 谢</h1><div class="cov-line center"></div>
  <p class="cov-sub">浙江工商大学研究生院督导系统</p>
  <div class="cov-meta">数据驱动 · 流程闭环 · 多角色协同</div></div></div>''',"dark")

N=len(SLIDES)
slides_html="\n".join(SLIDES)
HTML=f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>浙江工商大学研究生院督导系统 · 建设成果汇报</title>
<style>
:root{{--navy:#0E2A56;--navy2:#13315F;--blue:#2563EB;--blue2:#1E5BC6;--sky:#4A90E2;
--bg:#EEF3FB;--card:#fff;--text:#1F2A44;--gray:#5C6B82;--gold:#E8A23D;--line:#DCE6F4;--green:#2BA873;}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{height:100%;background:#0a1830;font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB","Source Han Sans SC","Noto Sans CJK SC","WenQuanYi Zen Hei",sans-serif;color:var(--text)}}
#stage{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}}
.slide{{position:absolute;width:1280px;height:720px;background:var(--bg);overflow:hidden;display:none;flex-direction:column;border-radius:8px;box-shadow:0 30px 80px rgba(0,0,0,.45)}}
.slide.active{{display:flex}}
.slide.dark{{background:var(--navy)}}
.shead{{padding:42px 60px 0}}
.tab{{display:inline-block;background:linear-gradient(90deg,var(--blue),var(--sky));color:#fff;font-size:15px;font-weight:bold;padding:6px 16px;border-radius:20px;letter-spacing:1px}}
.shead h2{{font-size:38px;color:var(--navy);margin-top:14px;font-weight:800;letter-spacing:.5px}}
.ssub{{color:var(--gray);font-size:18px;margin-top:7px}}
.shead::after{{content:"";display:block;width:62px;height:5px;border-radius:3px;background:linear-gradient(90deg,var(--blue),var(--sky));margin-top:12px}}
.slide>:not(.shead):not(.cover){{margin:0 60px}}
.bigimg{{margin-top:18px!important;width:calc(100% - 120px);max-height:480px;object-fit:contain;align-self:center}}
.bigimg.tall{{max-height:500px}}
.cover{{width:100%;height:100%;background-size:cover;background-position:center;display:flex;align-items:center}}
.cov-inner{{padding:0 96px;max-width:1000px}} .cov-inner.center{{margin:0 auto;text-align:center}}
.cov-lock{{display:flex;align-items:center;gap:14px;margin-bottom:30px}}
.cov-mark{{width:54px;height:54px;border-radius:12px;border:1.5px solid rgba(255,255,255,.5);display:flex;align-items:center;justify-content:center}}
.cov-mark svg{{width:28px;height:28px;color:#cfe0ff}}
.cov-org b{{display:block;color:#eaf2ff;font-size:19px;letter-spacing:1px}}
.cov-org span{{display:block;color:#7e9bce;font-size:11px;letter-spacing:1.5px;margin-top:3px}}
.cover h1{{color:#fff;font-size:66px;line-height:1.18;font-weight:800;letter-spacing:1px}}
.cov-hl{{color:#7fb2ff}}
.cov-line{{width:90px;height:6px;border-radius:3px;background:var(--gold);margin:28px 0}} .cov-line.center{{margin:28px auto}}
.cov-sub{{color:#dbe7fb;font-size:25px;font-weight:500}}
.cov-meta{{color:#8fb0e6;font-size:18px;margin-top:16px;letter-spacing:3px}}
.thanks{{font-size:92px;letter-spacing:18px;color:#fff}}
.ag-grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px 26px;margin-top:30px!important}}
.ag-grid.ag7{{grid-template-columns:1fr 1fr;gap:14px 26px;margin-top:24px!important}}
.ag-card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 22px;display:flex;align-items:center;gap:16px;box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.ag-no{{font-size:30px;font-weight:800;color:#cdd9ee;min-width:48px}}
.ag-ic{{width:46px;height:46px;border-radius:11px;background:linear-gradient(135deg,var(--blue),var(--sky));display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.ag-ic svg{{width:24px;height:24px;color:#fff}}
.ag-tx h3{{font-size:21px;color:var(--navy);font-weight:700}} .ag-tx p{{font-size:14px;color:var(--gray);margin-top:2px}}
.two-col{{display:flex;gap:34px;margin-top:24px!important}}
.pain-grid{{flex:1.1;display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.pain{{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--blue);border-radius:12px;padding:18px 20px;box-shadow:0 6px 18px rgba(14,42,86,.05)}}
.pain h4{{font-size:22px;color:var(--blue2);margin-bottom:6px}} .pain p{{font-size:15px;color:var(--gray);line-height:1.5}}
.goal-wrap{{flex:.9;display:flex}}
.goalbox{{background:linear-gradient(135deg,var(--navy),#1c3e76);border-radius:18px;padding:34px 30px;color:#fff;display:flex;flex-direction:column;justify-content:center}}
.goal-t{{font-size:24px;font-weight:800;color:var(--gold);margin-bottom:16px;letter-spacing:1px}}
.goal-c{{font-size:20px;line-height:1.7;color:#e8f0ff}} .goal-c b{{color:#fff}}
.quote{{background:#E8F0FF;border-left:5px solid var(--blue);border-radius:10px;padding:16px 22px;font-size:19px;color:var(--navy2);margin-top:18px!important;line-height:1.6}}
.quote b{{color:var(--blue2)}}
.quote.light{{background:#FFF7EA;border-color:var(--gold);margin-top:24px!important;text-align:center}}
.feat-grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;margin-top:30px!important}}
.feat{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 22px;box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.feat-ic{{width:54px;height:54px;border-radius:14px;background:#EAF1FF;display:flex;align-items:center;justify-content:center;margin-bottom:14px}}
.feat-ic svg{{width:28px;height:28px;color:var(--blue)}}
.feat h4{{font-size:22px;color:var(--navy);margin-bottom:7px}} .feat p{{font-size:15px;color:var(--gray);line-height:1.5}}
.fdetail{{display:flex;gap:32px;margin-top:22px!important;height:438px}}
.ftext{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.fvis{{flex:1.25;display:flex}} .fvis>*{{width:100%}}
.fnote{{margin-top:16px;font-size:14px;color:#9aa8bd}}
.bul{{list-style:none}} .bul li{{font-size:19px;color:var(--text);padding:11px 0 11px 30px;position:relative;line-height:1.5}}
.bul li::before{{content:"";position:absolute;left:2px;top:19px;width:10px;height:10px;border-radius:50%;background:var(--blue)}}
.bul li b{{color:var(--blue2)}}
.ph{{border:2px dashed #B9CBE6;border-radius:16px;background:#F6F9FF;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#7E93B5;text-align:center;width:100%}}
.ph svg{{width:54px;height:54px;margin-bottom:14px;color:#9FB6D8}}
.ph b{{font-size:21px;color:#5C6B82}} .ph span{{font-size:15px;margin-top:6px;color:#8A98AD}}
.shotfig{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px;box-shadow:0 12px 30px rgba(14,42,86,.10);display:flex;flex-direction:column;width:100%}}
.shotfig img{{width:100%;border-radius:8px;object-fit:contain;flex:1;min-height:0}}
.shotfig figcaption{{text-align:center;color:var(--gray);font-size:15px;margin-top:10px}}
.ui-row{{display:flex;gap:26px;margin-top:22px!important;align-items:flex-start;justify-content:center}}
.ui-row figure{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;box-shadow:0 12px 30px rgba(14,42,86,.10);flex:1}}
.ui-row figure.small{{flex:.66}}
.ui-row img{{width:100%;border-radius:8px;display:block}}
.ui-row figcaption{{text-align:center;font-size:15px;color:var(--gray);margin-top:10px}}
.cap{{font-size:15px;color:var(--gray)}} .cap.center{{text-align:center;margin-top:10px!important}}
.nflow{{display:flex;flex-direction:column;align-items:center;justify-content:center;width:100%;gap:8px}}
.nf-node{{display:flex;align-items:center;gap:14px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 24px;box-shadow:0 8px 20px rgba(14,42,86,.07);min-width:340px}}
.nf-node b{{font-size:19px;color:var(--navy);display:block}} .nf-node span{{font-size:13px;color:var(--gray)}}
.nf-ic{{font-size:24px;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#EAF1FF}}
.nf-blue{{border-left:5px solid var(--blue)}} .nf-sky{{border-left:5px solid var(--sky)}}
.nf-teal{{border-left:5px solid #0E9F8E}} .nf-gold{{border-left:5px solid var(--gold)}}
.nf-arrow{{color:var(--sky);font-size:20px}}
.nf-split{{display:flex;gap:20px}} .nf-node.sm{{min-width:200px;padding:14px 20px}}
.ach-grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px 26px;margin-top:28px!important}}
.ach{{display:flex;gap:16px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px;box-shadow:0 6px 18px rgba(14,42,86,.05)}}
.ach-ic{{width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,var(--green),#37b98a);display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.ach-ic svg{{width:26px;height:26px;color:#fff}}
.ach h4{{font-size:21px;color:var(--navy)}} .ach p{{font-size:15px;color:var(--gray);margin-top:3px}}
.dev-row{{display:flex;align-items:stretch;gap:14px;margin-top:28px!important}}
.dev-step{{flex:1;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px 22px;box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.dev-no{{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--sky));color:#fff;font-size:22px;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:13px}}
.dev-step h4{{font-size:21px;color:var(--navy);margin-bottom:8px}} .dev-step p{{font-size:15px;color:var(--gray);line-height:1.55}}
.dev-arr{{display:flex;align-items:center;color:var(--green)}} .dev-arr svg{{width:28px;height:28px}}
.val-grid{{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:20px;margin-top:30px!important}}
.val{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:26px 18px;text-align:center;box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.val-ic{{width:58px;height:58px;border-radius:50%;background:#EAF1FF;display:flex;align-items:center;justify-content:center;margin:0 auto 14px}}
.val-ic svg{{width:28px;height:28px;color:var(--blue)}}
.val h4{{font-size:21px;color:var(--navy);margin-bottom:8px}} .val p{{font-size:14px;color:var(--gray);line-height:1.5}}
.road-list{{margin-top:22px!important;display:flex;flex-direction:column;gap:13px}}
.road{{display:flex;align-items:center;gap:20px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px 24px;box-shadow:0 5px 15px rgba(14,42,86,.05)}}
.road-dot{{width:14px;height:14px;border-radius:50%;background:var(--blue);flex:0 0 auto;box-shadow:0 0 0 5px rgba(37,99,235,.15)}}
.road-tx{{display:flex;align-items:baseline;gap:18px}}
.road-tx h4{{font-size:21px;color:var(--navy);min-width:130px}} .road-tx p{{font-size:16px;color:var(--gray)}}
.qa-grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px 24px;margin-top:26px!important}}
.qa{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 24px;box-shadow:0 8px 22px rgba(14,42,86,.06)}}
.qa .q{{display:flex;gap:12px;align-items:flex-start;font-size:18px;color:var(--navy);font-weight:700;line-height:1.4}}
.qa .qb{{background:var(--blue);color:#fff;width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:15px;flex:0 0 auto;font-weight:800}}
.qa .a{{font-size:15px;color:var(--gray);margin-top:11px;line-height:1.55;padding-left:40px}}
.foot{{position:absolute;bottom:18px;left:60px;right:60px;display:flex;justify-content:space-between;align-items:center;font-size:14px;color:#9fb0c8}}
.slide.dark .foot{{color:#5f7bab}}
.pbar{{position:absolute;top:0;left:0;height:4px;background:linear-gradient(90deg,var(--blue),var(--sky));transition:width .3s}}
.nav{{position:fixed;bottom:22px;right:26px;display:flex;gap:10px;z-index:10}}
.nav button{{width:44px;height:44px;border-radius:50%;border:none;background:rgba(255,255,255,.14);color:#fff;font-size:20px;cursor:pointer;backdrop-filter:blur(6px)}}
.nav button:hover{{background:var(--blue)}}
.counter{{position:fixed;bottom:30px;left:26px;color:#cdd9ee;font-size:15px;z-index:10;letter-spacing:1px}}
.hint{{position:fixed;top:18px;right:24px;color:#7e93b5;font-size:13px;z-index:10}}
@media print{{.nav,.counter,.hint{{display:none}}}}
</style></head><body>
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
if(!el.querySelector('.foot')){{var f=document.createElement('div');f.className='foot';
f.innerHTML='<span>浙江工商大学研究生院督导系统 · 建设成果汇报</span><span>'+(k+1)+' / '+N+'</span>';el.appendChild(f);
var p=document.createElement('div');p.className='pbar';el.appendChild(p);}}}});
document.getElementById('cur').textContent=i+1;
var pb=slides[i].querySelector('.pbar');if(pb)pb.style.width=((i+1)/N*100)+'%';fit();}}
function go(d){{show(i+d);}}
document.addEventListener('keydown',function(e){{
if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown')go(1);
else if(e.key==='ArrowLeft'||e.key==='PageUp')go(-1);
else if(e.key==='Home')show(0);else if(e.key==='End')show(N-1);
else if(e.key==='f'||e.key==='F'){{if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}}}});
window.addEventListener('resize',fit);show(0);
</script></body></html>'''
os.makedirs(f"{ROOT}/slides",exist_ok=True)
with open(f"{ROOT}/slides/督导系统建设成果汇报.html","w",encoding="utf-8") as f: f.write(HTML)
print("wrote HTML deck:",N,"slides, size",round(len(HTML)/1024),"KB")
