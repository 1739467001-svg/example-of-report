# -*- coding: utf-8 -*-
import cairosvg, os, math
OUT = "/home/user/example-of-report/assets/diagrams"
os.makedirs(OUT, exist_ok=True)

FONT = "WenQuanYi Zen Hei"
# Palette
NAVY="#0E2A56"; NAVY2="#13315F"; BLUE="#2563EB"; BLUE2="#1E5BC6"
SKY="#4A90E2"; SKY2="#5AA9F0"; CYAN="#1FA2B8"; TEAL="#0E9F8E"
BG1="#F2F7FF"; BG2="#E7EFFC"; CARD="#FFFFFF"; GOLD="#E8A23D"; GREEN="#2BA873"
TEXT="#1F2A44"; GRAY="#5C6B82"; LINE="#D8E2F0"; SHADOW="rgba(14,42,86,0.10)"

def render(svg, name, w, h, scale=2):
    full = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">{svg}</svg>'
    cairosvg.svg2png(bytestring=full.encode("utf-8"), write_to=f"{OUT}/{name}.png",
                     output_width=int(w*scale), output_height=int(h*scale))
    print("wrote", name)

def compose(body,name,W,DY,finalH,scale=2):
    # draw bg at final size, shift content up by DY (removes the old title gap)
    s=bg(W,finalH)+f'<g transform="translate(0,{-DY})">{body}</g>'
    render(s,name,W,finalH,scale)

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def text(x,y,s,size,fill=TEXT,anchor="middle",weight="normal",ls=None):
    extra = f' letter-spacing="{ls}"' if ls else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{extra}>{esc(s)}</text>'

def rrect(x,y,w,h,r,fill,stroke="none",sw=0,opacity=1):
    so = f' stroke="{stroke}" stroke-width="{sw}"' if stroke!="none" else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" fill="{fill}"{so} opacity="{opacity}"/>'

def card(x,y,w,h,r=18,fill=CARD,accent=None):
    s = rrect(x+3,y+5,w,h,r,"#0E2A56",opacity=0.08)  # soft shadow
    s += rrect(x,y,w,h,r,fill,stroke=LINE,sw=1)
    if accent:
        s += rrect(x,y,w,8,r,accent) + rrect(x,y+4,w,4,0,accent)
    return s

def grad(id_, c1, c2, x1=0,y1=0,x2=0,y2=1):
    return f'<linearGradient id="{id_}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'

def bg(w,h):
    return f'<defs>{grad("bg",BG1,BG2)}</defs>' + rrect(0,0,w,h,0,"url(#bg)")

