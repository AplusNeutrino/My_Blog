# UI-A07 公开阅读与媒体检查

Base main `c5b99ed2284ac327270de5c952f0a026d85d87b3`；上一文档head的run38577189934已success。范围仅审计与公开证据，产品/旧正文/metadata/URL/hidden/noindex没有改动。

## 场景与已验证边界

计组07plain代码、FF1公开图片，两页×390/768/1024/1366×Night/Light，共16场景。只采用公开文章，候选hidden示例排除。plain代码没有现成复制按钮，不自行新增功能。FF1入口由Archive实际链接核对，使用原有大写FF1路径；基线candidate不是实际可达URL的替代。

检查代码文本/标题、三张图片逐张lazy加载、页面无横向溢出、GLightbox下一张/上一张/关闭及文章URL不变。390/768使用真实W3C touch swipe、1024/1366使用真实箭头click。Copy link只核对成功反馈，**实际剪贴板字节尚未验证**，不能把提示等同于复制内容正确。

桌面线上云浏览器1363×936 Light已看代码与首图/弹层并操作Next、Close；Copy link出现成功提示，但cloud clipboard API读为空，记工具验证局限，不报告网站故障。[桌面媒体截图](uia07-cloud-gallery-light.jpg)仅属此视口补充。

## 生产结果

实现审计head `2c60e4e1aeff6897447e6a0a90a65251869f547f`，[run38588924737](https://github.com/AplusNeutrino/My_Blog/actions/runs/38588924737) build115938279064 success（工作分支deploy/live按规则skipped）。205 Python tests、4项Ruby渲染回归、T01、authoring、production Jekyll、所有旧门禁及176页面场景+14侧栏专项通过。

下载artifact11906433178，核对16阅读记录及16组交互；人工查看40张viewport/gallery/copy-feedback截图的四张联系表，并放大390 Light代码、390 Night弹层、1024 Light图片、1366 Light复制提示。没有确认新的显示缺陷，没有猜测改样式。[完整JSON](uia07-production-audit.json)保存实际输入方法及clipboardBytes=not-verified。

联系表每行依次为代码、文章图片、弹层、代码文章复制提示、图片文章复制提示：

- [390px两主题](uia07-production-contact-390.jpg)
- [768px两主题](uia07-production-contact-768.jpg)
- [1024px两主题](uia07-production-contact-1024.jpg)
- [1366px两主题](uia07-production-contact-1366.jpg)

原176全页及viewport/gallery/feedback PNG保留于artifact14天；上述JSON/联系表永久留仓库。

## 失败与恢复（未隐藏）

- 17f592ee / run38587265953：移动弹层箭头隐藏，脚本点击失败；下载artifact11905583133，看失败截图后改真实touch输入，不改产品。
- 95204750 / run38587922497：触摸使用document坐标，滚动后MoveTargetOutOfBounds；改viewport坐标，不JS触发翻页。
- 5068d0f0 / run38588368297：手势不越界但下一张超时；显式在移动页面初始化前启用touch capability后完整矩阵通过。没有删翻页/关闭/URL断言。

## 当前状态

UI-A07限定生产检查通过；审计与证据非强推main后，需核对其实际head build/deploy/live176+14和相同16线上阅读场景，状态validation-pending。复制实际字节另列UI-A07b pending，其他页面/hover-focus/阅读控件未冒称完成。gh不可用、无新增待答问题，全站仍IN PROGRESS。
