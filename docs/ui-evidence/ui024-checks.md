# UI-024 — Atlas 加载态打开弹层未移入焦点

## 2026-10-20 当前main补齐线上限定验收：done

- 当前main/source3b68f4984477636b40bf58af2a8b8db3e2d466f1，[run39308494035](https://github.com/AplusNeutrino/My_Blog/actions/runs/39308494035) build118251656940/deploy118262207923/live118262473888全部success。初焦点app.js自004447db未改，现新head完整四宽度双主题线上8组通过，补齐此前1024/1366缺口；旧0044失败仍是失败，不改写历史。
- 线上58帧/8联系表全看、1024 Night与1366 Light loading-wrap放大：自然initial=date、明确disabled fixture的first=date/两首button disabled、Shift+Tab=aspectLinesToggle/inside/focusIsLast=true。16帧为UI fixture，不是自然服务/健康；真实Tab/Escape/重开/导航及小尺寸滚动通过。原audit/哈希/ZIP来源见[ui025-live/source.json](ui025-live/source.json)。
- 本轮云1363×936双主题自然已加载focus=refresh、Shift+Tab末south-node/Tab首/Escape返回trigger通过；本轮Night加载已在点击前完成，不冒称新云加载态图。明确复用此前同产品0044云自然加载focus=date证据，结合当前完整live矩阵关闭本缺陷pending。UI-A12其他业务/全站未完成，字体历史及未确定根因保留，不盲重跑或改门禁，无新用户决定。

## 2026-10-19 重跑失败与字体诊断

- 预记本轮base/main `004447dbdf2a8187c2cac9e7ab568709296ac8ab`，审计父`1ee05b3d9431a4bb1b925d38ae2a311b1db21c0d`，范围仅计划/日志/本记录及`ui024-live-retry-failure/`公开证据。无产品修改、无新确认UI缺陷或用户决策，gh不可用。
- [attempt2 live118021850681](https://github.com/AplusNeutrino/My_Blog/actions/runs/39234519303/job/118021850681)于2026-10-19 11:11:45 UTC failure。build118021851655/deploy118021853239是复用成功结果；不能把它们写成完整run成功。THINK/BUILD步骤在1366 Night think-all的settle line102等待document.fonts.ready异步30s超时，尚未执行本次Thought likes与OBSERVE，所以没有重跑Atlas图。首次失败是1024 Night Ravenis，二者分别保留。
- 本次artifact12181648252（366303644bytes）ZIP独立SHA256 `e9f2e7c9b6acd334262f366f924a4eb670fdf4629057e1844137b42b2580ea72`匹配。含2167文件，仅提取且实际查看scene-failure.png（1366×757）及解析scene-failure.json，其他2165文件未人工验收。画面中文、THINK标题与四入口可见，未确认新的显示缺陷，不能因可见而宣称字体门禁通过。
- 快照566字体面：123 loaded、4 loading、439 unloaded。loading均Noto Serif SC normal/display swap，400/600各两Unicode范围（详见原JSON）；FontFaceSet仍loading。采集到57条Font网络事件均finished，无pending/failed；这不保证日志完整对应每个加载面，不能据此断言CDN故障、缓存或Chrome内部根因。与旧UI-A09-F的Noto Sans SC快照不同，不混为同一个已知故障。
- 原30s/ready/失败阻断保持，不盲目第三次重跑，不换字体/禁缓存/删除门禁。UI024仍validation-pending，完整live受字体等待阻塞；先有可诊断复现方案再重新验证，旧云焦点及首轮28图仅显式复用。不把本轮失败诊断当四宽度视觉验收，也不将局部受阻扩大成全站无事可做。
- 原图、原JSON和summary来源/摘要永久保存`ui024-live-retry-failure/`，main不动；下一项UI-A12独立应用控件，另跟进字体等待证据。全站IN PROGRESS，不写最终报告或暂停。

## 2026-10-19 线上部分复验：仍 validation-pending

- 本轮base/main `004447dbdf2a8187c2cac9e7ab568709296ac8ab`，审计父`78446763f885148448df4b4278bbded533a8b046`。预定仅本记录/计划/日志及`ui024-live/`证据；无产品修改、无新用户决定、gh不可用未建Issue。
- [精确main run39234519303](https://github.com/AplusNeutrino/My_Blog/actions/runs/39234519303)：首轮build118000246276、deploy118008364191成功。279回归/T01/authoring/production Jekyll及原产物门禁通过不等于全站视觉正常。live118008468448于10:40:27 UTC失败：1024 Night Ravenis的document.fonts.ready异步30s超时，未进入该流程Atlas焦点断言。保留失败，不推断字体缺陷，不放宽等待或删门禁；仅失败job重跑一次。attempt2 build118021851655/deploy118021853239为复用成功结果，live118021850681仍运行，不称重跑全绿。
- 首轮live artifact12180635906（1382139bytes）ZIP SHA256 `72177d6a2d51437ba9de4df95339a661050da059b4aa43c166a7782ef24d02c6`独立核对匹配。实际逐张看390/768双主题28正常viewport（4联系表），初始时间焦点、Tab地点名和disabled UI fixture反向Tab末checkbox可见，标题未被共享导航遮挡。4流程passed/initialFocus与loadingInitialFocus=chartDateTime/loadingReverseTabWrapped=true；1024 Night无图失败，其余3流程未开始，不称8流程通过。16图fixture规则未改，本次28图中8图仍为明确disabled UI fixture，不是自然服务状态。
- 云Chrome1363×936双主题实际线上自然加载：稳定初始focus=datetime；加载后Escape关闭重开稳定focus=refresh。双主题Shift+Tab至最后south-node checkbox、Tab回refresh、Escape恢复trigger通过；Ravenis共享导航主题切换再回Atlas保持Night。资源app.js?v=40及noindex,nofollow核实，无网络mock/disabled改写。4云图本轮真实查看，未认证查询/导出/所有动态控件，也未在无溢出视口虚称滚动。
- 截图时序：Light initial画面仍加载中，紧接DOM时服务已完成；首次click同步观察在rAF前可见trigger，后续独立观察稳定datetime，与修复前两个稳定观察仍在trigger不同。Light loaded截图绘制仍停留refresh，虽当时AX/DOM已south-node，不把该帧当末checkbox可见证明；Night wrap帧真实显示south-node焦点。Night initial已加载画面仍保留首次datetime焦点。证据名称和对应时间不混用。
- `ui024-live/`永久保存4云原JPEG、4 CI联系表、audit与28源PNG SHA/尺寸summary；28原PNG在精确Actions artifact保留14天。修复前见ui024-before：trigger外遗留/Shift+Tab逃出，现自然加载及已加载重开均稳定入panel并可回环。1024/1366完整线上CI及全站其余矩阵pending；本轮只audit分支保存，不推main触发新CI，不关闭UI024/全站任务。

## main真实交付与待验收head

- 2026-10-19已按expected旧main=e44、force=false交付`004447dbdf2a8187c2cac9e7ab568709296ac8ab`；[main Actions39234519303](https://github.com/AplusNeutrino/My_Blog/actions/runs/39234519303)已创建，当前in_progress，尚不声称build/deploy/live成功。产品与已完整build验收的765c57a2相同，新增仅本轮文档/公开证据。
- UI024仍validation-pending，不能用工作分支success代替新main；下轮优先核对同一004447db的完整CI/部署/live，并实际复查加载态/已加载态焦点与Shift+Tab/Escape。此真实SHA/URL记录单独保存audit/ui-a12-focus，不再次推main取消部署。无新用户决策，全站IN PROGRESS。

## 2026-10-19 生产限定验收，准备main交付

- 最新main/base `e44fba12d6ddd0aba4b5252ddb265aa25ec45e70`，审计父`c8c886e7e89061b401678b27da1e070d5043421a`；精确实现`765c57a284173a47e75210ecf1e4932b712bd00b`/[run39228556141](https://github.com/AplusNeutrino/My_Blog/actions/runs/39228556141) build117980704074于09:37:03 UTC完整success。279 tests、T01、authoring、production Jekyll及原门禁全部通过。deploy117989980198/live117989979476按工作分支规则skipped，不等于已上线。
- artifact12176111372（3997064bytes）独立下载ZIP SHA256 `166c709895ae1f97738abd895439fd496e4a40323c6ad1762a71543bf108aece`匹配。本轮实际逐张看58正常viewport/8不缩放联系表，另放大1366 Light loading-wrap、390 Night open原PNG。首次打开时间控件有焦点、Tab后到地点名、反向Tab回环至末checkbox，标题及控件未见新遮挡或横溢出；从旧trigger外遗留/Shift+Tab逃出，变为弹层内可交互控件焦点。
- 8流程passed=true、initialFocus=chartDateTime、loadingInitialFocus=chartDateTime、loadingReverseTabWrapped=true；原层级故障注入/原生滚动/Tab/Escape返回/重开/导航往返/主题/侧栏收放保持。自然截图全部远端未加载，16张loading-focus/wrap为明确的可恢复disabled前两按钮UI fixture；不mock网络但不认证远端健康、不借此验证完整32选项或已加载时全部浏览器行为。Node覆盖loaded→refresh，线上同场景仍需复验。
- `ui024-production/`永久保存8张已看联系表、2放大原PNG、原audit.json、58源PNG哈希及尺寸summary；其余56原PNG留该head Actions artifact（14天）。旧失败及旧4张部分图不冒充本head验收；不下载/绕过超限总包。
- 交付前范围：以c8c886e为父仅新增上述公开证据和更新计划/日志/本记录，携既有最小focus修复/v40/必要回归与审计交付main；产品/样式/数据/门禁与精确765相同，无额外修复。expected main=e44、force=false，main若改变先停下重核，不覆盖用户修改。T01正文/URL/hidden、noindex/私密边界、七项目/外部仓库与旧COMPLETE保护保持。
- 本机重新跑279 tests、T01、authoring/diff；无本机Jekyll/Chrome，production来源仅上述精确CI。新main自身build/deploy/live及线上同场景仍validation-pending，UI024不标done、全站IN PROGRESS。gh不可用未编造Issue，无新增用户决策。下一项先核对新main精确head，再加载态/已加载态焦点/Shift+Tab/Escape复验。

## 最新状态：审计时序修订，仍validation-pending

- 首实现17a5aeb0/run39228088897 build117979204316回归/T01/authoring/production Build site成功，OBSERVE第7流程1366 Night侧栏展开动画后line138 click chartControlToggle被sky-command拦截(point45,204)，尚未进入该fixture焦点断言。整场failure，deploy/live skipped，不能标done。原失败历史保留，不推断新产品侧栏缺陷。
- 修订head `765c57a284173a47e75210ecf1e4932b712bd00b` / ui/fix-024，[run39228556141](https://github.com/AplusNeutrino/My_Blog/actions/runs/39228556141)运行中。只对原生click前增加有限10s实际中心点命中目标及非空矩形等待；不JS click/禁动画/放宽原焦点或层级断言，产品与17a5完全相同。修订后279 tests（2.664s）与diff通过；完整CI/新head截图/main部署仍待核对。
- 首轮部分artifact12175181738（3001524bytes），ZIP独立SHA256 `6a9d1887f0cd75d897488802341be98aca87740716cfbeb1a3c428d62c12e813`匹配。audit6流程390/768/1024双主题passed、initialFocus/loadingInitialFocus=chartDateTime、loadingReverseTabWrapped=true；1366 Night仅自然initialFocus=datetime，fixture未开始；1366 Light未开始，不称8流程完成。
- 仅人工查看390双主题loading-focus/loading-wrap共4张正常viewport原PNG，时间控件和末端checkbox焦点框可见，内部滚动位置保留；不是全部partial图片已看、不是线上。四图及原audit永久保存ui024-production-partial；其他图在精确artifact14天。不把UI fixture当自然加载或服务健康，未下载超限总包。
- main仍e44fba12，未交付半成品。旧audit/ui-a12-focus 8f4520dc的“Checkout运行中”为历史快照，以上覆盖当前状态。下一项优先核对765c57a2新run及四宽度双主题全部新图，再决定main交付，不重复UI023层级修改。

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

## 精确实现与后续核对

- 实现`17a5aeb0b538fb7337e3a2c0127d504b25085cf9`，分支`ui/fix-024`，[Actions39228088897](https://github.com/AplusNeutrino/My_Blog/actions/runs/39228088897)，build117979204316运行中（Checkout）。main仍e44fba12，不称实现已上线或分支deploy已通过。
- 修复前图SHA256分别`fbabbb08c04aa4fff0559653e535d02a756ce4438f66a90294598881017ae492`、`be1989fe884755acedd38b698800607afa424d00d45ade61b31291abca098985`。修复后CI图片尚未产生或人工查看，不虚构前后视觉验收。
- 本状态仅存不触发CI的audit/ui-a12-focus，不修改验证中的ui/fix-024，避免取消同head run。下轮先核对17a5aeb0的完整CI/专项42+16帧；新16帧为明确disabled UI fixture，不冒称自然加载或真实服务完整健康。验收通过再交付main并核对新main精确head。