def arrow(x1,y1,x2,y2,color=SKY,wd=4):
    ang=math.atan2(y2-y1,x2-x1); L=12
    ax=x2-L*math.cos(ang); ay=y2-L*math.sin(ang)
    p1=(x2,y2); p2=(ax-7*math.sin(ang), ay+7*math.cos(ang)); p3=(ax+7*math.sin(ang), ay-7*math.cos(ang))
    return (f'<line x1="{x1}" y1="{y1}" x2="{ax}" y2="{ay}" stroke="{color}" stroke-width="{wd}" stroke-linecap="round"/>'
            f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="{color}"/>')

# ---------------- Diagram 1: Data Foundation ----------------
def data_foundation():
    W=1600; s=""
    cards=[("1,431","门研究生课程",BLUE),("22","个学院",SKY),("2","个校区",CYAN),
           ("588","名授课教师",TEAL),("58","位系统用户",GOLD),("单双周","完整排课规则",GREEN)]
    n=len(cards); m=60; gap=30; cw=(W-2*m-(n-1)*gap)/n; cy=200; ch=250
    for i,(num,lab,acc) in enumerate(cards):
        x=m+i*(cw+gap)
        s+=card(x,cy,cw,ch,accent=acc)
        fs = 64 if len(num)<=5 else 44
        s+=text(x+cw/2,cy+135,num,fs,NAVY,weight="bold")
        s+=text(x+cw/2,cy+190,lab,23,GRAY)
    compose(s,"data-foundation",W,DY=160,finalH=320)

# ---------------- Diagram 2: Business Loop ----------------
def business_loop():
    W=1600; s=""
    steps=[("1","全校课表","多维筛选课程",BLUE),
           ("2","加入听课计划","待办 + 日历视图",SKY),
           ("3","课堂听课","课前自动提醒",CYAN),
           ("4","在线评价","标准化评价表",TEAL),
           ("5","自动通知","学院 / 研究生院",GOLD),
           ("6","数据统计分析","看板 · 趋势 · 分布",GREEN)]
    n=len(steps); m=70; gap=46; cw=(W-2*m-(n-1)*gap)/n; cy=200; ch=150
    centers=[]
    for i,(idx,t1,t2,acc) in enumerate(steps):
        x=m+i*(cw+gap)
        s+=card(x,cy,cw,ch,r=16,accent=acc)
        s+=f'<circle cx="{x+34}" cy="{cy+38}" r="20" fill="{acc}"/>'+text(x+34,cy+46,idx,22,"#fff",weight="bold")
        s+=text(x+cw/2+12,cy+92,t1,25,NAVY,weight="bold")
        s+=text(x+cw/2,cy+128,t2,19,GRAY)
        centers.append((x,x+cw,cy+ch/2))
        if i>0:
            px=centers[i-1][1]; 
            s+=arrow(px+8,cy+ch/2,x-8,cy+ch/2,SKY2,5)
    # return loop
    x1=centers[-1][0]+cw/2; x0=centers[0][0]+cw/2; ybot=cy+ch+120
    path=f'M {x1} {cy+ch} C {x1} {ybot+40}, {x0} {ybot+40}, {x0} {cy+ch+12}'
    s+=f'<path d="{path}" fill="none" stroke="{GOLD}" stroke-width="5" stroke-dasharray="2 0"/>'
    s+=arrow(x0, cy+ch+34, x0, cy+ch+10, GOLD,5)
    s+=rrect(W/2-160,ybot+12,320,52,26,"#FFF7EA",stroke=GOLD,sw=2)
    s+=text(W/2,ybot+46,"持续改进 · 质量闭环",26,GOLD,weight="bold")
    compose(s,"business-loop",W,DY=150,finalH=410)

# ---------------- Diagram 3: Role Matrix ----------------
def role_matrix():
    W=1600; s=""
    roles=[("督导专家","权限范围：全校课程",SKY,
            ["检索 / 筛选全校课程","加入听课计划并听课","填写标准化课程评价","查看本人评价记录"]),
           ("督导组长","权限范围：全校课程",BLUE,
            ["督导专家全部功能","查看全部专家的评价","掌握督导整体情况"]),
           ("学院教学秘书","权限范围：本学院",TEAL,
            ["查看本院被督导课程","查看评价详情（只读）","掌握本院督导进度","不可修改 / 删除"]),
           ("研究生院主管","权限范围：全研究生院",NAVY,
            ["全局统计数据看板","各学院督导总览","用户与角色管理","最高管理权限"])]
    n=4; m=56; gap=28; cw=(W-2*m-(n-1)*gap)/n; cy=170; ch=440
    for i,(name,scope,acc,caps) in enumerate(roles):
        x=m+i*(cw+gap)
        s+=card(x,cy,cw,ch,r=18)
        s+=rrect(x,cy,cw,84,18,acc)+rrect(x,cy+40,cw,44,0,acc)
        s+=text(x+cw/2,cy+54,name,28,"#fff",weight="bold")
        s+=rrect(x+24,cy+108,cw-48,42,21,"#EEF4FF")
        s+=text(x+cw/2,cy+135,scope,19,acc,weight="bold")
        yy=cy+196
        for c in caps:
            s+=f'<circle cx="{x+34}" cy="{yy-6}" r="5" fill="{acc}"/>'
            s+=text(x+50,yy,c,20,TEXT,anchor="start")
            yy+=48
        # level dots
        lvl=i+1
        for d in range(4):
            col=acc if d<lvl else "#E2E8F2"
            s+=f'<circle cx="{x+cw-90+d*20}" cy="{cy+ch-34}" r="7" fill="{col}"/>'
        s+=text(x+28,cy+ch-28,"权限等级",16,GRAY,anchor="start")
    compose(s,"role-matrix",W,DY=120,finalH=510)

# ---------------- Diagram 4: Architecture ----------------
def architecture():
    W=1500; s=""
    def layer(y,h,title,acc,items,fill="#FFFFFF"):
        out=card(120,y,W-240,h,r=16,fill=fill)
        out+=rrect(120,y,12,h,6,acc)
        out+=text(150,y+38,title,24,acc,anchor="start",weight="bold")
        iw=(W-300-(len(items)-1)*18)/len(items)
        for i,it in enumerate(items):
            ix=170+i*(iw+18)
            out+=rrect(ix,y+56,iw,h-80,12,"#EEF4FF",stroke=LINE,sw=1)
            out+=text(ix+iw/2,y+56+(h-80)/2+8,it,20,TEXT)
        return out
    y=150; gap=30
    s+=layer(y,140,"用户层（多端：电脑 · 平板 · 手机）",BLUE,["督导专家","督导组长","学院教学秘书","研究生院主管"]); 
    ym=y+140
    s+=arrow(W/2,ym,W/2,ym+gap,SKY2,5); y=ym+gap
    s+=layer(y,140,"前端应用层  ·  TypeScript / Material Design 3 / 商务蓝响应式",SKY,["课程检索","听课计划","评价表单","数据看板"])
    ym=y+140; s+=arrow(W/2,ym,W/2,ym+gap,SKY2,5); y=ym+gap
    s+=layer(y,150,"后端服务层  ·  前后端分离 API",TEAL,["认证授权","课程服务","听课计划","评价服务","通知服务","统计分析"])
    ym=y+150; s+=arrow(W/2,ym,W/2,ym+gap,SKY2,5); y=ym+gap
    s+=layer(y,140,"数据层  ·  PostgreSQL 关系型数据库",NAVY,["课程","教师","用户与角色","评价记录","消息通知"])
    ym=y+140; s+=arrow(W/2,ym,W/2,ym+gap,GOLD,5); y=ym+gap
    s+=layer(y,128,"数据来源  ·  自动解析建库",GOLD,["全校总课表.xls","角色信息表.xlsx","课程评价表"],fill="#FFFBF2")
    compose(s,"architecture",W,DY=100,finalH=890)

# ---------------- Diagram 5: Evaluation System ----------------
def eval_system():
    W=1500; s=""
    # root (left center)
    rx,ry,rw,rh=80,330,250,130
    s+=card(rx,ry,rw,rh,r=18,fill=NAVY)
    s+=text(rx+rw/2,ry+60,"课程评价表",27,"#fff",weight="bold")
    s+=text(rx+rw/2,ry+98,"标准化在线表单",18,"#CBD9F2")
    # 2x2 branch grid
    branches=[("定量评分（20 项）",BLUE,["教学内容 · 学生状态 · 课程内容","教学过程 · 教学方法 等多维度"]),
              ("定性文字评价",TEAL,["课程亮点","具体建议"]),
              ("综合评分",GOLD,["总体评分（如 4.9 / 5.0）","星级直观呈现"]),
              ("评价状态",GREEN,["保存草稿（可分次完成）","提交（必填项校验）"])]
    cols=[460,980]; rows=[170,400]; bw=460; bh=200
    for i,(title,acc,subs) in enumerate(branches):
        bx=cols[i%2]; by=rows[i//2]
        s+=arrow(rx+rw, ry+rh/2, bx-12, by+bh/2, acc,4)
        s+=card(bx,by,bw,bh,r=14)
        s+=rrect(bx,by,bw,56,14,acc)+rrect(bx,by+28,bw,28,0,acc)
        s+=text(bx+bw/2,by+37,title,23,"#fff",weight="bold")
        yy=by+108
        for sub in subs:
            s+=f'<circle cx="{bx+34}" cy="{yy-6}" r="5" fill="{acc}"/>'
            s+=text(bx+50,yy,sub,20,TEXT,anchor="start")
            yy+=46
    # features strip
    fy=662
    feats=["互斥单选项设计","保存草稿继续评价","系统自动计算综合评分","评价提交即自动通知"]
    fw=(W-160-(len(feats)-1)*20)/len(feats)
    for i,f in enumerate(feats):
        fx=80+i*(fw+20)
        s+=rrect(fx,fy,fw,62,31,"#EAF1FF",stroke=SKY,sw=1)
        s+=text(fx+fw/2,fy+39,f,20,BLUE2,weight="bold")
    compose(s,"eval-system",W,DY=120,finalH=620)

# ---------------- Cover background ----------------
def cover_bg():
    W,H=1600,900
    s=f'<defs>{grad("cv",NAVY,"#091B3A")}{grad("cv2","#1B3D7A","#0B2347")}</defs>'
    s+=rrect(0,0,W,H,0,"url(#cv)")
    # subtle dot grid
    dots=""
    for yy in range(60,H,54):
        for xx in range(60,W,54):
            dots+=f'<circle cx="{xx}" cy="{yy}" r="1.6" fill="#5A86C8" opacity="0.16"/>'
    s+=dots
    # abstract arcs
    s+=f'<circle cx="{W-180}" cy="{H-120}" r="320" fill="none" stroke="#3D6FBE" stroke-width="2" opacity="0.25"/>'
    s+=f'<circle cx="{W-180}" cy="{H-120}" r="210" fill="none" stroke="#4A90E2" stroke-width="2" opacity="0.3"/>'
    s+=f'<circle cx="160" cy="160" r="180" fill="none" stroke="#3D6FBE" stroke-width="2" opacity="0.18"/>'
    render(s,"cover-bg",W,H)

data_foundation(); business_loop(); role_matrix(); architecture(); eval_system(); cover_bg()
print("ALL SVG DIAGRAMS DONE")
