# UI-A08a Library／友链有限生产检查

生产验收head `d770c3565f03c537ef23273423b6ee98f139dcef`，[Actions38651914436](https://github.com/AplusNeutrino/My_Blog/actions/runs/38651914436) build116152939726 success。分支deploy/live skipped；线上验收尚未完成。

限定范围：390/768/1024/1366px × Night/Prospero Light，Library根页、当前条目弹层开闭、书籍目录打开和返回；友链页、href存在、真实全局Tab自然到达卡片并Tab/Shift+Tab返回。共16关系场景，加入原矩阵后为192页面+14侧栏专项。207 Python tests、4项Ruby、T01/authoring/production Jekyll/旧门禁通过。没有JS focus/click或外部网站访问。

已人工查看40张实际Chrome viewport、drawer、category、friend focus图的四联系表，并放大390 Light弹层及1024 Night友链焦点原图。关闭按钮/标题/中文换行/来源按钮可见、卡片及焦点正常，没有新增确认产品缺陷，不猜测改样式。390 Night根页个别封面尚未加载；完整延迟加载、时间线、搜索、高级筛选、分页与外部目的地明确pending。

- [完整生产JSON](uia08a-production-audit.json)
- [390双主题](uia08a-production-contact-390.jpg)
- [768双主题](uia08a-production-contact-768.jpg)
- [1024双主题](uia08a-production-contact-1024.jpg)
- [1366双主题](uia08a-production-contact-1366.jpg)

来源artifact11935087411，sha256:cca44ac135a726db1b5492eae2842763494924bcbce7bd3e89f72725014d3579；原PNG保留14天，JSON/联系表永久入库。截图是localhost production，不替代部署后截图。UI-A08a仍validation-pending；main交付后核对精确head部署与live相同场景，旧COMPLETE历史不改，无新待答问题。

## 2026-10-15 线上复验：限定done

验收main `85980c7e95f2407bbfb9232fafaf5e8cf9f485b4`，[run38657575079](https://github.com/AplusNeutrino/My_Blog/actions/runs/38657575079) build116170877784、deploy116172735660、verify-live-ui116172823721全部success。207 tests、4项Ruby、T01/authoring/Jekyll/旧门禁与production/live各192+14通过；16关系场景的弹层/目录返回与友链键盘往返通过。

人工查看40张实际线上截图四联系表，放大390 Light弹层与768 Night友链焦点原图，限定布局/控件没有新增确认缺陷。部分目录封面在截图时尚未加载，不能证明完整图片加载正常或确认失败；UI-A08b需在真实浏览器等待/记录complete、naturalWidth和错误后截图复查，不猜测改样式。时间线/搜索/高级筛选/分页、外部目的地仍pending。

- [完整live JSON](uia08a-live-audit.json)
- [390双主题](uia08a-live-contact-390.jpg)
- [768双主题](uia08a-live-contact-768.jpg)
- [1024双主题](uia08a-live-contact-1024.jpg)
- [1366双主题](uia08a-live-contact-1366.jpg)

来源live artifact11937374039，sha256:141adf7ebbb3828ff951b70a66b4f169d2506836fabf5bf08c127e783ea38965，原PNG保留14天。此限定done不代表全Library或全站COMPLETE；仅保存公开证据，不改产品、旧内容或隐蔽边界。
