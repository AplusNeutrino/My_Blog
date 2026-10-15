# Neutriverse UI 修复计划

状态：IN PROGRESS。独立于已 COMPLETE 的 T00–T39 重构；不改写历史验收。
启动日期：2026-10-14。仓库：AplusNeutrino/My_Blog。

## 范围与保护

只修复已实际复现的显示/交互缺陷；不借审美偏好重新设计。保留 Night / Prospero Light、四入口英文与中文说明、Jekyll/Pages、旧 URL、正文和 metadata、hidden/noindex、Gate/NAVI/旅行隐蔽边界、七项目且排除 MMXProj。不修改外部项目仓库或从聊天补入个人信息。

## 流程与验收

每轮先读 main/head、AGENTS/domain/ADR、本计划与日志；记录问题 ID、base、范围、复现、验收后实现。通过的小交付非强推提交 main，半成品留工作分支。精确实现 head 的 CI/build/deploy 与部署后同场景截图都通过才标 done；未完成验证保持 validation-pending。问题需通过 gh 跟踪；gh 不可用时在日志准确记录，不编造 Issue。

截图人工检查与自动几何/交互检查分别记证；通过测试不等于视觉正常。已有内容保护、authoring、Search/feed、SEO、资源、移动/无障碍门禁保留。

## 问题台账

| ID | 优先级 | 已复现问题 | 状态 | 验收 |
|---|---|---|---|---|
| UI-001 | P2 | 四入口导航卡片同一行底部不齐，长中文摘要使内部链接未撑满 Grid 单元格 | done | 两主题、四视口：首页及四入口卡片边框撑满各自单元格，保留换行/链接/焦点；production CI 与线上复验 |
| UI-002 | P2 | 项目/观察组件引用未定义的圆角、阴影与等宽字体变量；圆角失效、数据文本字体回退 | done | 变量默认值与运行时圆角/字体通过，112截图/交互与旧门禁通过，精确head main部署和双主题线上复验通过 |
| UI-003 | P2 | 390/768px截图顶栏显示内部布局名 Neutriverse-section / Neutriverse-project，而不是页面标题 | done | 120项production与120项部署后live场景、32张viewport、标题/tooltip/控件不重叠门禁通过；移动双主题截图复验 |
| UI-003a | P2 | 快速关闭移动菜单时延迟焦点可能回到已关闭侧栏；390px mask焦点门禁超时 | done | production及live390/768双主题各3次快速mask关闭、跨两帧焦点保持在trigger；原mask/Escape门禁通过 |
| UI-004 | P1 | 1024/1366×900窗口的实际viewport截图显示侧栏DISCOVER检索组与社交/主题组重叠 | done | production及live14短/高窗口场景无重叠、按钮hit-test/主题/搜索通过；人工查看本次live截图 |
| UI-005 | P1 | 计组04两张Markdown表格紧邻标题，线上渲染为连续竖线正文，失去行列结构 | done | 原md/metadata不改；4项渲染回归与T01通过；精确main部署和live四宽度双主题8截图/两table/横向阅读通过，已人工复验 |

## 检查矩阵

以下每行必须逐页覆盖 390/768/1024/1366px × Night/Light，并人工看截图与操作；扩展到320/1920px/缩放时记录实际条件。云浏览器当前1363×936，仅记该视口；其他尺寸以CI/本地浏览器证据补充。不能以五页面的既有40项门禁冒充全站检查。

