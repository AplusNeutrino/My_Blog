# UI-020 — THINK筛选与页码触控区域被返回顶部按钮部分覆盖

状态：validation-pending；最小实现已完成，实际修复后截图/production/main/live待验。before只确认视觉覆盖，原位置指针拦截未实测，不把推测写成已失败点击。

## 2026-10-18 先记录范围与复现

- base main c6d7978ede998948740836eb87ce59fdd6e4ce18；[run39122169875](https://github.com/AplusNeutrino/My_Blog/actions/runs/39122169875) build117659800192/deploy117663901328/live117663968118全部success，267 tests/T01/authoring/Jekyll/原门禁通过。live专项artifact12135991011独立SHA256 8f143ff7681364e7e3d510f8d2038f649783f56ffa013cc6dd13449c05ec5342匹配。
- UI-A10a实际看390 Light四页56帧12联系表，放大page1-5与page3-13原图，确认固定返回顶部圆钮覆盖Order下拉框右端箭头区域，以及第3页数字4页码按钮右侧部分触控区域；文字4仍可见，不声称整按钮失效。用户报告无；是实际线上图，不是审美偏好。原UI019文字避让正常，不重开。
- P2根因：筛选表单与分页条没有固定按钮横向安全空间；旧文字Range只查介绍/记录，分页next/previous流程会自动滚动居中，不能捕获任意停留滚动位置的控件边缘覆盖。实际拦截需新增精确hit-test确认，现不编造点击结果。
- 最小拟改范围：assets/css/neutriverse-sections.css仅<=1199.98px为THINK筛选表单和分页容器留2.75rem按钮安全区，保持现有grid/标签/字号/排序/分页/URL语义；tools/check_think_build_visual.py四页每帧新增可见select/reset/pager矩形与可见返回顶部不相交、关键点elementFromPoint控件命中检查，失败先保存PNG/JSON再抛出；必要接线回归、UI计划日志与公开before证据。不改按钮/产品JS/正文/metadata/URL/hidden/noindex/同步数据/外部仓库/旧COMPLETE。
- 验收：精确修复head四宽度双主题四页控件避让、实际hit-test、真实分页/刷新/上一页/滚轮/返回顶部、新截图实际查看；T01/authoring/production Jekyll/旧门禁不减。未验收留ui/fix-020不合main，修复后production及main/live同场景另验。无新用户决策，gh不在PATH不编造Issue。

## 最小实现与本机结果

### 2026-10-18 诊断确认及采样修正范围（先记录）

- base 351072c485131c515b54b9627bd99de1b9a05564；[run39130101572](https://github.com/AplusNeutrino/My_Blog/actions/runs/39130101572) build117683334367 failure，deploy117685602137/live117685602951 skipped。270 tests/T01/authoring/production Jekyll及前置检查通过，仍不是整构建通过。main保持c6d7978ede998948740836eb87ce59fdd6e4ce18。
- 专项artifact12137722054，20002706 bytes，独立SHA256 508869000b1197cf68cc2f34c958f897bd073e481b8eb8a9110843042c478bbf匹配。实际查看1024 Night失败原图并读原JSON：同一Series右下点命中父DIV.nv-writing-control，向左1px或向上1px即命中同一SELECT，向右/下1px仍命中父DIV；appearance:auto、borderRadius5.6px、pointerEvents:auto、transform:none。没有命中覆盖层，返回顶部与所有可见控件交集0。说明原5点把原生圆角边界处父容器误当拦截，并非UI020遮挡复发；不将CSS圆角公式等同Chrome原生控件实际hit轮廓。
- 最小范围仅审计脚本/必要回归/本UI计划日志与已看失败原PNG/JSON：原4个2px角点保留诊断，操作命中采样改为中心、四条直边中点内缩2px、按计算圆角+2px内缩的4个内部角点，共9个。每一可见有效点仍必须命中目标，整个控件矩形与返回顶部严格不交叉的门禁原样保留；不以父容器命中充当操作成功。故障注入验证9点任意拦截均失败、原角点圆钮覆盖即使未碰采样点也失败。原scope/文字Range/分页真实点击/刷新/上一页/滚轮/返回顶部和所有等待不减；产品CSS/JS不再改，真实新head生产与截图仍待验。gh不可用不编造Issue，无新用户问题。
- 本机实际271 tests OK（新增Node执行审计原JS的故障注入，不是另写等价算法）；9个操作点逐个被拦截均misses失败，1px圆钮仅覆盖旧角点但没碰任何操作点仍overlaps失败，圆角父容器命中保留原target/邻点诊断。authoring44/5/7、T01保护44/5/5、diff通过；无本机Chrome/Jekyll，新head生产/main/live继续pending。ui020-native-corner仅存本次实际看过的1张1024 Night原PNG及原始JSON，不裁切、不改像素，不扩大人工验收数量。

### 2026-10-18 精确失败核对与下一步范围（先记录）

- 分支实现/base 67f281e91b9b2e75fdb063fdcdd2749dde3baa5a；[run39126044604](https://github.com/AplusNeutrino/My_Blog/actions/runs/39126044604) build117671277541 failure，deploy117673410066/live117673410331 skipped。269 tests、T01、authoring、production Jekyll/SEO等前置检查通过，但不等于本次构建通过。
- 专项artifact12136740023（19956808 bytes）下载独立SHA256 95ab3cd27c718e9ee51a9b92b932a2a49f223e5e330ae10b995336f2a7695d83一致。实际放大查看3张原图：390 Light page1-5、page3-13与1024 Night失败图。前两张排序右箭头/页码4已与圆钮分离；分页现在下一行显示“下一页”，未裁切，但仅此两目标图，不是全矩阵验收。
- 失败条件：1024×757实际viewport、clientWidth1009、scrollY1146；Series rect left566.6875/right672.28125/top498.46875/bottom542.46875。五个探针只有右下(670.28125,540.46875)不命中；圆钮left914.5625/top655，与所有5个可见控件严格交集0。截图无可见遮挡，但不能仅凭截图证明该点可点，也不能认定圆角误报。当前JSON只留布尔值，实际命中元素/计算圆角/邻点尚缺，根因未确认。
- 最小下一步仅tools/check_think_build_visual.py失败诊断与必要回归、本计划日志及3张已看公开原图/原JSON；记录elementFromPoint实际元素、computed style（圆角/appearance/pointerEvents）、DPR与失败点周围1px命中。保持原5探针坐标、scope、所有require、矩形判定和等待完全不变；不靠更改内缩距离放行。产品CSS维持原候选，不再猜测修改；继续工作分支，不合main。gh仍不可用，不编造Issue；无新增用户决策。
- 诊断实现后本机270 tests、authoring44/5/7、T01保护44/5/5、diff通过；无本机Chrome/Jekyll。ui020-partial的3张原PNG及3原JSON均逐字复制artifact，未裁切重画；只人工查看这3帧，不冒称全部379文件或8流程完成。新诊断head production待验，失败原因和UI020保持validation-pending。

- 仅<=1199.98px给THINK表单padding-right:calc(1rem + 2.75rem)、分页padding-right:2.75rem；不更换grid/flex/换行规则、不动按钮/字号/产品JS。四页原生每帧检查4 select/1 reset与分页链接scope存在；仅对可见控件记录矩形，与可见返回顶部严格不交叉，并以elementFromPoint检查中心/四角内缩2px的实际命中。视口外和顶栏上方不假判可点；不点击以免改变筛选。失败先PNG/JSON再抛出，既有真实pager点击/刷新/上一页/顶部按钮和全部旧门禁保留。
- 加2项接线回归，本机269 tests OK、authoring44/5/7、T01保护44/5/5、diff通过；无本机Chrome/Jekyll，不声称修复后视觉/生产通过。未验收留ui/fix-020，main仍c6d7978e。UI019文字Range门禁保留，不放宽为截图通过。
- ui020-before/保存2实际放大原图与原始JSON、12已看联系表与8流程源JSON摘要/全部44href清单；本head人工56/302帧，其余246未看，不混入旧head52目标声称完整验收。下一项同一新head精确CI与修复后四宽度双主题目标截图。
