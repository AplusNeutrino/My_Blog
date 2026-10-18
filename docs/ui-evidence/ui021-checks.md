# UI-021 — THINK Series 说明行尾与固定圆钮交叉

## 2026-10-19 精确production限定验收

- 验收head `dae7e3a50e48d982132943d724fe61cfb7c30e5f`，[run39152206991](https://github.com/AplusNeutrino/My_Blog/actions/runs/39152206991) build117747975591 success；工作分支deploy117752696942/live117752697291按规则skipped，不冒称部署。273 tests、T01保护、authoring44/5/7、production Jekyll、Search/Atom、SEO/旧URL/noindex、资源/集成、移动/无障碍及主192浏览器场景全部成功。
- 先记录本轮范围：只对精确head四宽度双主题Series可见目标图做验收并保存公开证据/更新本UI计划日志；不再改产品CSS/JS/门禁/旧内容与保护边界。main仍d1ddfe95，计划在本范围通过后以expected_sha非强推交付，新的main自身build/deploy/live与同场景复验仍待完成。
- 专项artifact12146575289（52318374 bytes）下载独立SHA256 `cb680a882b3acaa49c36ce3cac2e38c8ee2838b5428d8c9e76ec4a586eda3571` 匹配。原总包544089007 bytes超过接口上限，未下载，不绕过、不声称已看总包；专项保留原PNG/JSON无损来源。
- 实际查看56张Series可见帧、14联系表（390/768双主题各8帧、1024双主题各4帧、1366双主题各8帧）；放大390 Night/Light page1-4、768 Night page1-3、1366 Light page1-3四原PNG并重看失败before。390 Night原行末right326.640625，修复后首行right299.765625、末尾“列。”换到下一行left31/right57.890625；圆钮left315不变，完整文字可读且避让。768/1024自然换行、1366原布局保持，未发现本目标范围新缺陷。未用JSON或测试代替看图。
- 独立机械复核8流程32页303帧：44唯一href且每页12/12/12/8同顺序、末页同URL刷新/上一页、原生滚轮main连续覆盖/返回顶部通过；303原生PNG尺寸匹配、scrollX0、无页面横溢出；介绍/记录和目录Topic4/Series3/检索5非空根计数/文字Range严格无交叉、4select/1reset/分页原控件矩形与pointer hit全部通过。与手工范围分开记证。
- ui021-production保存14已看联系表、4放大原图及8源JSON哈希/目标文件名单摘要。其他247/303帧本head未人工看，完整A10及全站不通过；不累加旧head57/97/52帧冒称全页。无新用户决策，gh不在PATH未编造Issue。UI021仅production限定通过，部署及线上仍validation-pending。

## 2026-10-19 实施前记录

- Task UI-021 / P2；base 工作提交 `6220e714f1c932a3b4f89815a4f95d88dad1844e`，main `d1ddfe95f178c55b1fef67c86949c639c6f85cdd` 未变。只接续本轮 UI，不重做 T00–T39 或改写 COMPLETE。
- [精确审计 run39148513573](https://github.com/AplusNeutrino/My_Blog/actions/runs/39148513573)：build117737199765 在目录文字遮挡断言失败；272 tests、T01、authoring、production Jekyll 和前置门禁通过，不算完整成功；deploy117737568622/live117737569395 skipped。
- 专项 artifact12143773674，366116 bytes，下载独立 SHA256 `1237b6c05c5bce764609406bf9e7351aa84f4ac80ed89c49f7d47780408ffbe0` 匹配。实际查看 `think-pagination-directory-overlap-think-page-1-390-dark.png` 原图，Computer Architecture 卡片说明行尾进入圆钮所在区域；同一截图 JSON 显示字行 left31/right326.640625/top608.296875/bottom625.296875，圆钮 left315/right359/top583/bottom627，交叉宽11.640625、高17。视口390×701，clientWidth375，scrollY1575，Night，THINK第1页。图与几何分别记证；未实测此处点击失败，不称文字全部消失。
- S-A10b-01 从截图疑点升级为本项实际复现。此处是共用描述样式没有给固定圆钮预留空间；UI019/020已修范围不含Series说明。Topic/底部检索当前没有确认缺陷，不凭同类推测改其样式。
- 最小文件范围：`assets/css/neutriverse-sections.css` 仅 <=1199.98px、THINK内Series说明 padding-right；`tests/test_think_pagination_audit.py` 必要作用域回归；本文件/UI计划日志/公开原图JSON。已有目录逐行Range、UI019文字、UI020控件矩形/hit及真实滚轮分页刷新返回顶部全部保留，不放宽门禁。不得改正文/metadata/URL/hidden/noindex/private边界、产品JS、字体、按钮或外部仓库。
- 验收：精确新head所有回归/T01/authoring/production Jekyll与原门禁、四宽度双主题Series目标原图与严格无交叉、真实分页/刷新/返回顶部；部署后同场景复验才 done。未验证存 `ui/fix-021`，不合main；完整A10其余矩阵仍pending。
- `gh` 不在 PATH（本轮再次检查），遵守 gh-only 不用 API 创建Issue、不编造编号。无新用户决策。实现与修复后实测尚待执行。

## 实现与本机验证

- 仅上述Series说明加入2.75rem padding-right，断点/字号/按钮/脚本不变，Topic/检索不改。新增限定选择器/断点/唯一padding及禁止其他布局改动的回归；实际目录逐行Range门禁保持原样。
- 273 tests OK；authoring44posts/5fragments/7projects通过；T01全新输出对照保护44/5/5通过；git diff --check通过。首条baseline命令因缺--output报错，随后使用新路径运行成功；未改冻结基线。此环境没有Chrome/Jekyll，production真实图与交互待精确新head CI，不冒称修复后视觉通过。
- 新head保存在ui/fix-021；main未变。下一项查看精确CI和四宽度双主题Series目标原图，若后续发现其他相交表面另取证确认，不提前改样式或放宽断言。未完成部署/live，不标done。
