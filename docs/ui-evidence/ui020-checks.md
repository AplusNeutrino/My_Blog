# UI-020 — THINK筛选与页码触控区域被返回顶部按钮部分覆盖

状态：validation-pending；最小实现已完成，实际修复后截图/production/main/live待验。before只确认视觉覆盖，原位置指针拦截未实测，不把推测写成已失败点击。

## 2026-10-18 先记录范围与复现

- base main c6d7978ede998948740836eb87ce59fdd6e4ce18；[run39122169875](https://github.com/AplusNeutrino/My_Blog/actions/runs/39122169875) build117659800192/deploy117663901328/live117663968118全部success，267 tests/T01/authoring/Jekyll/原门禁通过。live专项artifact12135991011独立SHA256 8f143ff7681364e7e3d510f8d2038f649783f56ffa013cc6dd13449c05ec5342匹配。
- UI-A10a实际看390 Light四页56帧12联系表，放大page1-5与page3-13原图，确认固定返回顶部圆钮覆盖Order下拉框右端箭头区域，以及第3页数字4页码按钮右侧部分触控区域；文字4仍可见，不声称整按钮失效。用户报告无；是实际线上图，不是审美偏好。原UI019文字避让正常，不重开。
- P2根因：筛选表单与分页条没有固定按钮横向安全空间；旧文字Range只查介绍/记录，分页next/previous流程会自动滚动居中，不能捕获任意停留滚动位置的控件边缘覆盖。实际拦截需新增精确hit-test确认，现不编造点击结果。
- 最小拟改范围：assets/css/neutriverse-sections.css仅<=1199.98px为THINK筛选表单和分页容器留2.75rem按钮安全区，保持现有grid/标签/字号/排序/分页/URL语义；tools/check_think_build_visual.py四页每帧新增可见select/reset/pager矩形与可见返回顶部不相交、关键点elementFromPoint控件命中检查，失败先保存PNG/JSON再抛出；必要接线回归、UI计划日志与公开before证据。不改按钮/产品JS/正文/metadata/URL/hidden/noindex/同步数据/外部仓库/旧COMPLETE。
- 验收：精确修复head四宽度双主题四页控件避让、实际hit-test、真实分页/刷新/上一页/滚轮/返回顶部、新截图实际查看；T01/authoring/production Jekyll/旧门禁不减。未验收留ui/fix-020不合main，修复后production及main/live同场景另验。无新用户决策，gh不在PATH不编造Issue。

## 最小实现与本机结果

- 仅<=1199.98px给THINK表单padding-right:calc(1rem + 2.75rem)、分页padding-right:2.75rem；不更换grid/flex/换行规则、不动按钮/字号/产品JS。四页原生每帧检查4 select/1 reset与分页链接scope存在；仅对可见控件记录矩形，与可见返回顶部严格不交叉，并以elementFromPoint检查中心/四角内缩2px的实际命中。视口外和顶栏上方不假判可点；不点击以免改变筛选。失败先PNG/JSON再抛出，既有真实pager点击/刷新/上一页/顶部按钮和全部旧门禁保留。
- 加2项接线回归，本机269 tests OK、authoring44/5/7、T01保护44/5/5、diff通过；无本机Chrome/Jekyll，不声称修复后视觉/生产通过。未验收留ui/fix-020，main仍c6d7978e。UI019文字Range门禁保留，不放宽为截图通过。
- ui020-before/保存2实际放大原图与原始JSON、12已看联系表与8流程源JSON摘要/全部44href清单；本head人工56/302帧，其余246未看，不混入旧head52目标声称完整验收。下一项同一新head精确CI与修复后四宽度双主题目标截图。
