# UI-A08k — 默认书籍分页中间区域视觉

状态：done（限定默认书籍全网格）；71ceb601精确main部署/live和全部原生行图已验收。首次失败证据保留，全站仍IN PROGRESS。

## 2026-10-17 — 精确main部署及线上验收

- 验收main71ceb60146048d463772c8c35a12ae39a5cc8c79 / [run38993751090](https://github.com/AplusNeutrino/My_Blog/actions/runs/38993751090)：build117281561210、deploy117283869973、verify-live-ui117283912634均completed/success。243 Python tests、4 Ruby渲染回归、T01/authoring44/5/7、production Jekyll、SEO/资源/旧门禁通过；production/live各192页面与14侧栏。live日志明确UI_LIVE_BASE=https://neutriverse.uk，不用localhost替代。
- live artifact12086956833 /460639421 bytes /sha256:842c79e9a47f1d05c7111ae33ca203ec42fbf7f5447b84edbcfc9f50f29aaf27独立下载摘要匹配。[完整线上审计](uia08k-native-live-audit.json)、[310行诊断](uia08k-native-live-diagnostics.json)、[992裁图来源清单](uia08k-native-live-crop-manifest.json)与32联系表永久入库；原PNG在artifact保留14天。联系表只是原生卡片像素裁剪/等比缩放，页码与来源以manifest为准，不是整页布局图。
- 人工查看下表全部32张线上联系表，覆盖四宽度双主题310行的992卡片；再放大390 Light第3页第4行、1024 Night第4页第3行原生viewport。封面/中英文标题/现有两行换行及卡片边界正常，无新增确认产品缺陷；部分元数据缺省造成高度差是现有数据状态，不当作审美缺陷。视口上下其他行自然局部可见不误报为卡片裁切。与生产相比取景/可读性无实质差异，未修改产品样式。
- 独立核对八流程完整124书籍/6页、页内顺序/全集合无遗漏无重复、行coveredIds完整、原生PNG尺寸/全行视口边界/scrollX=0/图片加载；992加载及末页刷新URL/ID、上一页、返回根和重入通过。逐页ID、图片记录、末页刷新/上一页ID与723c6515生产完全一致；310行诊断中61项完全相同，其余卡片坐标最大差0.542724609375px，不虚称全部字节一致或推断产品故障。
- UI-A08k限定done：默认书籍全网格中间区域视觉已生产/部署/live复验；其他Library分类全库存、首页/OBSERVE/ABOUT全页、应用共享导航与其余矩阵仍pending。无新用户决策，gh未安装不编造Issue。本机243 tests/authoring/T01/diff再次通过；本机无Jekyll/Chrome，真实浏览器来自精确Actions。
- 本轮只回写计划、日志与上述公开live证据。保护9个同步数据文件、正文/filename/date/slug/permalink/metadata/旧URL/hidden/noindex、关联仓库及旧COMPLETE不变；本次证据新head CI另行核对，不重启本项视觉验收。下一项优先首页/OBSERVE/ABOUT全页与滚动交互，避免继续重复书籍审美检查。

| 条件 | 全部线上卡片联系表（四批，原图/ID见来源清单） |
|---|---|
| 390 Night | [1](uia08k-native-live-cards-390-dark-1.jpg) / [2](uia08k-native-live-cards-390-dark-2.jpg) / [3](uia08k-native-live-cards-390-dark-3.jpg) / [4](uia08k-native-live-cards-390-dark-4.jpg) |
| 390 Light | [1](uia08k-native-live-cards-390-light-1.jpg) / [2](uia08k-native-live-cards-390-light-2.jpg) / [3](uia08k-native-live-cards-390-light-3.jpg) / [4](uia08k-native-live-cards-390-light-4.jpg) |
| 768 Night | [1](uia08k-native-live-cards-768-dark-1.jpg) / [2](uia08k-native-live-cards-768-dark-2.jpg) / [3](uia08k-native-live-cards-768-dark-3.jpg) / [4](uia08k-native-live-cards-768-dark-4.jpg) |
| 768 Light | [1](uia08k-native-live-cards-768-light-1.jpg) / [2](uia08k-native-live-cards-768-light-2.jpg) / [3](uia08k-native-live-cards-768-light-3.jpg) / [4](uia08k-native-live-cards-768-light-4.jpg) |
| 1024 Night | [1](uia08k-native-live-cards-1024-dark-1.jpg) / [2](uia08k-native-live-cards-1024-dark-2.jpg) / [3](uia08k-native-live-cards-1024-dark-3.jpg) / [4](uia08k-native-live-cards-1024-dark-4.jpg) |
| 1024 Light | [1](uia08k-native-live-cards-1024-light-1.jpg) / [2](uia08k-native-live-cards-1024-light-2.jpg) / [3](uia08k-native-live-cards-1024-light-3.jpg) / [4](uia08k-native-live-cards-1024-light-4.jpg) |
| 1366 Night | [1](uia08k-native-live-cards-1366-dark-1.jpg) / [2](uia08k-native-live-cards-1366-dark-2.jpg) / [3](uia08k-native-live-cards-1366-dark-3.jpg) / [4](uia08k-native-live-cards-1366-dark-4.jpg) |
| 1366 Light | [1](uia08k-native-live-cards-1366-light-1.jpg) / [2](uia08k-native-live-cards-1366-light-2.jpg) / [3](uia08k-native-live-cards-1366-light-3.jpg) / [4](uia08k-native-live-cards-1366-light-4.jpg) |

## 2026-10-17 — 原生行截图生产验收

- head723c651515b372756e12879f9c757a2cc8dc1b6b / [run38989785855](https://github.com/AplusNeutrino/My_Blog/actions/runs/38989785855)：build117269649689 success，deploy117272512100/live117272512541 skipped（工作分支，不能作为部署证明）。243 Python tests、4 Ruby渲染回归、T01/authoring/production Jekyll/SEO/资源/旧门禁、192页面+14侧栏通过。
- artifact12085016466，462140557 bytes，sha256:48ee7afff3dc1fbb7e43a037bc22bc26cd42f7552a6a41311f71be3ce2e267c2，下载后独立匹配。新[完整审计](uia08k-native-production-audit.json)、[310行诊断](uia08k-native-production-diagnostics.json)、[992卡片裁图来源清单](uia08k-native-production-crop-manifest.json)永久入库；原PNG在该artifact保留14天。
- 390/768/1024/1366 × Night/Light八流程，每组124书籍/6页（24/24/24/24/24/4），ID顺序完整且无重复；390两列共124行，其余六流程四列共186行，合计310原生viewport。每行PNG实际尺寸与原生viewport相同、全行卡片在topbar下和clientWidth/viewport内、scrollX=0、全部封面complete且自然尺寸为正，行coveredIds顺序严格覆盖每页。保留96页首尾、992加载、末页刷新同URL/ID、上一页/返回根/重入等门禁。
- 人工逐张看下表全部32张联系表，覆盖992张实际卡片截图（124×8），无首次整页裁图混入上一行或丢失本卡标题的问题。再放大原始390 Light第3页第4行、1024 Night第4页第3行viewport：所审行封面/标题可见、边界对齐、无横向溢出；其他行上下局部进入视口属于正常滚动取景，不误报为内容裁切。未确认新产品缺陷，未凭卡片高度/封面审美差异改样式。
- 本机再次243 tests、authoring44/5/7、T01保护44/5/5、diff通过；本机无Jekyll/Chrome，真实构建和浏览器来自上述精确CI。范围仍仅默认书籍网格；其他分类、全站余项不据此通过。gh未安装，不编造Issue；无新用户决策。
- base main仍dcb9e1362124d27bcf78aa0fe3d3aeb2cd3cd4b3。本次仅交付已验证审计/回归与公开证据/计划日志，不改产品、9个同步数据文件、原文/metadata/URL/hidden/noindex或旧COMPLETE。新main自身CI/Pages与310线上行图仍validation-pending，不用723c6515分支成功代替。

| 条件 | 全部卡片原生截图联系表（按ID顺序分四批） |
|---|---|
| 390 Night | [1](uia08k-native-production-cards-390-dark-1.jpg) / [2](uia08k-native-production-cards-390-dark-2.jpg) / [3](uia08k-native-production-cards-390-dark-3.jpg) / [4](uia08k-native-production-cards-390-dark-4.jpg) |
| 390 Light | [1](uia08k-native-production-cards-390-light-1.jpg) / [2](uia08k-native-production-cards-390-light-2.jpg) / [3](uia08k-native-production-cards-390-light-3.jpg) / [4](uia08k-native-production-cards-390-light-4.jpg) |
| 768 Night | [1](uia08k-native-production-cards-768-dark-1.jpg) / [2](uia08k-native-production-cards-768-dark-2.jpg) / [3](uia08k-native-production-cards-768-dark-3.jpg) / [4](uia08k-native-production-cards-768-dark-4.jpg) |
| 768 Light | [1](uia08k-native-production-cards-768-light-1.jpg) / [2](uia08k-native-production-cards-768-light-2.jpg) / [3](uia08k-native-production-cards-768-light-3.jpg) / [4](uia08k-native-production-cards-768-light-4.jpg) |
| 1024 Night | [1](uia08k-native-production-cards-1024-dark-1.jpg) / [2](uia08k-native-production-cards-1024-dark-2.jpg) / [3](uia08k-native-production-cards-1024-dark-3.jpg) / [4](uia08k-native-production-cards-1024-dark-4.jpg) |
| 1024 Light | [1](uia08k-native-production-cards-1024-light-1.jpg) / [2](uia08k-native-production-cards-1024-light-2.jpg) / [3](uia08k-native-production-cards-1024-light-3.jpg) / [4](uia08k-native-production-cards-1024-light-4.jpg) |
| 1366 Night | [1](uia08k-native-production-cards-1366-dark-1.jpg) / [2](uia08k-native-production-cards-1366-dark-2.jpg) / [3](uia08k-native-production-cards-1366-dark-3.jpg) / [4](uia08k-native-production-cards-1366-dark-4.jpg) |
| 1366 Light | [1](uia08k-native-production-cards-1366-light-1.jpg) / [2](uia08k-native-production-cards-1366-light-2.jpg) / [3](uia08k-native-production-cards-1366-light-3.jpg) / [4](uia08k-native-production-cards-1366-light-4.jpg) |

## 2026-10-17 — 首次生产检查与取景方式修正

- 精确eccb2551644d0a94b65830a6a5927ac057e73896 / [run38984590940](https://github.com/AplusNeutrino/My_Blog/actions/runs/38984590940)：build117253009701 success，deploy117255688589/live117255689373 skipped（分支，不作部署）。243 tests、4 Ruby渲染回归、T01/authoring/Jekyll/SEO/资源/既有门禁和192页面+14侧栏通过。
- artifact12082608255 /354689315 bytes /sha256:5237417b3bd66185e103f9cf56212e3e816be11209d844682237c2eb5e4ef2c6独立下载匹配。48个PNG签名/宽高、卡片集合与拍摄前几何门禁通过，但不代表视觉取景可靠。
- 实际看390双主题8张逐卡联系表、390 Light第3页整图及其顶部原始像素：截取卡片时混入上一行标题、裁去本卡标题。第3页拍摄前viewport width390/clientWidth379；首卡rect.right185.09375，次卡right363，而整页PNG中可见右缘约190/374。PNG像素布局与拍摄前几何不一致，不能据此证明原生viewport中间区域通过。CDP整页取景时滚动条占位变化可能相关，但此处不宣称已证实浏览器内部根因，也不判为产品缺陷；768/1024/1366未人工验收，不冒称48图全通过。
- 保留首次[完整审计](uia08k-production-audit.json)、[48诊断](uia08k-production-diagnostics.json)、390 Light[第1联系表](uia08k-production-cards-390-light-1.jpg)/[第2联系表](uia08k-production-cards-390-light-2.jpg)及[第3页原始PNG](uia08k-production-mismatch-390-light.png)。联系表为按拍摄前rect裁图，正是坐标不一致的失败证据，不能冒充卡片实际被裁切；原包保留14天。
- 修正仅审计：取消本项超视口CDP取景，按实际CSS grid列数逐行真实滚动，用原生viewport PNG；每行全部卡片完整位于topbar下/视口内、图片加载、PNG实际尺寸与原生viewport一致，coveredIds按序等于本页所有ID。原96页首尾/全量加载/刷新返回门禁保留；原全页PNG尺寸/范围断言替换为更直接的原生viewport完整行覆盖检查，不放宽验收。
- 当前390为2列，其余3宽度当前4列，预计新增310行截图（124书籍×2/2 +124×6/4），以实际列数动态计算，不固定未来数据。48整页图不再是修正后目标。每一行都需人工看图；其他分类仍pending。本机243 tests/authoring44/5/7/T01保护44/5/5/diff通过，不代替真实Jekyll/Chrome。
- main仍dcb9e136，修正留ui/audit-008k，新head production/行截图与main/live全部validation-pending，无新用户决策。不改产品/数据/原文/metadata/URL/hidden/noindex、关联仓库或旧COMPLETE。
- 真实修正实现337f2d1cc97b62e5cccf3f7367cf3a0009481c1b已expected_sha非强推保存ui/audit-008k，11个远程blob与本地git hash-object逐项相同；随后只追加此SHA检查点。下一轮核对最终分支head CI/原生行截图，不复用eccb2551整页结果作为验收。

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
