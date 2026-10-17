# UI-A09-F — 生产字体等待阻塞定位

状态：validation-pending。2026-10-17先记录范围。

- base main53787e0bbe111da193918ee959e82780b58d87c3不动，工作head563d054f5c975eca6aaaa583edee18910bdc09de；run39015972699 build117348035702 failure，deploy117349896137/live117349895961 skipped。250 tests/4 Ruby/T01/authoring/Jekyll/SEO/资源及前置门禁通过；主144/192、新public18/24、139原生滚动帧、侧栏0。不能当完整通过。
- artifact12095147120 /331569201 bytes /sha256:31a16316b1663752bcac01ad731beec225b490129d3c6d66dfb94538357473dc独立匹配。失败原生PNG已实际看，1366 Night THINK内容可见；实际看768 Night精选第5帧与390 Night近期第4帧，UI-013/012原位置已避让，但其余139图未全部人工验收，main/live仍pending。
- 事实：document.readyState complete、mode dark、FontFaceSet loading，566个字体面中128 loaded、435 unloaded（未使用不等于失败）、3 loading；后者均Noto Sans SC，normal，weight400/500/600，display swap。51个已完成字体资源时序没有指出未完成请求。不能据此断言整个字体损坏、CDN故障或浏览器内部机制。
- 本轮范围只tools/check_think_build_visual.py、必要接线回归、本轮计划日志及公开诊断证据；不再改产品CSS/字体/内容/数据/URL/metadata/hidden/noindex，不动外部仓库/旧COMPLETE。gh未安装不编造Issue，无新用户决策。
- 拟增加失败时Unicode范围及字体网络请求/响应/完成/失败事件，辨别分片与请求状态；仅采集Font资源，不输出页面其他请求。原document.fonts.ready等待、30s脚本时限、有限动画门禁及192+14/24新流程保持，不取消加载、不吞失败、不启用替代字体。保存新head在工作分支，实际新CI/production/截图/main/live未验收前不交付main。

## 本轮实现（待精确新head验证）

- 保存[原失败字体状态](uia09-font-stalled-1366-dark.json)和[UI-013部分生产原图](ui013-production-partial-home-768-dark.png)，后者原遮挡位置文字已避让；并非四宽度双主题完整验收或线上证据。
- Chrome性能日志只用于诊断，启用Network事件、不启用Page事件，不改变网络缓存/浏览器版本或字体。每个主场景导航前清空旧日志以限定当前导航且控制内存；失败时只保存Font请求URL/ID/时间/状态/协议/缓存标记及完成/失败原因，不输出headers和其他请求。诊断失败另记错误，原始settle异常仍raise。
- FontFace快照新增unicodeRange，原fontSetStatus/资源时序保留。没有产品改动、延时重试或跳过ready；尚未证明具体CDN/分片根因。两项新增回归实际执行纯事件解析，验证finished/failed/pending及非Font/headers排除，并约束原30s/ready/raise接线；不是浏览器视觉验收。
- 本机252 tests、authoring44/5/7、T01保护44/5/5、diff check通过。无本机Ruby/Jekyll/Chrome；精确新head CI/字体根因/完整production截图/main/live仍validation-pending。下一轮先核对同head诊断，不盲改样式或用旧CI通过替代。
