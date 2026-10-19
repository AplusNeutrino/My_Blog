# UI-024 — Atlas 加载态打开弹层未移入焦点

- 状态：confirmed / implementation pending；P2键盘交互。2026-10-19，base/main e44fba12d6ddd0aba4b5252ddb265aa25ec45e70，审计父127c1ee7e70c5265c95b13883822da770c49bf72。
- 非用户报告/偏好：本轮云Chrome1363×936 Prospero Light真实加载态click打开，两个独立观察调用后active=chartControlToggle、panel.contains=false、refresh.disabled=true。服务随后加载完毕但焦点仍在trigger，Shift+Tab实际移到弹层外“返回Neutriverse主站”链接。即候选S-A12-01转确认UI-024，不是即时截图/rAF先后差异。
- 截图ui024-light-loading-focus-before.jpg捕获时远端已完成加载（与此前disabled=true诊断时间不同）；不把已加载截图冒称加载中，焦点遗留由后续DOM/AX证据补充。ui024-loading-light-before.jpg同样为加载完成后的焦点遗留状态。原UI-023层级正常，不重开该问题。
- 修改前范围：occult-atlas-app/app.js仅初始焦点选择；_data/occult_atlas.yml资源版本39→40；tests必要执行回归、tools/check_observe_dialog.py稳定初始焦点/反向Tab门禁；本计划日志/公开证据。禁止改服务等待、正文/metadata/URL/noindex/隐蔽边界、主题/业务语义，不删除旧门禁。
- 验收：禁用首按钮时首个可交互控件获得焦点，已加载时仍优先刷新；rAF执行前关闭不得抢回隐藏panel焦点；反向Tab/正向Tab边界、Escape恢复保留。四宽度双主题production及部署同场景真实截图与交互未完成前validation-pending，工作分支不提前main。
- gh不在PATH时如实记录未建Issue；无新用户决定。云不可调视口，其他宽度依赖CI实际截图，不以Node执行或DOM代视觉。

## 最小实现与当前验证

- 初始focus与原trap共用既有enabled/visible列表，不再focus disabled刷新；rAF执行时panel已关闭则不抢焦点。资源版本40；不改变原trap或服务/样式语义。
- 2项Node实际函数执行回归覆盖disabled→datetime、loaded→refresh、Shift+Tab/Tab边界、Escape恢复、快速关闭及空列表fallback；旧first-button逻辑故障注入必须失败。279 tests（2.615s）、authoring44/5/7、T01正文/URL/hidden44/5/5通过，node语法/专项Python编译/diff通过；这不是视觉验收。
- 原OBSERVE8流程增加稳定初始focus wait；另每流程独立“仅前两按钮disabled”的可恢复UI fixture检查datetime初焦点、原生Shift+Tab到末控件及Escape返回，保存loading-focus/loading-wrap正常viewport。不拦截网络或修改远端服务，fixture明确不等于自然加载状态/后端健康。原层级故障注入/滚动/Tab/导航等门禁保留。
- 真实修复前两图保存ui024-before/light-open-focus-outside.jpg与light-shift-tab-escaped.jpg：截图已加载完成，后图主站链接focus框在panel后方可见，AX与DOM记录active A aria-label返回Neutriverse主站、inside=false、panel仍open。未做修复后线上操作；production Jekyll/四宽度双主题截图/完整CI/部署仍validation-pending。
