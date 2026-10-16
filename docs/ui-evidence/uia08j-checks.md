# UI-A08j — 默认书籍全分页与封面加载

状态：validation-pending；尚未运行本次精确实现head浏览器检查。

本机240 tests、authoring44/5/7、T01保护44/5/5、diff check通过；新增3项为接线回归，不是浏览器或视觉验收。本机无Ruby/Jekyll/Chrome，真实production和线上检查仍pending。

真实审计实现cf03a5ad663271603b50347c3cc9edc90f111d38已保存ui/audit-008j，5个上传blob与本地git hash-object完全一致；随后仅追加此SHA检查点。main仍325db4d0，未部署本次审计。应验收检查点后最终分支head的Actions和96图，不借base或其他head成功替代。

- base main：325db4d0771c3fd518d52ebf908e7d6b45962453。其run38944307535 build117119432424/deploy117122814466/live117122895755全部success，仅为base状态，不能替代本次验证。
- 优先级：剩余Library库存检查，非已确认产品缺陷；不猜测修改样式。当前公开默认书籍124条，24/页，共6页；动态计算，不锁死未来同步库存。
- 文件范围：tools/check_think_build_visual.py、tests/test_library_book_inventory_audit.py、本轮计划/日志/此证据。不改正文、metadata、旧URL、hidden/noindex、数据、关联仓库或旧COMPLETE历史。
- 条件/验收：390/768/1024/1366 × Night/Light，真实分类/下一页/上一页/返回控件；每页数量、ID唯一、跨页无重复且全体ID与公开默认书籍集合相同；末页刷新URL/ID保留，再上一页/返回根/重入首页恢复。
- 每卡真实滚动，不改src/loading、不注入数据或强制请求；记录原生complete/decode/自然尺寸、初始离屏几何与占位路径。各页首尾viewport截图，当前目标96张；中间卡片仅加载与几何断言，不称人工视觉通过。当前目标992次封面检查，不要求缓存未命中。
- production图必须人工看，再决定main；精确main Actions/build/deploy及线上同场景复验另行完成。失败保留真实证据，不放宽门禁。其他分类、书籍中间区域完整视觉及其余全站矩阵仍pending。
- gh未安装，遵循仓库仅gh Issue规范，不编造Issue；无新增用户决策。
