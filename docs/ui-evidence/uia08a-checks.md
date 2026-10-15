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
