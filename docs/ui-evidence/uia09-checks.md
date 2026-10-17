# UI-A09 — 首页、OBSERVE、ABOUT 原生纵向视口与往返

## 2026-10-18 剩余整页验收范围（先记录）

- Task UI-A09；base/验收main `8bff45a9e83f1598dd7d248e5aaeb8350d7a2889`，run39056732011 build117466109670/deploy117469225064/live117469268662全部success，关闭UI015证据head CI pending。UI012–015已分别限定done，不重复修改产品。
- 本轮最小范围：取此head首页/OBSERVE/ABOUT四宽度双主题24流程177原生线上滚动图，人工查看完整main（含此前四类遮挡作用域之外的区域）；对照既定真实滚轮、返回顶部、四入口/公开详情/Library/友链往返记录。先检查不预设新缺陷；若没有确认缺陷只记录，不凭偏好改样式。作者旧br空白/倒计时保留。
- 文件范围仅本UI计划/日志、本文件及uia09-final-live公开证据；现有审计/全部门禁不减，不改产品/正文/metadata/旧URL/hidden/noindex/数据/外部仓库/旧COMPLETE。gh不在PATH，准确记录而不编造Issue。其余THINK、阅读控件、应用、Library其他分类和Gate/NAVI矩阵不由此推断完成。
- 验收暂pending：独立artifact摘要核验、24流程177帧完整覆盖、逐张看联系表并放大必要原图、相关回归/T01/authoring及本次精确head Jekyll/产物；完成证据提交后核对该新head自己的CI。无新用户待决问题。

### 本次实际检查结果与优先队列变化

已下载live artifact12110591949并独立核验SHA256 `28855b85123470e7e0bf045a715dee673ec45ac59ebfffc2760e61cc6dd465be`；177原生帧/24流程完整，main覆盖、原生尺寸、无横向溢出/滚动偏移、真实返回顶部及公开往返原断言通过。人工只实际看前12联系表68帧（ABOUT1024/1366双主题、390 Night全17帧与390 Light前6帧）；其余109帧未验收。放大390 Night ABOUT第9原图确认UI016关系卡说明被按钮覆盖，转[UI016最小修复](ui016-checks.md)，A09整体不标done。第8时间线原图已看，所查位置没有确认遮挡；1366 Light引文滚动裁切仅疑点待原图核实，不算已确认缺陷。未看完的整页联系表留scratch，不提交冒充验收；永久保存UI016实际before PNG/JSON，完整原包在该head artifact保留14天。无新用户决策，不改旧br空白或倒计时。

随后已放大查看1366 Light ABOUT第8原生PNG：右侧引文完整、左边界与文字正常，联系表缩小引起的裁切疑点解除；未确认产品缺陷，不改样式。该额外原图不改变前述68帧覆盖计数（属已看联系表内帧）。

状态：validation-pending。base main53787e0bbe111da193918ee959e82780b58d87c3；精确run38997545484 build117293294892/deploy117295587015/live117295621809均success。旧UI-A08k限定done不重启。

## e437精确main线上限定验收（2026-10-17）

