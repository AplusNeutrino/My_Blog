# UI-A08j — 默认书籍全分页与封面加载

状态：validation-pending；首次生产检查通过，但人工看图发现取景缺口，修正后需要新的精确head验证。

## 2026-10-17 — 首次生产检查与取景修正

- 精确head57a950674734cf0b8fc4b218534fa5425fcedf64 / [run38952889668](https://github.com/AplusNeutrino/My_Blog/actions/runs/38952889668)：build117148951098 success；deploy117153638838与verify-live-ui117153640466 skipped（工作分支，不作部署通过）。240 tests、4项Ruby渲染回归、T01/authoring44/5/7、production Jekyll、SEO/资源/既有门禁、192页面+14侧栏通过。
- artifact12069319714 /272044392 bytes /sha256:ef6db3f5f6bb6eee87c99902851970cf1f1c4593e579851fe90cc41c901d2be4，下载后独立匹配。人工查看96图的四联系表，并放大390 Light第1页首、768 Night第6页首原图。
- 8流程各124条/6页、每页24/24/24/24/24/4，992次封面complete/decode/自然尺寸、全体ID集合/无重复/末页刷新/上一页/重入与96几何诊断通过；没有据此确认新产品缺陷。
- **验收缺口**：前置Steam流程在刷新并清除筛选后留下open的高级筛选details，书籍各页首截图被其正常浮层遮住（包括768末页）。这是审计起始状态未隔离，不凭此将预期浮层判为产品缺陷，也不将CI成功写成视觉通过。
- 最小修正仅审计：进入书籍后若面板open，真实点击summary关闭并等待；每次capture另断言无open面板，再定位/截图。新增1接线回归，所有既有断言保留。不改产品/数据/旧正文/metadata/URL/hidden/noindex。
- 修正后本机241 tests、authoring44/5/7、T01保护44/5/5及diff通过；本机没有Ruby/Jekyll/Chrome，未将接线通过当视觉通过。
- 修正后96图、production精确head及main/live仍pending；main保持325db4d0，不合入未验收项，无新用户决策。中间卡片完整视觉、其他分类与全站矩阵仍pending。

首次取景联系表：[390](uia08j-production-contact-390.jpg)、[768](uia08j-production-contact-768.jpg)、[1024](uia08j-production-contact-1024.jpg)、[1366](uia08j-production-contact-1366.jpg)；[192审计](uia08j-production-audit.json)、[96诊断](uia08j-production-diagnostics.json)。仅保留真实历史，不冒充修正后视觉验收。原PNG保留在上述artifact14天。

本机240 tests、authoring44/5/7、T01保护44/5/5、diff check通过；新增3项为接线回归，不是浏览器或视觉验收。本机无Ruby/Jekyll/Chrome，真实production和线上检查仍pending。

真实审计实现cf03a5ad663271603b50347c3cc9edc90f111d38已保存ui/audit-008j，5个上传blob与本地git hash-object完全一致；随后仅追加此SHA检查点。main仍325db4d0，未部署本次审计。应验收检查点后最终分支head的Actions和96图，不借base或其他head成功替代。

- base main：325db4d0771c3fd518d52ebf908e7d6b45962453。其run38944307535 build117119432424/deploy117122814466/live117122895755全部success，仅为base状态，不能替代本次验证。
- 优先级：剩余Library库存检查，非已确认产品缺陷；不猜测修改样式。当前公开默认书籍124条，24/页，共6页；动态计算，不锁死未来同步库存。
- 文件范围：tools/check_think_build_visual.py、tests/test_library_book_inventory_audit.py、本轮计划/日志/此证据。不改正文、metadata、旧URL、hidden/noindex、数据、关联仓库或旧COMPLETE历史。
- 条件/验收：390/768/1024/1366 × Night/Light，真实分类/下一页/上一页/返回控件；每页数量、ID唯一、跨页无重复且全体ID与公开默认书籍集合相同；末页刷新URL/ID保留，再上一页/返回根/重入首页恢复。
- 每卡真实滚动，不改src/loading、不注入数据或强制请求；记录原生complete/decode/自然尺寸、初始离屏几何与占位路径。各页首尾viewport截图，当前目标96张；中间卡片仅加载与几何断言，不称人工视觉通过。当前目标992次封面检查，不要求缓存未命中。
- production图必须人工看，再决定main；精确main Actions/build/deploy及线上同场景复验另行完成。失败保留真实证据，不放宽门禁。其他分类、书籍中间区域完整视觉及其余全站矩阵仍pending。
- gh未安装，遵循仓库仅gh Issue规范，不编造Issue；无新增用户决策。