| 页面组 | 视觉检查 | 交互 |
|---|---|---|
| 首页、THINK、BUILD、OBSERVE、ABOUT | 导航UI-001：40项截图与几何通过；THINK 1363px双主题已部署复验。全页检查仍pending | THINK侧栏展开/收起、双主题切换已操作；其他pending |
| THINK筛选/分页、Series、Tags、Archive、Thoughts | THINK四状态已检查；UI-A05的Series目录/Tags/Archive/Thoughts：390/768/1024/1366双主题32张生产及线上viewport已人工查看并放大代表原图，无新增确认缺陷 | THINK筛选/刷新/返回通过；UI-A05线上32组长标签/归档打开返回、Series精确筛选数量/返回、Thought稳定锚点/返回通过；点赞及其余hover/focus仍pending |
| BUILD列表、七个BUILD详情 | 80张两主题四宽度全页截图已生成并看联系表；长项目名与OfficeSpire原图放大；UI-002双主题线上复验通过 | BUILD筛选/刷新/返回属于16组自动交互，通过；线上详情返回/状态筛选通过；应用/外部来源链接不作本轮修改 |
| 代表文章：代码、表格、图片 | UI-005表格8场景及UI-A07代码/图片16场景：四宽度双主题生产/live截图已人工查看并放大代表原图，未新增确认缺陷 | 表格横向阅读、图片逐张加载、移动touch/桌面arrow翻页关闭、复制提示及UI-A07b线上实际剪贴板16场景通过；其余阅读控件pending |
| Library、友链 | UI-A08a限定done：生产及线上四宽度双主题40张根页/弹层/目录布局/友链/焦点截图已查看，无新增确认缺陷；部分封面加载状态未验收 | 生产及线上16场景弹层开闭、书籍目录返回、友链href与真实Tab往返通过；时间线/搜索/高级筛选/分页/完整延迟加载及外部站点仍pending |
| Ravenis、Occult Atlas | pending | 共享导航/核心控件/返回pending |
| Gate/NAVI（仅既有隐蔽边界） | pending | 不将私有截图/入口加入公开台账 |

## 集中问题队列

无新增需要用户决定的问题。未来按Q编号记录影响、选项、推荐；未回复不视为同意，继续无关任务。

## 完成条件

全部矩阵有明确截图和交互证据；所有确认缺陷完成部署复验；无validation-pending或未解释阻塞。写 docs/neutriverse-ui-fix-final-report.md，标 COMPLETE、最终main/线上核对后暂停“修复 Neutriverse UI”。不无限审美修改。

## 当前运行

UI-A08b生产通过、待main/live：base main30e26ead4ee97aa6bc3120aec3372897bb1285bc，验收head aa328fa7b8f5e09d58adbe3d8aada6f7ae0f8b03 / run38674518402 build116224939740 success，分支deploy/live skipped。8场景56次可见封面complete/尺寸/原生decode通过；人工查看8张解码后截图两联系表并放大390 Night原图，均显示封面，无新增确认产品缺陷。211 tests/4 Ruby/T01/authoring/Jekyll/旧门禁及192+14通过；只交付审计和公开证据，不改样式或图片源。非强推main后核对实际head部署及live8图/加载记录，仍validation-pending，搜索/筛选/分页等另项pending，无新问题。[证据](docs/ui-evidence/uia08b-checks.md)。

UI-A08b接续validation-pending：base main30e26ead、工作head de7dbdf4；run38668866802 build116206975426 success、deploy/live skipped。下载artifact11942794466，8场景56次可见封面complete/尺寸全部通过；实际看8张covers截图及390 Night后续category原图，前者局部空白、后者封面已显示，不能以尺寸成功替代视觉。现有decoding=async可在load后下一paint显示，审计仅补原生decode()与两帧后采图，不修改src/loading或网站产品。文件范围现有审计/4项helper回归/计划日志；生产192+14与新截图待精确head重验，不进main，无新用户问题。

UI-A08b in-progress：base30e26ead4ee97aa6bc3120aec3372897bb1285bc，run38663584681 build116190250811/deploy116192067722/live116192142932全部success已核对。最小范围tools/check_think_build_visual.py、封面审计回归、本计划日志；仅检查书籍目录当前viewport内img.pgl-cover，等待真实complete并记录naturalWidth/currentSrc，再截图；不改src/loading、不强制加载、不猜测修产品。四宽度双主题8加载场景，完整192+14及线上验证pending。搜索/筛选/分页等另项pending，先工作分支，无新用户问题。

