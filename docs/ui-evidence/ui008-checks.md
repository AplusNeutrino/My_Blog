# UI-008 窄屏高级筛选浮层溢出

状态：done；以下保留失败、生产与线上验收历史。

证据head `ab85af5a022eb9b0a27126f2613fa7e7dadb0772`，
[run38724996114](https://github.com/AplusNeutrino/My_Blog/actions/runs/38724996114)，build116388845796 failure；deploy/live skipped。
218 tests、T01/authoring/Jekyll及此前旧门禁通过；新Library审计390 Night第2页刷新同ID成功，随后年份可见文本断言失败。未把失败记作通过。

下载artifact11967657119，sha256:5a489b51123bc5c00d0999fe21a1050da36e6df862cd78b64fc274b1809de92a。人工查看page2/open/failure三张原图：第2页当前按钮2正确；[高级筛选展开截图](ui008-before-390-night.png)中页面内容向左移、标题左侧被裁，浮层从位于中部的summary开始向右延伸。实际viewport390×701；该布局缺陷不同于浮层按设计覆盖卡片的行为。

根因：panel绝对定位left:0相对details，宽min(19rem,82vw)，没有考虑该details距页面左缘的位置；窄屏聚焦select/滚动到面板时可横向移出原页面。最小修复仅720px内将toolbar作为定位参照，details静态定位，panel左右均约束到toolbar边界。桌面与筛选数据/行为不改。

审计新增panel真实矩形、viewport、scrollX与卡片年份innerText/textContent记录；严格拒绝展开panel超出视口或页面横向偏移。年份语义比较读取实际textContent，避免将布局可见性与数据过滤混为一谈；所有年份匹配、分页、刷新URL/ID、清除断言仍保留，新的截图仍必须人工复核。原失败图未保存年份textContent，不能仅据此次断言宣称网站年份筛选失效。

本地220 tests、authoring、T01及diff检查通过；修复后32张分页/面板/组合筛选/清除四宽度双主题截图、完整production192+14、精确main部署和live复验均pending。代码先保留ui/fix-007，不放宽门禁或将静态测试当视觉验收。无新用户决定问题；其他全站矩阵未完成。

## 2026-10-15 生产验收通过，线上待验收

精确head51f5e999 / run38731750252的build116411370430 success，220 tests、T01/authoring/Jekyll/旧门禁、192+14及8分页/筛选流程通过。实际查看32张四宽度双主题截图两联系表，放大390 Night面板原图，浮层与标题/页面左缘均在屏内；32份几何scrollX=0，展开面板左右界均通过。

完整artifact摘要、JSON与截图见[UI-007共同生产证据](ui007-checks.md#2026-10-15-ui-007ui-008生产验收)。仍须精确main部署和线上同场景复验，状态validation-pending；不以CI成功单独替代视觉。

## 2026-10-15 线上验收通过

精确main 3a6258a2cfaca97c281d3d96843c238508f57f63 / run38739750905，build116438041048、deploy116441394565、verify-live-ui116441674267全部success。live artifact11975492793摘要独立匹配，32张四宽度双主题截图已人工查看，并放大390 Night展开面板原图：标题左侧完整、面板左右均在viewport内，32诊断scrollX=0；原分页/筛选/刷新/清除8流程保持通过。相比修复前页面横向偏移与标题裁切，本次相同窄屏展开场景不再出现。

共同的完整线上audit、32诊断、两联系表及验收局限见[UI-007线上证据](ui007-checks.md#2026-10-15-精确main线上验收)。UI-008 done，不将此限定验收当全站COMPLETE；本次没有追加产品样式改动。
