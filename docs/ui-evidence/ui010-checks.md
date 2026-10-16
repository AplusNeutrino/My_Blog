# UI-010：评分末端提示被滚动条裁切

当前状态：done（精确main线上验收见末节）。下文复现/修复/生产阶段的pending为历史记录。2026-10-16实际复现；初始main `3d822d563af3b798a98887d3f35505496931d63c`，复现工作分支head `9d8d3c0869853fd69e4623c50b68ebf1607c8b12`。

复现：Library根页，390×844，Night或Prospero Light；切换全域，用Shift+Tab从全域按钮进入评分10端点。提示“10 · 4 条目”末尾被右侧滚动条裁切，影响完整读数，不是审美偏好。

![390 Light修复前](ui010-before-390-light.png)
![390 Night修复前](ui010-before-390-dark.png)

精确[run38858665322](https://github.com/AplusNeutrino/My_Blog/actions/runs/38858665322) build116836040776 success，deploy116838599413/live116838599804 skipped；229 tests、4 Ruby、T01/authoring/Jekyll/旧门禁与192+14通过，但实际截图否定视觉验收。artifact12029150207 /202758715 bytes，sha256 `83a90b333cd19a8782f7dd36bb0ba469c31860e1fa16410471d930423f1e94ca` 独立匹配。

人工看完整32张评分四状态图两联系表并放大390双主题末端。390 Light诊断tip.right=390.390625、document.scrollWidth=379、innerWidth=390；滚动条占去可用宽，旧几何按innerWidth含滚动条且容差1px误报通过。这是具体门禁缺口，不降低现有门槛。

根因：pgl.js与pgl-rating-polish.js两个既有renderer均只按分箱点百分比设置提示中心，未扣除提示半宽。最小修复显示提示并测量实际宽度，使用CSS clamp让中心在shell边缘内留8px；同时覆盖两个renderer，保留坐标/文本/主题/交互。浏览器审计新增documentElement.clientWidth与shell左右边界断言，原innerWidth、32图、8分类/摘要/真实键盘/刷新及192+14保留。

未修改数据、旧正文/metadata/URL/hidden/noindex或关联仓库。修复后新head production32图与main部署/live同场景尚未验收，保留ui/audit-008h，不合main；不将修复代码存在或单测通过当视觉正常。gh未安装，不创建或编造Issue；无新用户决策。

本地230 tests、authoring44/5/7、T01保护44/5/5及diff check通过；本机未运行Ruby/Jekyll/Chrome，等待新实现head的真实截图。

## 2026-10-16 修复后生产验收

验收head `c9d2280d4c139158371496798782933ac3c88bdd`，包含实际修复 `dc3454d778d628c60576ab5fa57dd9b416e9a4f1`；[run38864744419](https://github.com/AplusNeutrino/My_Blog/actions/runs/38864744419) build116855162216 success，deploy116857968018/verify-live-ui116857968151 skipped。230 tests、4 Ruby、T01/authoring/production Jekyll/旧门禁及192+14通过。分支成功不是部署成功。

artifact12031007024：203323040 bytes，sha256 `481775ceecbfc251fc4dd252573a5b7d76efec2f855b3ef358dd81e19d901033` 独立匹配。首次传输不足202510336 bytes，摘要与解压失败；续传完整后通过，未使用不完整证据。

已人工看32张390×844、768/1024/1366×900、Night/Prospero Light、book/music/tooltip-first/tooltip-last截图两联系表；放大390双主题末端、Night首端及1024 Light书籍原图。首末提示完整可读、未被滚动条裁切；音乐空图、书籍曲线和分类按钮保持。只验收具体修复，不由此推断全Library或全站正常。

| 390px末端提示 | 修复前right | 修复后right | 可用页宽 | shell.right |
|---|---|---|---|---|
| Light | 390.390625 | 355 | 379 | 363 |
| Night | 已截图确认裁切 | 350.9921875 | 375 | 359 |

8组当前数据八分类分箱/摘要、真实键盘首末端与退出隐藏、刷新默认全域通过；32诊断逐项通过clientWidth及shell左右边界和原溢出断言。不是用几何或单测代替人工看图。

- [390/768两主题四状态联系表](ui010-production-contact-390.jpg)
- [1024/1366两主题四状态联系表](ui010-production-contact-1024.jpg)
- [完整192 audit与交互记录](ui010-production-audit.json)
- [32评分几何诊断](ui010-production-rating.json)

生产验收通过后交付main；UI-010仍validation-pending，须核对新main精确head的Actions/build/deploy及线上同32图/8流程，不以此分支localhost证据当部署后复验。无新用户问题，其余全站矩阵仍pending；本轮不增加产品改动。

## 2026-10-16 精确main线上验收

验收main `41dca277eace9aa053bcb87e3cd21892b5ae6390`，包含实际修复 `dc3454d778d628c60576ab5fa57dd9b416e9a4f1`。[run38871666487](https://github.com/AplusNeutrino/My_Blog/actions/runs/38871666487) build116876943806、deploy116880022801、verify-live-ui116880240197全部success。230 tests、4 Ruby、T01保护/authoring44/5/7/production Jekyll/Search/feed/SEO/资源及production/live各192+14通过；线上job明确`UI_LIVE_BASE=https://neutriverse.uk`。

live artifact12033767964 /203043902 bytes，sha256 `39edaa4a63d2f035c1606cd398dc0da391823cd244faa4aa3ad547e46b9d596c` 独立匹配。已人工看32张四宽度双主题同四状态两联系表，放大390双主题末端、Night首端及1024 Light书籍原图。评分首末提示全文可读、不被滚动条裁切；390 Light末端right355/clientWidth379，Night350.9921875/clientWidth375，和生产相同。8组当前数据八分类/摘要/真实键盘首末提示/退出隐藏/刷新默认全域及32几何诊断全部通过，逐项与生产记录相同。

- [线上390/768四状态](ui010-live-contact-390.jpg)
- [线上1024/1366四状态](ui010-live-contact-1024.jpg)
- [线上完整192 audit与交互](ui010-live-audit.json)
- [线上32评分诊断](ui010-live-rating.json)

UI-010 done、UI-A08h评分限定done。另在1024 Light原图确认[UI-011目录计数被固定按钮遮挡](ui011-checks.md)，单独排队，不由评分通过推断全页正常。无新用户决策，完整库存/离屏加载、Steam及全站余项pending；本轮不追加产品改动，新证据文档head的CI另核对。
