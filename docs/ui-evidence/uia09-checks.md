# UI-A09 — 首页、OBSERVE、ABOUT 原生纵向视口与往返

状态：validation-pending。base main53787e0bbe111da193918ee959e82780b58d87c3；精确run38997545484 build117293294892/deploy117295587015/live117295621809均success。旧UI-A08k限定done不重启。

## 范围先记录（2026-10-17）

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
