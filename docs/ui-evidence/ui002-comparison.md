# UI-002 / UI-A02 evidence

2026-10-14；base main `bc3efad53188f1ff86ae5b49d5a159a136643792`。
实现 head `4d7eac959d1448cbdeb490aebf11e1a79a7b66d4`。

## 已复现与根因

线上 OfficeSpire 1363×936，Light/Night：hero 与 detail section 圆角为 0px，项目面包屑字体回退到阅读字体。组件引用未定义的 `--nv-radius-lg/md`、`--nv-shadow-soft`、`--nv-font-mono`。补已有尺度的圆角默认值，阴影显式 none 保持旧表现，数据字体统一复用 `--nv-font-data`。不是新主题或重设计。

| 条件 | 修复前 | 修复后 |
|---|---|---|
| OfficeSpire Light | [全页](ui002-before-light.jpg) | [全页](ui002-after-light.jpg) |
| OfficeSpire Night | [全页](ui002-before-night.jpg) | [全页](ui002-after-night.jpg) |

部署后1363×936实际复验：hero 8px / section 5.6px，面包屑IBM Plex Mono字体栈；Light/Night全页截图查看、主题切换、详情返回BUILD、状态筛选1/7通过；实际article卡片8px（外层li本身仍是0px，不将li圆角当作卡片样式）。文字和链接内容不改。

## Production 浏览器证据

[工作分支 run38505520642](https://github.com/AplusNeutrino/My_Blog/actions/runs/38505520642)：build 成功，部署按条件跳过。截图 artifact `11867593738`，同一实现 SHA 的112张全页PNG（14天保留）。[完整几何与交互记录](uia02-audit.json)持久保存。112场景包含THINK默认/Fragment/空结果/末页、BUILD全项目/状态筛选、七个公开项目详情。16组筛选/刷新/返回交互通过；页面不横溢、标题不裁切，项目圆角和等宽字体有效，特定详情noindex保留。

人工查看了下面8张联系表的各页面总体布局，并放大390px THINK正文/控件、长项目名、1024px OfficeSpire、1366px BUILD。联系表不能证明所有细文字都已精读，也不能替代尚未覆盖的其他页面/hover/触控/缩放检查。

| 宽度 | Night | Light |
|---|---|---|
| 390 | [截图联系表](uia02-sheet-390-dark.jpg) | [截图联系表](uia02-sheet-390-light.jpg) |
| 768 | [截图联系表](uia02-sheet-768-dark.jpg) | [截图联系表](uia02-sheet-768-light.jpg) |
| 1024 | [截图联系表](uia02-sheet-1024-dark.jpg) | [截图联系表](uia02-sheet-1024-light.jpg) |
| 1366 | [截图联系表](uia02-sheet-1366-dark.jpg) | [截图联系表](uia02-sheet-1366-light.jpg) |

## 新发现与局限

- UI-003：390/768px顶栏显示内部布局名，不是当前页标题；已编号待修复。
- 大尺寸全页CDP截图侧栏部分裁切仍是待核实疑点；需viewport截图和开闭复现，不能只凭此截图断言线上故障。
- [线上Night搜索截图](uia02-search-night.jpg)：输入“计网”显示10项公开结果，取消返回THINK；1363×936云浏览器实际操作。
- 无私人内容或隐藏Gate/NAVI应用截图；这里只检查既有公开项目详情。其应用/外部项目仓库未改。
- [main run38505942304](https://github.com/AplusNeutrino/My_Blog/actions/runs/38505942304)：同一head build115663355032、deploy115664001709 success；线上同场景双主题复验通过。UI-002 done；UI-003和其他未覆盖页面仍待后续，整轮非COMPLETE。
