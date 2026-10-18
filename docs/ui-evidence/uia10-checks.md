# UI-A10 — THINK四页原生整页与分页往返

状态：validation-pending；专项8b3308d生产build成功、包已独立核验并开始实际看图，确认UI-019遮挡。不是视觉通过，main不改。

## 2026-10-18 专项包实际验收发现UI-019

- 8b3308db63b810c58afbce317a27427d3a38072e / [run39110109162](https://github.com/AplusNeutrino/My_Blog/actions/runs/39110109162) build117624212912 success；工作分支deploy117628254520/live117628258809 skipped。265 tests/T01/authoring44/5/7/production Jekyll与旧门禁成功。专项artifact12129943687共51332149 bytes，下载独立SHA256 60d83add292b465be9e17097e35803e93f4b4cc4b65b7cf36fa10693cfc0eee5一致，下载限制已解除；不需要再下载超限总包。
- 八流程32页共292原生帧，全部JSON机械核对44条唯一href顺序12/12/12/8、末页刷新/上一页、连续main覆盖/实际PNG尺寸/无横向溢出通过。人工仅查看390 Light第一页13帧3联系表并放大2/6/7/8原图，确认介绍与写作卡摘要被返回顶部按钮遮挡，记录[UI-019](ui019-checks.md)；不能以CI成功判定视觉正常。剩余279帧未人工验收。
- 当前优先UI-019最小修复，保留A10审计与所有门禁，工作分支ui/fix-019；生产修复后与main/live仍需同head/同场景逐项验收。before原图/实际查看联系表/摘要在ui019-before/与ui019-before-summary.json，无新用户决策。以下旧记录是原时点状态，非当前下载状态。

## 2026-10-18 精确生产结果与证据下载限制（先记录）

- 实现c1a7bb710467663093b75d947458ac2ebbd35728；[run39105966506](https://github.com/AplusNeutrino/My_Blog/actions/runs/39105966506) build117611754548 success，工作分支deploy117615335443/live117615336133 skipped。日志核对264 tests、4项Ruby、T01保护、authoring44/5/7、production Jekyll/Search/feed/SEO/资源/旧门禁与主192成功。未取回JSON或人工截图，不写视觉通过，也不冒称已部署。
- production artifact12128916636为543024842 bytes，服务端标注SHA256 1c246977e59fa99e64e2bb110ac29b0b5cfeef316ac54992af36073c93ffb3cf；download_workflow_artifact明确拒绝超过536870912 bytes，未取得字节，因此未独立核验该摘要、未生成联系表、未看原图。不是产品UI缺陷，不绕过接口限制或把成功日志当人工图。
- 本次最小范围先记录：仅pages-deploy.yml增production/live的THINK分页专项artifact（原生PNG、逐帧JSON、8流程JSON及audit.json），同时保留原总包和所有原检查/等待/失败机制/截图原质量。加1项包装接线回归和计划日志；不改审计/产品/数据/原文/URL/hidden/noindex/外部仓库/旧COMPLETE。在ui/audit-010非强推接续，新head重新构建截图待验，不拿c1成功代替。main仍40e6ee2b；无新用户决策。
- 包装接线实现完成；本机265 tests、authoring44/5/7、T01保护44/5/5、diff通过。审计脚本未改，不重编码或裁剪PNG，不移除原总包；新专项artifact尚未生成，必须下载其实际字节校验并看图后才能生产视觉验收。当前仍validation-pending，下一项新head精确CI与专项原图。

## 2026-10-18 先记录范围

- base main40e6ee2b693778dacca9140ff9fabaf454176c78；run39102519248 build117601511609/deploy117604332268/live117604361133全部success。关闭上一证据head pending；A09限定done不重启，不重做T00–T39。
- Task UI-A10：390/768/1024/1366 × Night/Prospero Light，遍历THINK默认四页。按原始公开列表顺序核对44条规范href，页内/跨页无重无漏、每页12/12/12/8、URL/current marker一致；末页刷新URL和ID不变、上一页回到原第三页。用既有严格原生滚轮全main采证函数逐页截图，保留旧门禁/字体30s/动画20s及失败采证，不以静态测试代视觉。
- 范围仅tools/check_think_build_visual.py、必要审计回归、本文件/本轮UI计划日志；不改产品/样式/数据/正文/metadata/URL/hidden/noindex、外部仓库或旧COMPLETE。未验证保存ui/audit-010工作分支，完整生产与人工截图通过前不交main；Thought点赞/其他筛选与矩阵另待检查。
- AGENTS/docs/agents/ADR/旧COMPLETE与本轮计划日志、用户补充核对；CONTEXT无，gh不在PATH不编造Issue。独立worktree保留原目录用户修改和同步，无新增用户决策。实施与结果待记录。

## 实现与本机验证

- 在原think-all筛选检查之后新增think_pagination_controls；原192场景、14侧栏、24公开流程及全部门禁保留。严格44唯一href与四页顺序12/12/12/8、URL/current marker，真实pager pointer click；每页调用既有原生滚轮全main截图/连续覆盖/PNG尺寸/无溢出/返回顶部检查，目标名只允许原三页或think-page-1至4，原三页公开往返不减少。
- 末页刷新严格同URL/ID，上一页严格第三页ID；失败保存PNG和部分页JSON并重新抛出，不将部分图当验收。补2项审计接线测试，只检查接线，非视觉证明。
- 本机264 tests、authoring44/5/7、T01保护44/5/5、diff通过；本机无Chrome/Jekyll，新增32页的production/实际截图与交互均未运行，状态validation-pending。不修改产品，先ui/audit-010，下一轮核对同一新head生产浏览器与真实截图；main/live待后续交付验收。
