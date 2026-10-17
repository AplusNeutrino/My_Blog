# UI-A09 — 首页、OBSERVE、ABOUT 原生纵向视口与往返

状态：validation-pending。base main53787e0bbe111da193918ee959e82780b58d87c3；精确run38997545484 build117293294892/deploy117295587015/live117295621809均success。旧UI-A08k限定done不重启。

## 范围先记录（2026-10-17）

- 当前矩阵这三页缺全页原生滚动视觉与对应往返；不是用户报告的新缺陷。本轮新增审计，不凭推测改产品或把偏好当缺陷。
- 条件：390/768/1024/1366×Night/Prospero Light，三页24流程。沿页面真实滚轮滚动，以重叠的原生viewport PNG覆盖main从顶部到底部，记录scrollY/clientWidth/viewport/topbar与覆盖区间；动态截图数量，不用超视口CDP裁图冒充原生画面。既有192+14及所有专项门禁保留，新增首页/ABOUT场景，不删除既有OBSERVE。
- 有界往返：首页四入口；OBSERVE两公开项目详情（不提前宣称应用共享导航通过）；ABOUT的Library和友链。均真实点击/浏览器返回核对原URL，末端真实返回顶部检查。私有旅行/Gate/NAVI入口、应用业务与外部站点不进入新增公开采证。
- 云1363×936首页Light首屏截图实际看过，长标题/中文摘要可见；真实向下滚动已操作，尚不足四宽度/全页验收，无新确认产品缺陷。本机无Chrome/Jekyll，交由工作分支精确CI生产截图后逐张看；未通过前不交付main。
- 文件范围：tools/check_think_build_visual.py、必要审计接线回归、本轮UI计划/日志与uia09公开证据。无产品/样式/同步数据/原文/metadata/旧URL/hidden/noindex、外部仓库或旧COMPLETE修改。gh未安装不编造Issue，无新用户决策。

## 实现与待验收

- 在既有192场景后、每个主题/宽度内另加三页共24流程，写public-page-audit.json；既有SCENARIOS/192主审计/14侧栏及专项不减。每页真实滚轮分段，以160px余量重叠；逐帧校验原生PNG实际尺寸、clientWidth无溢出、main覆盖无断档，最多80帧未完成会失败，不接受部分覆盖。
- 末端scrollY>50时真实点击返回顶部；内容已完整处于短视口、没有有效返回顶部状态时明确backToTopNotRequired，不伪造点击。首页四入口、OBSERVE两公开项目详情、ABOUT Library/友链真实点击并浏览器返回核对原URL，不进入隐藏边界或应用业务。
- 新增2项接线回归（不是视觉验收）；本机245 tests、authoring44/5/7、T01保护44/5/5、diff通过。云1363×936 Light首页首屏与中部实际看并滚动，尚无确认缺陷；其他尺寸、三页连续截图与新head production Jekyll/Chrome/main/live仍validation-pending。main不动，先工作分支ui/audit-009，不用旧head CI代替本次结果。
