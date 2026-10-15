# UI-009 窄屏时间线文字被固定按钮遮住

状态：validation-pending。
Base main2e3d2844af408504cb616b9596ea682c97c3edd0，复现验收head47b3c294711c77abb62b321f71f5ae1eb658f855。
[run38765012413](https://github.com/AplusNeutrino/My_Blog/actions/runs/38765012413) build116526426682 success，分支deploy116529172398/live116529172648 skipped。

223 tests、4 Ruby、T01/authoring/production Jekyll/192+14以及8时间线流程机械通过。下载artifact11989890630 /159222185 bytes，sha256:5264018373f168f4969b4c74c618e65078b65c79ff0af80553f1cc0a2b0861b9独立匹配；人工看四宽度双主题24张首/尾/刷新图两联系表，并放大390 Light首/尾、1024 Night刷新原图。

[390px Light首段原图](ui009-before-390-light.png)中2026-09-04行作品名尾部被固定“返回顶部”按钮覆盖。长文字自身没有横向溢出，故原scrollWidth检查通过但视觉失败。只确认这个具体遮挡场景，不将整个时间线或其他页面都断言故障。

最小修复：720px内仅给时间线列表右侧留3.5rem避让空间，保留文字自然换行；不改原文字、加载逻辑、全站固定按钮或桌面样式。新审计在首/尾/刷新状态保存TreeWalker/Range.getClientRects真实可见文字行与按钮矩形，明确要求按钮可见且无相交；不以行元素外框代替文字，也不隐藏按钮/删除遮挡断言换取通过。

完整production192+14、修复后24图/8流程和精确main部署/live仍pending，先工作分支；未确认修复后视觉成功。gh未安装，不编造Issue；无新用户问题，其他全站矩阵仍未完成。

## 2026-10-16 修复后生产验收通过

精确head2fcde494768cd4f45c10ae6615e85219f8c8fd62，
[run38774806960](https://github.com/AplusNeutrino/My_Blog/actions/runs/38774806960) build116560105866 success；分支deploy116563569328/live116563569815 skipped。
224 tests、4 Ruby、T01/authoring44/5/7、production Jekyll、旧门禁和192+14通过。

artifact11993626620 /159632592 bytes / sha256:24ef1ed4db15f96d41254d1eee6d3dd18e61b6687a43ca623a73f34f9b756c92下载独立匹配。实际看24张四宽度双主题首/尾/刷新图两联系表，放大390 Light首段、390 Night刷新、1024 Light尾段原图；窄屏长作品名现在完整换行，按钮仍在既有位置但与文字分离，未新增确认显示缺陷。

- [完整192项生产记录](ui009-production-audit.json)
- [24份真实文字行/按钮与溢出诊断](ui009-production-timeline.json)
- [390/768双主题三状态](ui009-production-contact-390.jpg)
- [1024/1366双主题三状态](ui009-production-contact-1024.jpg)

24诊断返回顶部按钮实际可见、真实文字Range非空、overlaps=[]；无行/页面横向溢出且scrollX=0。8时间线流程46条、一次性按钮替换、单列表、滚动同组文本、刷新lazy重置、Enter加载同记录通过。JSON/联系表永久保存、原PNG留artifact14天。

这是localhost production验收，不是部署后线上验收。UI-009/UI-A08d仍validation-pending：交付main后必须核对实际新head build/deploy/live和同24场景截图。其他Library控件/全站矩阵未完成，不标COMPLETE。
