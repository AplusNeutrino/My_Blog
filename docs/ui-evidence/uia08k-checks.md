# UI-A08k — 默认书籍分页中间区域视觉

状态：validation-pending；尚无本次精确实现head截图或视觉验收。

实现仅扩展既有bookInventory流程：每页首尾截图后真实回到顶部，原生CDP整页截图；校验PNG签名/IHDR宽高等于clip、全部当前卡片文档矩形在clip内、ID等于本页遍历集合、图片已加载，记录fullPage元数据。保留原96图/992加载等门禁。新增2项接线回归，原视觉范围文案随新增整页证据更新，未删除原断言。

本机243 tests、authoring44/5/7、T01保护44/5/5和diff通过；这些不代替production Jekyll/真实Chrome或人工看图。本次48整页图及main/deploy/live仍pending，无产品或数据修改。

真实实现a059a6a4a111f588c2cb2fc5e40cf37d98a28063已保存ui/audit-008k，6个远程blob与本地git hash-object逐项一致；随后只追加此SHA检查点。main保持dcb9e136，未部署本次实现；下一轮必须核对最终分支head CI及48图，不能拿base成功代替。

- base main dcb9e1362124d27bcf78aa0fe3d3aeb2cd3cd4b3；run38979246164 build117235958658/deploy117238946046/live117239020388全部success，仅为base状态。
- 沿用UI-A08j默认书籍真实分类/完整分页/逐卡加载/刷新返回流程，逐页在原生图片complete/decode后补整页截图，覆盖首尾viewport之间卡片。当前124书籍/6页，390/768/1024/1366×Night/Light，目标48整页PNG；数量随真实数据动态计算，不固定未来同步库存。
- 截图使用既有CDP captureBeyondViewport，不改变窗口尺寸、图片src/loading、DOM或CSS，不注入数据，不扩大为其他分类全库存验收。原96页首尾viewport图和所有原断言保留。
- 记录每页原生viewport、clientWidth/page宽高、grid/card文档坐标、已加载图片自然尺寸、截图clip和实际PNG宽高；确保截图确实包含全部当前卡片，不只是写入一个PNG路径。自动断言不等于视觉验收，必须逐页人工查看整图/分段联系表并放大中间代表图。
- 文件范围：tools/check_think_build_visual.py、必要tests、本轮计划日志及此证据；不改产品/同步数据、正文/filename/date/slug/permalink/metadata、旧URL、hidden/noindex、关联仓库或旧COMPLETE历史。
- 先ui/audit-008k保存未验收实现；精确head production/Jekyll/回归、48图人工核查通过后才交付main；再核对本次main Actions/build/deploy及相同线上截图/交互。当前均pending，本机无Ruby/Jekyll/Chrome，不冒称本机视觉通过。
- gh未安装，不编造Issue；没有新用户决策或确认产品缺陷，不猜测改样式。其他分类/全站余项保持pending。
