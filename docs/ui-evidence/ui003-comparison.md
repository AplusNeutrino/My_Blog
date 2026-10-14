# UI-003 mobile topbar / drawer focus

Base `c12d9d2ac262e924ce800f7e303f59279a0e9741`；实现head `e020fb73e9de4fcd91732c2bc7e281575f3395af`。
日期2026-10-14；旧重构COMPLETE历史不改。

## 复现与修复

之前390/768px頂栏显示内部`Neutriverse-section` / `Neutriverse-project`，见[上一轮真实Chrome截图](uia02-sheet-390-light.jpg)。Chirpy默认以不认识的layout名兜底；现保留其结构/旧布局逻辑，仅自定义section/project显示已有page.title，HTML escape后保留完整title提示。长标题可缩小并ellipsis，菜单/搜索不收缩，不改项目名称或正文。

UI-003a：run38509680549在既有390px mask关闭焦点门禁超时；源码存在开菜单rAF在快速关闭后抢回焦点的竞态。实现检查callback执行时菜单仍打开；原门禁不放宽。[run38509991407](https://github.com/AplusNeutrino/My_Blog/actions/runs/38509991407)重新通过204 tests、旧移动菜单焦点门禁、T01/authoring、production Jekyll和全部原门禁。工作分支deploy/live按条件跳过，不算部署。

## 截图与回归证据

artifact11869786736：120张全页PNG、32张viewport PNG、[完整几何及16组交互](ui003-audit.json)。120场景包括THINK四状态、BUILD三状态、七详情及OBSERVE，四宽度双主题。每个移动顶栏与h1语义名称相同、完整title提示保留、控件无重叠；几何/菜单门禁通过不等于所有页面视觉正常。

已人工查看8张viewport联系表，重点确认移动顶栏和长项目名、按钮位置、字体与四入口。代表性原始截图随Actions保留14天；以下联系表与JSON长期存仓库。

|宽度|Night|Light|
|---|---|---|
|390|[截图](ui003-contact-390-dark.jpg)|[截图](ui003-contact-390-light.jpg)|
|768|[截图](ui003-contact-768-dark.jpg)|[截图](ui003-contact-768-light.jpg)|
|1024|[截图](ui003-contact-1024-dark.jpg)|[截图](ui003-contact-1024-light.jpg)|
|1366|[截图](ui003-contact-1366-dark.jpg)|[截图](ui003-contact-1366-light.jpg)|

## 未完成与新问题

- UI-004：1024/1366×900窗口（实际网页高度小于窗口高度）底部DISCOVER与社交/主题组重叠，双主题viewport确认。优先修复，不当审美偏好。
- 原全页CDP截图侧栏部分裁切：新viewport完整，rect[0,260]；这是不同截图机制的差异，不据此修改transform。
- [main run38526220139](https://github.com/AplusNeutrino/My_Blog/actions/runs/38526220139)精确head e020fb73：build115727074632、deploy115727829396、verify-live-ui115727902355 success。部署后live120场景/16组交互通过，artifact11875927572下载。人工看[390px THINK Light](ui003-live-think-light.png)、[长项目名Night](ui003-live-project-night.png)、[768px OBSERVE Light](ui003-live-observe-light.png)、[1024px BUILD Night](ui003-live-build-night.png)；[live JSON](ui003-live-audit.json)保存检查条件与结果。云浏览器1363×936 reload核对隐藏移动标题文本/tooltip为THINK，并实际切换主题。UI-003 done。
- UI-003a仅production快速mask焦点门禁已通过，保护代码已部署；live矩阵操作主题与Escape，但未单独复验快速mask焦点，保持validation-pending。下轮补专项，不以部署代替验收。
- 其他文章/独立工具/Library等矩阵仍pending，无新增用户决策问题。
