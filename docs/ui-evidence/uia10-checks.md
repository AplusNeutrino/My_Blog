# UI-A10 — THINK四页原生整页与分页往返

状态：in-progress；未确认产品缺陷，不改样式。

## 2026-10-18 先记录范围

- base main40e6ee2b693778dacca9140ff9fabaf454176c78；run39102519248 build117601511609/deploy117604332268/live117604361133全部success。关闭上一证据head pending；A09限定done不重启，不重做T00–T39。
- Task UI-A10：390/768/1024/1366 × Night/Prospero Light，遍历THINK默认四页。按原始公开列表顺序核对44条规范href，页内/跨页无重无漏、每页12/12/12/8、URL/current marker一致；末页刷新URL和ID不变、上一页回到原第三页。用既有严格原生滚轮全main采证函数逐页截图，保留旧门禁/字体30s/动画20s及失败采证，不以静态测试代视觉。
- 范围仅tools/check_think_build_visual.py、必要审计回归、本文件/本轮UI计划日志；不改产品/样式/数据/正文/metadata/URL/hidden/noindex、外部仓库或旧COMPLETE。未验证保存ui/audit-010工作分支，完整生产与人工截图通过前不交main；Thought点赞/其他筛选与矩阵另待检查。
- AGENTS/docs/agents/ADR/旧COMPLETE与本轮计划日志、用户补充核对；CONTEXT无，gh不在PATH不编造Issue。独立worktree保留原目录用户修改和同步，无新增用户决策。实施与结果待记录。

## 实现与本机验证

- 在原think-all筛选检查之后新增think_pagination_controls；原192场景、14侧栏、24公开流程及全部门禁保留。严格44唯一href与四页顺序12/12/12/8、URL/current marker，真实pager pointer click；每页调用既有原生滚轮全main截图/连续覆盖/PNG尺寸/无溢出/返回顶部检查，目标名只允许原三页或think-page-1至4，原三页公开往返不减少。
- 末页刷新严格同URL/ID，上一页严格第三页ID；失败保存PNG和部分页JSON并重新抛出，不将部分图当验收。补2项审计接线测试，只检查接线，非视觉证明。
- 本机264 tests、authoring44/5/7、T01保护44/5/5、diff通过；本机无Chrome/Jekyll，新增32页的production/实际截图与交互均未运行，状态validation-pending。不修改产品，先ui/audit-010，下一轮核对同一新head生产浏览器与真实截图；main/live待后续交付验收。
