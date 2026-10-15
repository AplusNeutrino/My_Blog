# UI-A08b 可见书籍封面加载与绘制检查

生产验收head `aa328fa7b8f5e09d58adbe3d8aada6f7ae0f8b03`，[run38674518402](https://github.com/AplusNeutrino/My_Blog/actions/runs/38674518402) build116224939740 success；分支deploy/live skipped，不当作线上验收。

范围为书籍目录固定viewport的可见img.pgl-cover，390/768/1024/1366px × Night/Prospero Light共8场景、56次图片加载。等待真实complete、严格原生尺寸>0、原生decode()成功及两帧后保存截图，没有修改src/loading、mock图片或替换加载器。失败/超时仍阻断并留JSON/PNG。211 tests、4 Ruby、T01/authoring/Jekyll/旧门禁和192+14通过。

前一head de7dbdf4虽然加载尺寸成功，但截图存在尚未绘制区域；该结果未作为视觉通过。此次人工查看8张解码后截图两联系表并放大390 Night原图，可见封面均显示，未确认新产品缺陷，不改网站样式或图片源。

- [完整生产审计](uia08b-production-audit.json)
- [8场景加载记录](uia08b-production-covers.json)
- [390/768双主题](uia08b-production-contact-390.jpg)
- [1024/1366双主题](uia08b-production-contact-1024.jpg)

来源artifact11945044852，sha256:1ea5e0c902c998a32139ca4a067b66c82adb273936f3653cc92602bf44b15ae8，原PNG保留14天，JSON/联系表永久留仓库。固定视口可见图片通过不等于完整库存或离屏滚动加载通过；搜索/筛选/分页/时间线另项pending。UI-A08b仍validation-pending：main交付后核对精确head部署和线上相同8场景记录/截图，不能用localhost替代，无新待答问题。

## 2026-10-15 线上复验：限定done

验收main `57a6817cd90f27f41039c92040c38ff3de53a03e`，[run38679922788](https://github.com/AplusNeutrino/My_Blog/actions/runs/38679922788) build116241892225、deploy116243565530、verify-live-ui116243614933全部success。211 tests、4 Ruby、T01/authoring/Jekyll/旧门禁及production/live192+14通过。

线上8场景56次可见书籍封面complete/原生尺寸/原生decode全部通过，实际等待解码及两帧后截图。人工看8张线上截图两联系表并放大390 Light原图，没有空白封面或新增确认显示缺陷。此结论仅针对固定viewport可见书籍封面，不覆盖全库存/离屏图片/时间线或检索交互。

- [完整live audit](uia08b-live-audit.json)
- [8场景live加载记录](uia08b-live-covers.json)
- [390/768双主题](uia08b-live-contact-390.jpg)
- [1024/1366双主题](uia08b-live-contact-1024.jpg)

来源live artifact11946904727，sha256:b16ca99d4828149863d34acf498e4ca12c40d2ce6280d080cb268f50af538f9c，原PNG保留14天，JSON/联系表永久保存。UI-A08b限定done，全站IN PROGRESS；没有为采图修改产品图片加载/样式/同步数据，旧COMPLETE历史保持原样。