- 验收head e437b97d089359c47f8e83a691a3e9e43dbd2989 / [run39023453629](https://github.com/AplusNeutrino/My_Blog/actions/runs/39023453629)：build117369686142、deploy117372301121、verify-live-ui117372348023全部success；线上日志目标https://neutriverse.uk。252 tests/4 Ruby/T01/authoring/Jekyll/Search/feed/SEO/资源/旧门禁以及production/live各192+14和24public通过。
- live artifact12098546289 /492553783 bytes /sha256:692e9aef49140ca36f32e04be63c6309fe3553f46665712872186d889cdacb2d下载后独立匹配。全三页177帧已生成、24流程完成；本轮人工只验收首页八流程56帧的10联系表（uia09-live-home-contacts/）及放大390 Night近期第4帧、768 Night精选第5帧原图，不冒称全部177线上图已人工验收。24流程/177帧摘要永久存uia09-live-summary.json；完整原图/JSON留精确artifact14天。
- UI012/013线上旧位置不再被按钮盖住，中文/长标题/摘要换行可读，卡片外框/列数/双主题气质保持；八流程main完整覆盖、无横向溢出、所有近期/精选真实文本行与可见按钮无交集、真实返回顶部及四入口点击返回通过。本两项done，原问题图与线上修复图均保留。
- 字体阻塞在此main production/live均未复现，原等待/时限未放宽；仍不声明旧网络/浏览器内部根因已被产品修改修好。A09整体仍validation-pending：OBSERVE/ABOUT UI014待修且本轮其余线上图未全部人工看，全站余项不扩写done。无新确认缺陷/用户决策，gh未安装不编造Issue。

## d50精确生产验收与新问题（2026-10-17）

- head d50f1bc9dcf67606d8029468c5f9248fcc1d0234 / [run39019844860](https://github.com/AplusNeutrino/My_Blog/actions/runs/39019844860)，build117359307157 success，deploy117362280180/live117362280399 skipped（工作分支）。252 tests/4 Ruby/T01/authoring/production Jekyll/Search/feed/SEO/资源及所有既有门禁通过；主192/侧栏14、新public24/24完整通过，177张原生滚动PNG。不是部署后验收。
- artifact12096771963 /490940794 bytes /sha256:21850691c43288e3347f35ce8a83342e45c88eb6a92f9e13fb6debd1390317a7下载独立匹配。四宽度双主题三页177帧的36联系表全部实际看，另放大390 Night首页第4帧、768 Night首页第5帧、390 Light OBSERVE第2帧、390 Night ABOUT第3/11帧原图。联系表永久存uia09-production-contacts/，24流程/177帧几何与交互摘要存uia09-production-summary.json；原完整JSON/PNG在精确artifact保留14天。
- UI-012/013：首页近期表达/精选卡片全文与固定按钮无交集，原场景确已避让；中文换行、外框/两列布局和真实返回顶部/首页四入口往返通过。此两项生产限定验收可独立交付；新main自身build/deploy/live仍pending，不标done。
- 新确认UI-014/P2：[OBSERVE390 Light原图](ui014-before-observe-390-light.png)说明段“数据流…”右端、[ABOUT390 Night原图](ui014-before-about-390-dark.png)介绍段“并…”右端被固定按钮遮挡。普通说明文字与近期表达/精选不同作用域，原home Range门禁不覆盖，不将CI成功当视觉正常。列下一最小独立组，待定位/逐行交集回归，不扩大为全站重设计；其他宽度/主题不提前宣称确认。
- ABOUT末端多屏空白实际看见；源码_tabs/about.md显式保留大量br及倒计时，当前无意外缺陷证据，按旧作者内容保留而非偏好删除，不新增用户问题或公开隐藏入口。ABOUT部分其他文字/日期靠近按钮，未逐项确认的不计缺陷。
- 字体阻塞本次未复现，原ready/30s及动画门禁不变；启用性能日志后一次成功不能证明网络/浏览器内部根因已修好，不改产品字体，失败历史和诊断保留，main/live若再现继续pending。gh未安装不编造Issue，无新用户决策。A09采证已完成，但OBSERVE/ABOUT视觉仍受UI-014影响，不标三页整体done。

## 563d字体状态定位（2026-10-17）

精确563d054f5c975eca6aaaa583edee18910bdc09de / [run39015972699](https://github.com/AplusNeutrino/My_Blog/actions/runs/39015972699)：build117348035702 failure，deploy117349896137/live117349895961 skipped。250 tests/4 Ruby/T01/authoring/Jekyll/前置门禁通过，主144/192、新public18/24、139滚动帧、侧栏0。artifact12095147120 /331569201 bytes /sha256:31a16316b1663752bcac01ad731beec225b490129d3c6d66dfb94538357473dc独立匹配。失败原图及768 Night精选/390 Night近期原场景实际看，遮挡已避让但139图未全验收。失败FontFaceSet loading，Noto Sans SC400/500/600三个面loading，其余128 loaded/435 unloaded；不能将未使用unloaded当失败。仅补Unicode/Font网络请求事件诊断，原字体ready/30s/动画门禁不变，详见[uia09-font-wait-checks.md](uia09-font-wait-checks.md)。无产品追加改动，main仍53787e0b，完整production/main/live pending。

## d91精确生产首次失败与同head重试（2026-10-17）

接续：attempt2 build117337553687 failure，deploy117339610923/live117339611045 skipped，同一1366 Night THINK document.fonts.ready约30s脚本超时。artifact12093428361 /331496554 bytes /sha256:022d4f9e84169d80fe447afac180acb12dc7e9b64f4c05404b63780e20f46aab独立匹配；主144、新public18、139帧、侧栏0。本次失败原图已看，未看完139图，不称验收。现增加字体状态/FontFace/字体资源失败诊断，原等待/时限/失败重抛不变；UI-013另按先记录的最小范围修复并扩展文字交集门禁，见ui013-checks.md。新head production/完整视觉/main/live保持pending，不用旧main成功替代。

永久代表原图：[UI-013实际遮挡](ui013-before-home-768-dark.png)、[UI-012原场景局部生产复查](ui012-production-partial-home-390-dark.png)。后者仅partial，不代表完整验收或已部署。

- head d91bd7217515eb3edfad65951b7e958af2182218 / [run39008835671](https://github.com/AplusNeutrino/My_Blog/actions/runs/39008835671)，首次build117326775861 failure，deploy117329051203/live117329051171 skipped。248 tests/4 Ruby/T01/authoring/Jekyll/SEO/资源通过，主144/192、新public18/24、139原生滚动图，sidebar0。
- [artifact12092431014](https://github.com/AplusNeutrino/My_Blog/actions/runs/39008835671/artifacts/12092431014)，331640994 bytes，独立sha256:e0412461f80d5330b9003358ee9e35b76aa1d1676dfc0a2a841adb3f39e5fb8f。scene-failure.png/json对应1366 Night THINK；字体就绪document.fonts.ready脚本超时约30秒，没有字体诊断不能断言根因。截图已看，内容可见不等于门禁通过。
- 已看六组首页联系表及390 Night3/4、390 Light4、768/1024 Night5原图。近期表达六组Range无交集，390 Z.A.T.O.旧场景无遮挡；没有验收全部139图、1366或线上。768 Night第5帧确认UI-013精选内容正文被按钮遮挡，列独立最小队列；其余主题/尺寸待检，不凭推测改CSS。
- 已触发同head失败job重试，attempt2 build117337553687运行中，所有等待/时限/门禁原样。不移动ui/audit-009/main以免取消重试；本记录另存verification/ui-a09-d91-retry。下一轮先核对同head结果；完整production/main/live仍pending，无新用户决策。

## 范围先记录（2026-10-17）

## 2026-10-17 — 定位返回悬停过渡阻塞；UI-012最小修复待验

- 精确37fa1d786d415388edd7d0559a08cdfda5112ea5 / [run39004907637](https://github.com/AplusNeutrino/My_Blog/actions/runs/39004907637)：build117315276681 failure，deploy117317704915/live117317705669 skipped。246 tests/4 Ruby/T01/authoring/Jekyll/SEO/资源与既有主192场景通过；新public完成21/24，生成162滚动帧，侧栏0完成。没有人工验收全部162图，不当成完整通过。
- artifact12090578680 /485643590 bytes /sha256:7148d9cb1248a08ed9287fb84e3d514564c4df664a9a2fca75ea6938f29de708独立匹配。[失败诊断](uia09-return-stalled-1366-light.json)/[原生PNG](uia09-return-stalled-1366-light.png)入库；原图已人工看，1366 Light返回OBSERVE入口处没有内容消失，但有限动画等待未完成，不能因画面正常放行。
- 阻塞对象为返回入口background-color过渡，duration180/iterations1/state running/currentTime0/startTime null。永久装饰旋转为Infinity，不是原等待的阻塞项。浏览器内部停滞机制仍不作未证实推断；本次真实指针移出悬停后再走同一settle，保留失败重抛与快照，不取消动画或删等待。
- 同时按先记录的[UI-012最小范围](ui012-checks.md)为首页近期表达预留按钮避让内边距，新增逐行Range/按钮不相交严格门禁。248 tests/authoring/T01/diff本机通过；新精确head production/全部24流程截图/人工视觉及main/live仍pending，main保持53787e0b，不冒称已修复部署。无新用户决策，gh不可用不编造Issue。

## 2026-10-17 — 首次失败与UI-012新复现

- 精确head8831153b2e190a312628e8e3c9ca808d0403bea4 / [run39001620617](https://github.com/AplusNeutrino/My_Blog/actions/runs/39001620617)：build117305564644 failure，deploy117306200350/live117306198823 skipped。245 tests、4 Ruby渲染回归、T01/authoring/Jekyll/SEO/资源及前置门禁通过；主审计仅完成390 Night的24场景，新public流程0完成、侧栏0完成，不能写成完整192+14或三页24流程通过。
- artifact12089466875 /43173706 bytes /sha256:030926de45ef3cb4061b051e41a5111ef6f8c5004083514f9ba5dd55fd4fd9d0下载后独立匹配。保留[部分主审计](uia09-first-production-audit.json)、[9帧诊断](uia09-first-production-partial-diagnostics.json)、[9帧联系表](uia09-first-production-partial-home-390-dark.jpg)，原包保留14天。已人工看9帧联系表并放大第3帧原始PNG，不将部分截图当验收。
- 已确认产品缺陷UI-012/P2：[390 Night首页第3帧原图](ui012-before-home-390-dark.png)，返回顶部按钮覆盖近期表达中Z.A.T.O.卡片正文首行右端。证据是实际生产原生viewport，不是单凭DOM推测；类似其他页面已有避让修复，但本轮尚未定位/修改首页CSS根因。优先队列转UI-012，需保留双主题气质，以最小范围避让并补真实文字行与按钮交集回归；Light/其余尺寸尚未确认，不扩张为全站 redesign。
- 同一run另在public_page_sweep点击入口→浏览器返回→settle的有限动画等待（line80）超时。该位置确定，但没有失败时动画列表/截图，不能断言BFCache或某个动画为根因，更不能把它等同UI-012。云1363×936 Light真实首页→THINK→返回成功；云read-only页面接口不提供getAnimations，因此不能替代CI诊断。
- 本次仅补新public返回流程失败时的原生PNG、URL/主题/scroll/焦点、动画name/state/currentTime/startTime/timing/computedTiming与目标诊断，并重新抛出原失败；原settle等待/时限/几何/覆盖/导航门禁不放宽。新增1接线回归；修正留工作分支，main仍53787e0b，未部署本项。先精确新head诊断及UI-012最小修复/生产截图，main/live仍validation-pending，无新用户决策，gh未安装不编造Issue。

### 原范围记录（保留）

本次本机246 tests、authoring44/5/7、T01保护44/5/5及diff check通过；只证明回归/保护与诊断接线，不证明动画根因、UI-012修复或新浏览器视觉通过。

真实诊断实现c56bdf21a0c56be95e229e261b8fa344d87b0605，9个上传blob与本地hash逐项一致；随后仅追加SHA检查点。最终工作分支head CI需独立核对，未更新main。

- 当前矩阵这三页缺全页原生滚动视觉与对应往返；不是用户报告的新缺陷。本轮新增审计，不凭推测改产品或把偏好当缺陷。
- 条件：390/768/1024/1366×Night/Prospero Light，三页24流程。沿页面真实滚轮滚动，以重叠的原生viewport PNG覆盖main从顶部到底部，记录scrollY/clientWidth/viewport/topbar与覆盖区间；动态截图数量，不用超视口CDP裁图冒充原生画面。既有192+14及所有专项门禁保留，新增首页/ABOUT场景，不删除既有OBSERVE。
- 有界往返：首页四入口；OBSERVE两公开项目详情（不提前宣称应用共享导航通过）；ABOUT的Library和友链。均真实点击/浏览器返回核对原URL，末端真实返回顶部检查。私有旅行/Gate/NAVI入口、应用业务与外部站点不进入新增公开采证。
- 云1363×936首页Light首屏截图实际看过，长标题/中文摘要可见；真实向下滚动已操作，尚不足四宽度/全页验收，无新确认产品缺陷。本机无Chrome/Jekyll，交由工作分支精确CI生产截图后逐张看；未通过前不交付main。
- 文件范围：tools/check_think_build_visual.py、必要审计接线回归、本轮UI计划/日志与uia09公开证据。无产品/样式/同步数据/原文/metadata/旧URL/hidden/noindex、外部仓库或旧COMPLETE修改。gh未安装不编造Issue，无新用户决策。

## 实现与待验收

- 真实审计实现e571673dfe0b1abe46a22bc81019c13d96c7fda0，5个上传blob与本地git hash-object逐项相同；随后仅追加此SHA检查点，最终分支head须单独核对Actions。main保持53787e0b，未部署本项，不以本机测试或旧main成功替代新24流程真实截图。

- 在既有192场景后、每个主题/宽度内另加三页共24流程，写public-page-audit.json；既有SCENARIOS/192主审计/14侧栏及专项不减。每页真实滚轮分段，以160px余量重叠；逐帧校验原生PNG实际尺寸、clientWidth无溢出、main覆盖无断档，最多80帧未完成会失败，不接受部分覆盖。
- 末端scrollY>50时真实点击返回顶部；内容已完整处于短视口、没有有效返回顶部状态时明确backToTopNotRequired，不伪造点击。首页四入口、OBSERVE两公开项目详情、ABOUT Library/友链真实点击并浏览器返回核对原URL，不进入隐藏边界或应用业务。
- 新增2项接线回归（不是视觉验收）；本机245 tests、authoring44/5/7、T01保护44/5/5、diff通过。云1363×936 Light首页首屏与中部实际看并滚动，尚无确认缺陷；其他尺寸、三页连续截图与新head production Jekyll/Chrome/main/live仍validation-pending。main不动，先工作分支ui/audit-009，不用旧head CI代替本次结果。
