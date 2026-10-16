# UI-A08i — Steam 空数据与游戏离屏封面

状态：in-progress；base f2d463cfb75168b7ca0a883915ef56efa0b7b4e4。

范围：游戏目录Steam游玩时间排序第1页原生封面滚动加载、排序刷新、Steam来源实际结果/空提示、刷新与清除恢复、返回根目录；不代表完整Library库存验收。

2026-10-16云浏览器1363×936 Light实际操作排序、来源、刷新并看图：当前Steam来源0条，暂无记录可见，刷新保留状态；未确认新产品缺陷。当前数据不支持有遥测时的成就/时长视觉验收，不注入伪数据替代。

目标：390/768/1024/1366 × Night/Light，每组统计、排序首屏、滚动末端、刷新、Steam筛选5状态，共40图；8个真实控件流程与原192+14门禁。尚未完成，保持validation-pending；main未修改。

实现：只新增真实控件/逐卡滚动审计。按当前公开JSON验证游戏category/status、分页数量、无重复、进行中优先及Steam分钟降序；逐卡scrollIntoView，保留原生loading/src、等待complete/decode/两帧并记录natural尺寸、初始离屏几何；不要求缓存未命中，不强制图片请求。Steam状态对照sync_status，缺数据只接受已有不可用提示，不造数字。排序/来源刷新、实际空提示、清除/返回与clientWidth溢出均保留严格断言。

本地236项测试、authoring44/5/7、T01保护44/5/5与diff检查通过；本机无Ruby/Jekyll/Chrome，不能冒称视觉或构建通过。完整40截图/8流程/production及main/live仍validation-pending。

真实审计实现：9f6f0fb021c35167d5419afc9a05f4c174f7a4e6，保存ui/audit-008i；5个上传blob与本地git hash-object逐项一致。随后仅追加此SHA记录，须核对最终分支head的CI，不用其他提交成功代替。