UI-A08a限定done：验收main/base85980c7e95f2407bbfb9232fafaf5e8cf9f485b4 / run38657575079 build116170877784、deploy116172735660、verify-live-ui116172823721全部success。207 tests、4项Ruby、T01/authoring/production Jekyll/旧门禁与production/live192+14通过。下载live artifact11937374039，人工查看40张线上关系场景四联系表，放大390 Light弹层及768 Night友链焦点原图，16限定交互通过。部分目录封面在截图时尚未加载，完整图片加载专项保留pending，不当作已修复或视觉正常；仅回写计划/日志/公开证据，不改产品。新文档head CI单独核对；下一项UI-A08b优先补可见封面加载状态和Library搜索/筛选/分页，其他全站矩阵仍IN PROGRESS，无新待答问题。[证据](docs/ui-evidence/uia08a-checks.md)。

UI-A08a生产通过、待main/live：base main9809089372832f3d6ff7a499a85c48755da7208e；验收head d770c3565f03c537ef23273423b6ee98f139dcef / run38651914436 build116152939726 success，工作分支deploy/live skipped。207 tests、4项Ruby、T01/authoring/production Jekyll/旧门禁及192+14通过；下载artifact11935087411、人工查看40张关系场景截图四联系表并放大390 Light弹层和1024 Night友链焦点原图，未确认新产品缺陷。仅审计/计划日志与公开证据非强推main，保留同步数据；实际main head部署及live同场景仍validation-pending。全站IN PROGRESS，无新待答问题。[证据](docs/ui-evidence/uia08a-checks.md)。

UI-A08a接续 validation-pending：base main98090893、branch22b184d3；run38644349352 build116127411671 failure，deploy/live skipped。390 Night Library弹层/目录/返回已通过，友链焦点失败。下载artifact11931034197并实际看弹层、目录和友链失败截图，无新增确认产品缺陷；Element.send_keys每次先聚焦目标，原脚本对同一卡片发Shift+Tab实际移走焦点，不是全局反向Tab。仅改审计为ActionChains真实全局Tab遍历、Tab/Shift+Tab往返，保留严格activeElement断言，并补焦点tag/class/href诊断。范围审计/计划日志；192+14、四宽度两主题完整截图与线上仍pending，main不改，无新用户问题。

UI-A08a接续 validation-pending：branch7ca4df8a/run38636477276失败于390 Night目录打开后的返回click；已下载artifact11928481822查看目录截图/JSON，category=book、drawerOpen=false、scrollY161。原弹层与目录click已通过，pgl分类事件启动smooth scroll，返回点击可能在滚动中。只补返回按钮instant居中、两帧与viewport hit-test再真实click，截图在稳定视口记录，所有原断言保留。main新增9809089372832f3d6ff7a499a85c48755da7208e为9个Library同步数据文件，已无冲突合并进工作分支并原样保护；不回退同步。范围仍审计/计划日志，main不改、192+14与线上验收pending，无新用户问题。

UI-A08a接续 validation-pending：base maina5738952、branch57efc919，run38628620429 build116074140246失败于390 Night弹层关闭后目录click坐标y1621被拦截；此前207 tests/Ruby/T01/authoring/Jekyll/旧门禁通过。下载artifact11926170787查看失败截图，页面在首屏、弹层已闭；close事件异步恢复opener焦点可能与下次自动滚动竞争。本轮仅修审计：等待恢复焦点及两帧，再instant滚动目录、hit-test后真实click，补失败几何JSON，不放宽目录/弹层/URL断言，不猜测改产品。main未改，完整192+14和线上矩阵仍pending，无新用户问题。

