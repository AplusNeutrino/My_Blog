# UI-013 — 首页精选卡片正文避让固定按钮

状态：in-progress，生产截图/main/live尚未验收。

## 先记录范围（2026-10-17）

- base：main53787e0bbe111da193918ee959e82780b58d87c3；实现基于78d01a325da82cd12e5005667cb51641d76f913b（包含d91修复及上一轮真实失败记录），工作分支ui/audit-009当前d91bd7217515eb3edfad65951b7e958af2182218。原工作区修改不动。
- 实际复现而非用户报告/推测/偏好：[768 Night原生第5帧](ui013-before-home-768-dark.png)，精选内容右下Progressive Disclosure卡片摘要右端被返回顶部圆钮遮挡。来自run39008835671 attempt1的artifact12092431014；其他尺寸/主题不提前宣称已复现。
- 文件范围：assets/css/neutriverse-sections.css、tools/check_think_build_visual.py、tests/test_public_page_sweep_audit.py、本轮计划/日志和ui013/uia09证据。拟仅无右侧辅助栏时给精选网格最右列文字留出按钮横向区域；单列时该列就是所有卡片。保持卡片外框/列数/主题/字号、共享按钮和DOM不动；不修改数据/正文/metadata/旧URL/hidden/noindex、外部仓库或旧COMPLETE。
- 回归：保留近期表达逐行Range/按钮无交集门禁；同样严格检查精选卡片全部真实文本行，失败保存PNG/JSON并抛错。四宽度双主题原生滚轮全页截图，实际看原遮挡场景、中文长标题/摘要/列对齐，真实返回顶部与公开入口往返；原192+14/所有专项不减。
- UI-A09另有同head重试再次在1366 Night THINK的document.fonts.ready脚本超时；本轮仅增加失败时字体状态/FontFace/资源时序诊断，保留原等待与失败，不据此推断网站字体损坏或绕过门禁。
- 必须local回归/T01/authoring、精确新head production Jekyll/产物/完整浏览器截图通过才可交付main，随后核对新main自身build/deploy/live。未验证留工作分支。gh未安装不编造Issue，无新用户决策。

## 实现与真实验证边界

- 2026-10-17接续：精确563d054f/run39015972699 build117348035702 failure、deploy117349896137/live117349895961 skipped；250 tests/4 Ruby/T01/authoring/Jekyll等通过，主144、新public18、139帧、侧栏0。实际看[768 Night原第5帧修复后](ui013-production-partial-home-768-dark.png)，正文已避开按钮，390 Night近期第4帧旧场景也正常；只属部分生产验证，未验收全部139图或1366/main/live。字体诊断3个Noto Sans SC400/500/600仍loading，另补请求诊断详见uia09-font-wait-checks.md，原门禁不变。

- 真实实现提交eba88e0fcb3b3c2fbd5d0e2a55529fe21b1cd379，7个上传blob均与本地git hash-object一致；随后只追加SHA检查点。最终分支head精确CI须独立核对，当前未交付main。

- 根因：精选卡片padding1rem，两列网格的最右列文字进入固定44px按钮区域；与UI-012近期表达不同选择器。768–1199.98px仅:nth-child(2n)卡片增加2.75rem右内边距；<=767.98px单列全部卡片同样避让；>=1200px保持原辅助栏布局。边框/列数/字号/DOM/数据/按钮未改。
- 原recentTextButton诊断字段为兼容保留，但TreeWalker选择器扩展至近期表达+精选卡片全部文本；新增surface标记，仍严格拒绝真实行矩形与可见按钮相交，失败PNG/JSON和重抛不减。新接线回归约束两列只改外列、单列避让及失败字体诊断不改变settle。
- 本机250 tests、authoring44/5/7、T01保护44/5/5、diff check通过；初次新增测试有两个定位断言错误，已修正定位范围后重跑全套通过，不删除旧门禁。没有本机Ruby/Jekyll/Chrome，不把静态测试当视觉验收。修复后四宽度双主题production截图、24流程/192+14、main/live仍validation-pending。
- UI-A09 attempt2失败：run39008835671 build117337553687 failure，deploy117339610923/live117339611045 skipped。artifact12093428361 /331496554 bytes /sha256:022d4f9e84169d80fe447afac180acb12dc7e9b64f4c05404b63780e20f46aab独立匹配；144主场景、18新流程、139滚动帧、侧栏0。实际查看本次scene-failure.png，1366 Night THINK内容可见，仍不放行；没有人工验收全部139图。再次字体ready脚本超时约30秒，本次只补fontSetStatus/逐FontFace状态/字体资源时序，再次失败原样重抛，根因仍待诊断。
