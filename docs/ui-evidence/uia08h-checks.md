# UI-A08h：Library 评分控件

状态：validation-pending。Base main `3d822d563af3b798a98887d3f35505496931d63c`。仅浏览器审计/回归/证据，不改产品或数据，未确认新显示缺陷。

2026-10-16云Chrome1363×936 Prospero Light实际操作书籍与音乐分类：书籍21个已评分作品、均值7.5、峰值7；音乐0项并显示水平零线。数目只为当前观察，不硬编码未来同步。Shift+Tab从全域按钮进入末端点，真实activeElement为评分10 circle，提示“10 · 0 条目”显示在viewport内。

![线上评分键盘末端提示](uia08h-tooltip-1363-light.jpg)

新增Selenium审计四宽度双主题八分类切换，逐项对照当前仓库stats分布核对十个分箱、摘要总数/均值/峰值及单一active分类；非空书籍/音乐状态、键盘首末端提示共32张截图与几何JSON。通过真实Shift+Tab/Tab遍历首末端与退出隐藏，不调用focus/dispatchEvent伪造；刷新按既有非URL控件契约恢复默认全域，不擅自增加持久化功能。保留192+14及全部门禁。

本地228 tests、authoring44/5/7、T01保护44/5/5、diff check通过。云真实Tab从末端点退出到全域按钮后tooltip.hidden=true。

Production32图、8流程、main部署/live同场景尚未验收，先ui/audit-008h，不合main；不把接线单测当视觉通过。本机未运行Ruby/Jekyll/Chrome。完整库存/离屏加载、Steam与其他全站项仍pending，无新用户决策；gh未安装，不编造Issue。

## 2026-10-16 首轮CI失败与审计修复

验收head `fb511faf9d364e9907f07ee71958d9547d996532`，[run38854460953](https://github.com/AplusNeutrino/My_Blog/actions/runs/38854460953) build116822998597 failure；deploy116823893916/live116823894777 skipped。228 tests、4 Ruby、T01/authoring/Jekyll及既有导航门禁通过，但扩展192场景未完成，不作全矩阵通过。

失败点是评分整页刷新后的verify(all)逐节点读取SVG aria-label时异步重绘，触发StaleElementReferenceException；现有pgl.js与pgl-rating-polish.js会先后替换SVG子节点。此证据支持“审计读取竞争”，不是产品显示缺陷，不改产品renderer。

下载失败artifact12026791958 /54244746 bytes，sha256 `beb9aa59f0a97c444bbd6846c0af1af71f9ae0d7e5c68a1f3decba39f5c37c8e` 独立匹配。实际只生成12张评分图（390双主题/768 Night）。人工放大390 Light首末端提示、768 Night书籍图，不能据此宣称32图/8流程完整通过；原图仍在该artifact，不复制为已验收证据。

审计改为一次execute_script返回同一帧分箱/坐标标签/area/active/摘要的纯值快照，再保留全部原有严格断言；真实分类点击、Shift+Tab/Tab、刷新、截图及几何检查不变，不忽略异常或放宽门禁。新head仍须production完整32图/8流程及main/live，validation-pending。

本次审计修复本地229 tests、authoring44/5/7、T01保护44/5/5及diff通过；新增测试仅验证读取契约，不代替Chrome/视觉验收。本机未执行Ruby/Jekyll/Chrome。
