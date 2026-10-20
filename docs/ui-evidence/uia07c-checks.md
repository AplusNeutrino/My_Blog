# UI-A07c 阅读目录控件检查

## 2026-10-20 范围先记

- 实际 main `b084b8a1f7818a1b9d2e1935456308ad9e6ff22e`；审计父 `dcb1aace27726a12779884fa498105b824978e3a`。main 用户 Library 同步保留；Q-UI-01 无答复，不执行受阻 Atlas 门禁。
- 最小独立任务 UI-A07c：代表公开长文章的目录链接、滚动定位、返回顶部与双主题；不重复已 done 的媒体/复制专项。优先发现遮挡/消失/菜单故障，不凭偏好改样式。
- 拟写文件仅本记录、NEUTRIVERSE_UI_FIX_PLAN.md、docs/neutriverse-ui-fix-log.md 及公开截图/来源；如确认缺陷，另先记 ID/base/复现与最小产品范围后实施。
- 本地 Browser 插件初始化 Unknown tool；使用用户允许的云浏览器。云实际视口另记录；390/768/1024/1366、触控与缩放在取得对应实际图前 pending。不用 DOM 或测试代替视觉。
- 初次错误猜测英文文章路径返回404；它不是站内链接故障。改从 Archive 已有链接选择实际公开文章，绝不将猜测路径当产品缺陷。
- 验收：真实截图逐张看、真实目录 click / 滚动 / 返回、主题往返；各尺寸单独记证。无修改产品时不触发 CI 或重跑受阻 gate；main 现有 live 字体超时历史不抹除。gh 不可用则不编造 issue。
- 状态：in-progress，尚无新确认缺陷。

## UI-026 先记录 confirmed / P2

- 实际复现（不是用户报告/推测/偏好）：云1363×936 Night，Archive实际点击计组07，真实目录点击“8.速记”，原生滚动停止于scrollY2580。原图 `uia07c-night-last-20261020.jpg` 已看；Light折叠侧栏的对应跳转与返回顶部正常，不能混称相同布局。
- 返回顶部按钮 rect x1236.609..1280.609/y834..878；第8系列链接 y846.812..900.219，其日期06/11 rect x1253.25..1282.406/y851.922..870.016，日期中心的elementFromPoint实际命中按钮fas-angle-up。遮挡文字与链接触点，已排除圆角矩形误判。尚未点击被盖日期以免混淆导航与返回顶部。
- 根因已定位：`#post-panel-stack` sticky top0/max-height100vh允许系列滚动区占至viewport底部，而固定按钮位于底部58..102px；两个滚动/固定面未预留安全边界。不是日期metadata错误，不修改任何日期数据。
- 最小拟改：从最新main b084独立分支，assets/css/NormaiNight.css仅桌面右侧文章stack可用高度留顶部bar与固定按钮安全区；必要CSS版本号、独立原生滚轮/文字命中回归/CI和本轮文档证据。保留按钮位置/可用性、目录/系列所有链接和滚动、移动原有布局、主题色与字号。不得携入受阻Atlas新门禁或旧审计分支覆盖main数据。
- 验收：1366/1920双主题、900/640窗口高度，真实末节目录click和侧栏原生滚轮覆盖所有系列项/邻接链接，文字实际可见部分不得被按钮命中，sticky面在固定按钮上方；有限旧100vh故障注入必须能拒绝；返回顶部真实click。其余390/768/1024文章目录弹层仍pending，不冒称本任务通过。精确实现head全回归/T01/authoring/production Jekyll与新图人工检查、main自身CI/deploy/live通过前不合main、不done。
- 状态：confirmed，implementation/validation-pending；gh不在PATH，未创建或编造Issue。无新用户决定，Q-UI-01不重复催问。

## 实现与本机检查（不是视觉验收）

- 从main b084独立ui/fix-026实施，未包含check_observe_history.py或其工作流门禁；审计分支dcb历史不覆盖。仅追加CSS的min1200右侧stack max-height calc(100vh - 10rem)，原max-height100vh/overflow-y:auto对移动仍保持。
- 新增7项回归，实际执行assert_clear拒绝日期被盖、旧全高、空链接、隐藏按钮及溢出；其余为有限CSS/真实Range输入/双入口证据接线保护。本机296tests（3.176s）、authoring44/5/7、T01保护44/5/5、Python编译与diff通过。Ravenis LKG输出来自既有unit fixture，不表示线上服务故障。
- 本机没有Chrome/Ruby/Jekyll，本轮不再次安装或绕过此前权限限制。精确新head CI/production Jekyll、新PNG逐张人工查看及main自身部署复验仍validation-pending。未获得修复后实际截图，不推定10rem已视觉通过；若原生滚动/日期位置不满足，新门禁失败并保存现场，不放宽原门禁。
- 三张公开before原JPEG及原始来源/具体命中记录保存[ui026-before/source.json](ui026-before/source.json)；Light末节/返回顶部、Night展开侧栏末节均已看。最终main再次核对必须保持用户Library数据。
