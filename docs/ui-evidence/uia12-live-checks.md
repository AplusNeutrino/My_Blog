# UI-A12 / UI-023 — e44fba12 部署复验

- 2026-10-19 base/main/source `e44fba12d6ddd0aba4b5252ddb265aa25ec45e70`，run39207405231：build117913149025、deploy117919391087 success；首轮verify-live-ui117919453041 failure，不能标全通过或done。
- 先记录范围：只复验UI-023层级/已加载长弹层、滚动、Escape与主题/共享导航，调查初始焦点候选S-A12-01；本轮预定只写计划/日志/公开截图证据，不凭推测改产品。全部原文/metadata/URL/noindex/隐蔽边界不变。
- 首轮live：THINK/BUILD及Thoughts专项成功；OBSERVE已完成390/768/1024双主题6流程，1366 Night进入Ravenis时在settle的document.fonts.ready异步等待30秒超时，尚未产生第7流程截图；1366 Light未开始。不是弹层层级断言失败，也不凭此认定网站字体故障。
- 部分artifact12167877026，1814326bytes，独立SHA256 `4a22c54f58af3643ea672fac96cd38b1a5ac7809de9d48beb29d79cedd1ee08f`匹配；30张viewport/6流程成功不是8流程全部完成。
- 已仅重跑同一head的失败job一次，保留原失败历史；不修改timeout、不跳过字体或删减门禁。完整重跑和1366两主题仍validation-pending。审计存不触发CI的分支，避免取消重跑。

## 实际复验与局限

- 实际查看首轮390/768/1024双主题30张viewport的6张原生联系表；标题完整、遮罩仅覆盖背景、Tab焦点框可见，暂无本作用域新增遮挡或横溢出。专项Atlas仍加载态；不能借30张部分图关闭8组完整矩阵。保存1张390 Light联系表及原audit.json、30源PNG哈希summary；其余5联系表已看但不重复保存，源PNG在该head artifact（14天）。
- 云Chrome1363×936，未fixture：Light与Night均等星历数据出现后实际点击打开长弹层，32个checkbox选项完整可见、父层级1001，标题不再被共享导航遮住、scrim不再覆盖弹层。2张云原截图见uia12-live。两主题长弹层clientHeight/scrollHeight均882px，已全部容纳，不伪称滚动了无溢出内容；小尺寸原生滚动证据是上述CI6流程，不是云移动手测。
- 稳定后两主题初始焦点为refreshAstroButton、inside=true；Light真实Tab到exportChartButton仍在弹层内，Escape关闭后焦点恢复chartControlToggle；Atlas→Ravenis、切Night→Atlas往返保持主题成功。S-A12-01已加载状态未复现，加载中禁用首按钮的初始焦点仍pending，不能宣称候选全关闭。未查询/导出或逐个操作32选项，相关业务验收仍pending；未认证远端服务全面健康。
- noindex,nofollow在线保留。浏览器技能本地工具当前Unknown tool，按技能云浏览器fallback，无权限或登录绕过。
- 同head重跑attempt2当前build117933481131/deploy117933435392显示success，verify-live-ui117933434240运行中。原attempt1 failure继续记录，不用重跑中状态替换成功；UI-023/UI-A12仍validation-pending。
- 277 tests/authoring/T01在独立worktree复核，产品/旧内容/数据/门禁不变；本轮仅计划、日志、公开证据。gh不可用未编造Issue，无新用户决策。下一轮先核对该head attempt2及1366双主题正常viewport；不提前关闭UI-023或重跑旧T00–T39。
