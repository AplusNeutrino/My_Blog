# UI-A07b 实际剪贴板内容检查

审计实现2892b031dc0e0de8493bbe03a7b10ce1a24620b9；生产验收head `e431aeaced355ccb155595fe912860a4007f59dd`，[run38604621533](https://github.com/AplusNeutrino/My_Blog/actions/runs/38604621533) build115992207806 success。分支deploy/live skipped，不能作为线上验收。

两篇既有公开文章、390/768/1024/1366px、Night/Prospero Light，共16复制场景。只在隔离CI浏览器origin授权读写clipboard；先写非URL sentinel并读回确认，再真实click Copy link，核对成功提示，读实际clipboard严格等于当前完整URL。没有替换clipboard API或JS click，没有访问用户个人剪贴板；hidden候选继续排除。

207 Python tests、4项Ruby、T01/authoring/production Jekyll/全部旧门禁、176页面+14侧栏专项通过。16复制实值全部verified且sentinel已替换；生产URL为localhost，不当线上URL通过。没有新增确认产品缺陷，不改样式或原文。

人工查看以下16复制反馈截图（四联系表）并放大1366 Light代码原图，反馈可见，无新遮挡/整页溢出。JSON保存实际copiedUrl与输入验证结果；截图只证明反馈显示，不单独证明剪贴板内容。

- [完整production JSON](uia07b-production-audit.json)
- [390px双主题](uia07b-production-contact-390.jpg)
- [768px双主题](uia07b-production-contact-768.jpg)
- [1024px双主题](uia07b-production-contact-1024.jpg)
- [1366px双主题](uia07b-production-contact-1366.jpg)

来源artifact11915342655；原PNG保留14天，JSON/联系表永久留仓库。UI-A07b仍validation-pending：非强推main后需核对其精确head部署、线上16真实复制URL与同场景截图。其他完整UI矩阵没有冒称完成，无新增待答问题，gh不可用不虚构Issue。

## 2026-10-15 线上复验：限定done

验收main head `aa3dbcec717bbbec27e02c0dd196fb0822a6fdec`，[run38611417490](https://github.com/AplusNeutrino/My_Blog/actions/runs/38611417490) build116015462124、deploy116017753847、verify-live-ui116018039763均completed/success。207 Python tests、4项Ruby、T01/authoring/production Jekyll/旧门禁及production/live各176+14通过。

live artifact11918142663含16阅读记录：实际clipboardBytes=verified、sentinel已替换；复制内容逐项精确等于当前线上URL（https://neutriverse.uk），不使用localhost结果替代。人工查看16反馈图四联系表并放大390 Light代码、768 Night图片、1024 Light图片、1366 Night代码原图，没有新增确认显示缺陷。视觉证据证明反馈可见，JSON和严格clipboard断言证明实际内容，二者分开验收。

- [完整live JSON](uia07b-live-audit.json)
- [390px双主题](uia07b-live-contact-390.jpg)
- [768px双主题](uia07b-live-contact-768.jpg)
- [1024px双主题](uia07b-live-contact-1024.jpg)
- [1366px双主题](uia07b-live-contact-1366.jpg)

UI-A07b限定两篇公开文章Copy link done；其他阅读/完整UI矩阵仍pending。只保存验收证据，未改产品/正文/metadata/URL。新证据文档提交CI单独核对，原PNG在上述artifact保留14天。
