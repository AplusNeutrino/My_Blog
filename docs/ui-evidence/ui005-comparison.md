# UI-005 表格渲染修复

## 实际复现

Base main9708457fee99f7a00d8d74bb13bf59d669687ad4。线上1363×936 Light计组04目录跳转后的[原图](ui005-before-table.jpg)显示两张表格为连续竖线正文，DOM table=0；Night同样table=0。源文件两表紧邻ATX标题，没有空行。

## 修复与保护

仅post pre_render内存输入补合法table header/separator前缺失的空行；不修改原md或metadata，不改变全站Markdown parser。不处理普通竖线正文，代码围栏内示例不变，重复调用幂等。原正文/日期/URL/hidden基线仍通过。

初始98a03cc1 / run38568937714因bundle缺minitest启动失败，尚无生产截图。改用零额外依赖Ruby断言入口后，head `c20396fa62672943eda5d675955cc6eeb394d3ea` 的[run38569176497](https://github.com/AplusNeutrino/My_Blog/actions/runs/38569176497) build115869531704 success；分支deploy/live按约定skipped。

4项Ruby渲染回归、205 Python tests、T01/authoring/production Jekyll/所有旧门禁通过。新增8表格场景让总矩阵160+14通过；两table与两scroll-wrapper、无页面横向溢出、真实pointer-wheel横向滚动断言全部通过。

下载production artifact11897310795，人工查看8张双主题四宽度[联系表](ui005-production-contact.jpg)，放大390 Light及1366 Night原图：原先连续正文变为可读行列；宽表在容器内横向滚动，没有裁掉源数据或改写内容。[生产JSON](ui005-production-audit.json)记录具体尺寸与操作。截图为工作分支生产环境，尚不是线上证据。

## 当前状态与剩余

UI-005 validation-pending：已通过的修复及证据准备非强推main；必须核对main实际head build/deploy/live160+14并查看8张相同场景线上截图，再标done。文章代码/图片/其他阅读控件仍pending，不把表格修复当全站COMPLETE。gh不可用，没有虚构Issue或把CI成功冒称人工视觉正常。
