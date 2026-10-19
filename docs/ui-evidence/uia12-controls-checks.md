# UI-A12b — Atlas 独立控件检查

- 状态：in-progress；2026-10-19。base/main `004447dbdf2a8187c2cac9e7ab568709296ac8ab`，审计父 `77a3c16a17a5335133a8cb193d47313fb1b9d1ea`。
- 本轮最小检查组：已加载后的显示菜单开关、数据折叠、历史查询与返回实时、共享导航与双主题；先真实操作/看图，没有确认缺陷不修改产品。先限定云Chrome1363×936，四宽度/移动/缩放未完成不得冒称全矩阵。
- 预定文件范围：本记录、NEUTRIVERSE_UI_FIX_PLAN.md、docs/neutriverse-ui-fix-log.md及公开截图uia12-controls。若确认新缺陷，先另记编号/复现/产品范围再修；不改旧原文/metadata/URL/noindex/隐蔽边界或外部仓库。
- UI024完整线上门禁仍字体等待阻塞；不重跑同job、不降低门禁，不以本轮独立检查代替UI024验收。gh不可用，不编造Issue；无新用户决定。
- 初始实际观察：真实Atlas首开显示正在连接，控制panel可打开；刷新/导出/查询/回到此刻disabled，待自然服务完成后检查，不伪造disabled状态/拦截网络。

## 本轮实际增量

- Light自然服务已完成，10普通行星/11连线；关闭全部相位线真实控件后0连线10节点，空提示可见；恢复后隐藏太阳变9节点/10连线、左表13/17，再恢复太阳变10节点/11连线/左表14/17。均为真实UI交互，不改DOM/网络，菜单偏好恢复。
- 实际看initial/loading与loaded-menu、lines-off、sun-hidden三状态原图；lines-off与sun-hidden发现正常行星符号低对比，转确认UI025并先另记范围。选中太阳后同PNG清晰，是可读性缺陷非审美；本轮切换至该最小修复，历史查询/折叠/其余业务不冒称通过。
- 折叠尝试的getByRole正则在工具中no_matches，未点击成功；后续AX显示行星位置仍展开，不把尝试当通过。Ravenis首次创建tab导航超时后已有实际完成页面，仅绑定既有tab；真实主题切Night再刷新Atlas，Night完整加载截图另记录。未借此判定站点或后端故障。
- UI024完整live仍阻塞；本轮UI025未验留分支，不掩盖该pending。没有新增用户决定。