UI-A08a in-progress：base a5738952dc9584e4e8282dbd5090bfe17992e2af，run38620953323 build/deploy/live全部success已核对。范围仅tools/check_think_build_visual.py、本计划/日志；Library根页/当前条目弹层/书籍目录返回、友链卡片href与键盘焦点，四宽度双主题16页面场景（总192+14）。云1363×936 Light已实际查看上述界面和操作弹层/目录，无新增确认缺陷，不改产品。时间线/高级筛选/分页/搜索与外部站点可用性另留pending；先ui/audit-008分支production，未验证不进main，无新用户问题。

UI-A07b done（限定两篇公开文章Copy link）：base/验收main aa3dbcec717bbbec27e02c0dd196fb0822a6fdec，[run38611417490](https://github.com/AplusNeutrino/My_Blog/actions/runs/38611417490) build116015462124、deploy116017753847、verify-live-ui116018039763全部success。207 tests、4项Ruby、T01/authoring/production Jekyll/旧门禁、production/live各176+14通过；16线上clipboardBytes=verified、sentinel已替换、copiedUrl精确等于当前https://neutriverse.uk URL。人工查看16复制反馈四联系表并放大四宽度代表原图，无新增确认缺陷。只回写计划/日志与公开证据，不改样式或内容；新证据文档提交CI另行核对。下一项Library/友链四宽度双主题目录/延迟加载/链接矩阵，全站IN PROGRESS，无新增用户问题。

UI-A07b生产通过、待main/live：base main536281728dcc314c71c64936b06334b2f74bb800，审计验收head e431aeaced355ccb155595fe912860a4007f59dd / run38604621533 build115992207806 success，分支deploy/live skipped。207 tests、4项Ruby、T01/authoring/Jekyll/旧门禁、176+14场景通过；16实际剪贴板内容精确等于当前URL，sentinel均替换。人工查看16复制反馈截图的四联系表并放大1366 Light代码原图，没有新确认缺陷。仅将已验证审计和[证据](docs/ui-evidence/uia07b-checks.md)非强推main，状态仍validation-pending；下一轮核对实际main head build/deploy/live与16线上复制记录/截图，不以localhost复制通过代替线上。其余矩阵IN PROGRESS，无新用户问题。

UI-A07b validation-pending：审计实现2892b031dc0e0de8493bbe03a7b10ce1a24620b9，本机207 tests/authoring/T01/diff通过，未冒称真实剪贴板或视觉验收。上一文档head536281728dcc314c71c64936b06334b2f74bb800的run38595958153重试build115988897946、deploy115988897534、live115989007513均success，部署恢复；首次超时历史保留。现在将实现和状态非强推保存ui/audit-007b，main不改，下一轮先核对其精确head生产CI与剪贴板16记录/截图，再决定main及live。无新增用户问题。

UI-A07b in-progress：base536281728dcc314c71c64936b06334b2f74bb800；范围仅tools/check_think_build_visual.py、必要审计回归、本UI计划/日志。补16公开阅读场景复制实际字节：浏览器测试origin授予clipboard读写权限，先写不等于URL的sentinel，真实点击原按钮，再读系统clipboard并严格等于当前完整URL，保留原成功提示和所有视觉/媒体门禁。未确认产品缺陷不改样式。先工作分支production，通过后main/live；没有把未运行的检查标done。上次文档run38595958153部署十分钟updating_pages超时，已重试失败jobs；同head重试deploy成功、live尚在运行，不暂停任务或修改部署超时阈值。无新用户问题。

UI-A07 done（限定代码/图片/媒体与复制提示）：验收main/base cd4ec29eb1ab500563b9247af7ae98ac1661438a，[run38590193242](https://github.com/AplusNeutrino/My_Blog/actions/runs/38590193242) build115942706728、deploy115945097313、verify-live-ui115945238565全部success。176+14线上检查通过，人工查看新增40张截图的四联系表并放大四宽度代表图，代码/图片/弹层无新增确认缺陷。本轮只回写计划/日志与公开live证据；正文/metadata/样式未改，旧COMPLETE历史不动。文档提交CI另行核对；UI-A07b剪贴板实际字节仍pending，下一项先核对文档head再补实际复制或Library/友链矩阵，全站IN PROGRESS。无新增用户问题。

UI-A07生产通过、待main/live：审计head2c60e4e1aeff6897447e6a0a90a65251869f547f / run38588924737 success；205 tests、4项Ruby、T01/authoring/Jekyll/旧门禁、176+14通过。新增16阅读场景、真实移动touch/桌面arrow/关闭及复制提示通过；人工看40张viewport/gallery/feedback联系表，放大代表原图，无新增确认产品缺陷。审计与[证据](docs/ui-evidence/uia07-checks.md)非强推main，精确head线上矩阵仍validation-pending；UI-A07b剪贴板实际字节pending，不以成功提示代替。下轮先核对main/live再继续复制实值/未检页面，无新增用户问题。

UI-A07（检查，不预设缺陷）：base c5b99ed2284ac327270de5c952f0a026d85d87b3，run38577189934 completed/success已核对。范围现有浏览器审计、计划/日志及公开证据；代表计组07plain代码、FF1公开图片，390/768/1024/1366×Night/Light，共16场景。验收代码/图片可见且不引起整页溢出、图片逐张lazy加载及弹层下一张/返回/关闭、复制链接反馈；剪贴板实际字节明确pending。候选高亮示例因hidden排除，不生成公开截图。桌面1363×936已看代码/图片并操作弹层翻页，没有新增确认缺陷，不猜测改产品。先ui/audit-007验证；本轮不改旧文章/metadata/URL/hidden/noindex。无新增待答问题。

UI-005 done：base/main5922412f7fc82af68984091e75c142242c290cec，[run38570020301](https://github.com/AplusNeutrino/My_Blog/actions/runs/38570020301) build115872459830、deploy115874598655、verify-live-ui115874783745均success。4项Ruby渲染回归、205 tests、T01/authoring/production Jekyll/全部旧门禁、生产与live各160+14通过。下载live artifact11898410699，看8张表格viewport联系表并放大四宽度代表图，1366 Light全页两表复核，行列恢复且横向阅读通过。只回写计划/日志/公开证据，本次没有额外产品修改；文档提交CI另行核对。下一项代码/图片/复制/媒体阅读场景，完整矩阵仍IN PROGRESS，无新增用户问题。[证据](docs/ui-evidence/ui005-comparison.md)。

UI-005生产通过，待main/live：实现head c20396fa62672943eda5d675955cc6eeb394d3ea，[run38569176497](https://github.com/AplusNeutrino/My_Blog/actions/runs/38569176497) build success；4项Ruby渲染回归、205 tests、T01/authoring/Jekyll/旧门禁、160+14浏览器矩阵通过。已查看8张表格截图并放大390 Light/1366 Night，真实横向滚动通过；没有更改旧md。准备非强推main并核对其实际head部署后同场景，UI-005保持validation-pending；[前后记录](docs/ui-evidence/ui005-comparison.md)。无新增待答问题，代码/图片阅读仍pending。

UI-005 / UI-A06：base9708457fee99f7a00d8d74bb13bf59d669687ad4，run38560753961 completed/success已核对。1363×936线上计组04 Light实际截图确认两张表格为pipe prose，DOM为0 table；原md有合法header/separator但紧邻ATX标题。最小范围：render-only post hook、Ruby渲染回归、现有CI与8场景表格截图/横向操作、计划日志；不改正文源/metadata、配置全局parser或其他页面设计。先ui/fix-005，生产与线上截图pending；完整代码/图片阅读检查仍pending。无新增用户问题。

UI-A05 done（限定检索页截图与已列交互）：base/main head f755f17c3e1f1a1b66eee714ef4b8ff8aec73cfb，[run38554989713](https://github.com/AplusNeutrino/My_Blog/actions/runs/38554989713) build/deploy/verify-live-ui全部success；205 tests、T01/authoring/production Jekyll/旧门禁、production与live各152+14通过。下载live artifact11890351589，人工查看32张检索viewport（四张分宽度联系表）及390 Light Tags、768 Night Thoughts、1024 Light Archive、1366 Night Series原图。未确认新产品缺陷，本次仅证据文档更新，不修改网站样式/内容；文档提交CI另行核对，不冒称其已通过。下一项代表文章代码/表格/图片阅读矩阵，Thought点赞等仍pending；全站IN PROGRESS，无新增待答问题。

UI-A05生产检查通过，等待main/线上复验：head f3d51b79f1b8e813fa7e94b4ebc2592772566277 / run38554138564 success；205 tests、保护/authoring/Jekyll/旧门禁、152场景+14侧栏专项通过。新增32检索截图与32组往返操作已核对，联系表人工查看；未确认新产品缺陷，没有改样式。将审计+证据非强推main，状态validation-pending。下一轮先核对本次main head的build/deploy/live152+14与截图，然后继续Thought其他交互/代表文章等矩阵。详见[UI-A05记录](docs/ui-evidence/uia05-checks.md)，无新增待答问题。

UI-A05本轮接续：base main93825c66 / branch2114197f，run38548101812失败诊断已取回；Archive打开post按既有规则存储侧栏collapsed，下一页主题按钮因此在inert侧栏。审计补真实召回按钮后再检查主题，不修改产品规则。先ui/audit-005精确head验收，32新检索截图与main/live仍pending；失败PNG/JSON来源artifact11884993704。

UI-A05检查进行中：base93825c66/run38541205915 success；Tags/Archive/Thoughts独立页+THINK内Series目录32双主题四宽度截图及往返操作。Tags桌面首屏与长标签详情跳转已实际检查，尚未确认新缺陷；不猜测改样式。工作分支新增检查pending，其他页面矩阵仍保留pending。

UI-A05工作分支ui/audit-005：6bcac453的Series hash预期失败已修正；6d0df28f生成95场景但主题按钮不可交互失败；诊断a38ff743/run38547751557在原mobile gate关闭动画中的pointer点击被topbar-title拦截，未进入新矩阵。补原gate点击前等待有限动画结束，焦点/真实click/所有断言不变。部分20张检索viewport联系表已看（390/768双主题+1024 Night），暂无新增确认产品缺陷；1366和1024 Light/完整生产及live矩阵pending。下轮先检出该工作分支精确head核对CI，不重做历史已done事项。

UI-004/UI-003a已验收：head8415050ddd200f51c471b84e0011e3d46260a305的[main run38540154437](https://github.com/AplusNeutrino/My_Blog/actions/runs/38540154437) build/deploy/verify-live-ui均success。205 tests、保护/authoring/Jekyll/原门禁、production120+14与live120+14通过；查看本次live14张联系表，放大1024×900 Light原图，侧栏检索/主题分开且可操作。live移动两宽度两主题各3次快速mask关闭及跨两帧焦点断言通过。证据artifact11882032589及永久JSON/联系表。上次live失败未隐藏；只稳定每次点击起点，仍保留快速open→mask操作。下一项独立检查Series/Tags/Archive/Thoughts四视口双主题；全站矩阵仍IN PROGRESS，无新增待答问题。

2026-10-14接续：base main787a4a61，run38535247898 build/deploy success，但verify-live-ui快速mask关闭焦点wait失败。UI-003a/UI-004仍validation-pending。本轮仅诊断/修正审计起始点击时序，补失败状态截图，不放宽断言、不推测改产品；下轮/本轮以修正后的精确head重新核对production+live。其他独立页矩阵未冒称完成。

UI-004接续：实现与审计head ba75465277be11c48c7f4242138842a88effc953，工作分支run38534716282 success；205 tests、T01/authoring/Jekyll/全部旧门禁、120场景与14短/高窗口专项通过。a93f494f在main的run38534120830因新脚本焦点/滚动时序失败，未部署；ba754652补等待焦点完成后滚动，没有放宽断言。将修复与此状态记录非强推提交main，UI-004/UI-003a均validation-pending；下轮先核对该main head的build/deploy/verify-live-ui和同场景截图，再继续独立页面矩阵。[前后证据](docs/ui-evidence/ui004-comparison.md)。无新增待答问题。

2026-10-14 UI-004：base 7d376af1f05329dca43861c47c4dde83ded20786，run38526904330 success已核对。先记录范围：共享侧栏CSS、短窗口几何/指针/截图回归、UI-003a快速mask关闭专项、计划日志。已查看上一head线上1024px BUILD Night截图确认重叠；桌面1363×936测量nav flex-shrink=1/min-height=0，其children不随压缩而缩小。保留组高度，让容器滚动，不改变内容/尺寸风格。先工作分支验证；尚未部署验收。

UI-003已部署并验收：实现head e020fb73e9de4fcd91732c2bc7e281575f3395af；[main run38526220139](https://github.com/AplusNeutrino/My_Blog/actions/runs/38526220139) build/deploy/verify-live-ui success。UI-003a保护代码已部署、原production菜单焦点门禁通过，但快速mask关闭的同场景线上焦点专项检查仍validation-pending（live矩阵只操作主题菜单/Escape，不冒称mask复验）。下一项优先UI-004，并补UI-003a线上专项；其他独立页面矩阵仍pending。无待答问题。[证据与局限](docs/ui-evidence/ui003-comparison.md)。

2026-10-14 UI-003接续：main仍c12d9d2a，ui/fix-003实际head e020fb73e9de4fcd91732c2bc7e281575f3395af，run38509991407 build success（deploy/live按工作分支规则skipped）。下载artifact11869786736，120项标题/控件/溢出/圆角/noindex与16组交互通过，人工查看32张viewport联系表。非强推main至同一head后run38526220139正在build/deploy/live验证；未标done。下一优先UI-004；全页截图侧栏裁切疑点被viewport/rect澄清，不修改其开闭transform。

2026-10-14 UI-003：base c12d9d2ac262e924ce800f7e303f59279a0e9741，run38506420729 success已核对。范围：topbar模板、必要溢出样式、回归与浏览器标题/控件/viewport截图证据、计划/日志。只修复自定义公开section/project布局的顶栏名称；其他布局保留Chirpy行为。先工作分支验收，再核对main部署。侧栏疑点只复核，不凭全页合成截图改样式。

2026-10-14 UI-002 / UI-A02：base = bc3efad53188f1ff86ae5b49d5a159a136643792；工作分支验证后main非强推至4d7eac959d1448cbdeb490aebf11e1a79a7b66d4；[run38505942304](https://github.com/AplusNeutrino/My_Blog/actions/runs/38505942304) build/deploy success，双主题线上复验通过，UI-002 done。[证据与局限](docs/ui-evidence/ui002-comparison.md)。下一项UI-003移动顶栏名称，先核实侧栏截图疑点；不将此局部审计当全站COMPLETE。无新增待答问题。

UI-001 done；base = dd2e52ee17322519190fdacf1a12e5d35f035ead；最终实现head = 0348b33c7e00a5f4584181c8d7244da88fc50244；[run38500122266](https://github.com/AplusNeutrino/My_Blog/actions/runs/38500122266) build/deploy成功；无待答问题。下一项：THINK筛选/分页/阅读区与BUILD列表/七详情全页视觉检查，继续补矩阵，不把导航截图当全站通过。

UI-001证据：[前后对照](docs/ui-evidence/ui001-comparison.md)，40项几何JSON与两主题线上截图持久保存。必要CI修复包含推荐预期模块/3项测试、viewport截图与CJK字体；内容/数据/URL未改。
