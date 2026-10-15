# UI-009 窄屏时间线文字被固定按钮遮住

状态：validation-pending。
Base main2e3d2844af408504cb616b9596ea682c97c3edd0，复现验收head47b3c294711c77abb62b321f71f5ae1eb658f855。
[run38765012413](https://github.com/AplusNeutrino/My_Blog/actions/runs/38765012413) build116526426682 success，分支deploy116529172398/live116529172648 skipped。

223 tests、4 Ruby、T01/authoring/production Jekyll/192+14以及8时间线流程机械通过。下载artifact11989890630 /159222185 bytes，sha256:5264018373f168f4969b4c74c618e65078b65c79ff0af80553f1cc0a2b0861b9独立匹配；人工看四宽度双主题24张首/尾/刷新图两联系表，并放大390 Light首/尾、1024 Night刷新原图。

[390px Light首段原图](ui009-before-390-light.png)中2026-09-04行作品名尾部被固定“返回顶部”按钮覆盖。长文字自身没有横向溢出，故原scrollWidth检查通过但视觉失败。只确认这个具体遮挡场景，不将整个时间线或其他页面都断言故障。

最小修复：720px内仅给时间线列表右侧留3.5rem避让空间，保留文字自然换行；不改原文字、加载逻辑、全站固定按钮或桌面样式。新审计在首/尾/刷新状态保存TreeWalker/Range.getClientRects真实可见文字行与按钮矩形，明确要求按钮可见且无相交；不以行元素外框代替文字，也不隐藏按钮/删除遮挡断言换取通过。

完整production192+14、修复后24图/8流程和精确main部署/live仍pending，先工作分支；未确认修复后视觉成功。gh未安装，不编造Issue；无新用户问题，其他全站矩阵仍未完成。
