# UI-A08i — Steam 空数据与游戏离屏封面

状态：production通过，main部署/live validation-pending；base f2d463cfb75168b7ca0a883915ef56efa0b7b4e4。

## 2026-10-17 — 精确main首次超时，原head重试

- main b4a502396bd02650738f4b69912ef2bdca437173 / [run38920457806](https://github.com/AplusNeutrino/My_Blog/actions/runs/38920457806)：首次build117038739414 failure；deploy117041059374/live117041060364 skipped，尚未部署/线上验收。前置237 tests、4 Ruby、T01、authoring、production Jekyll通过，不能据分支成功声称main矩阵通过。
- Chrome在390 Night Library场景后的下一次导航driver.get中发生控制通道ReadTimeoutError localhost:52101（120s）。按代码顺序下一页为友链；没有该目标页面的scene日志/DOM/截图，不能判定产品缺陷或具体网络根因。完整浏览器矩阵未完成。
- 部分artifact12054128548 /16327844 bytes /sha256:f4d97a6a5ee31ed9678edf2cf5df1ce04e5816406284c4db99077f63f870ed72下载后独立匹配，仅有本项390 Night5状态，source原图已实际查看，“暂无记录”清晰可见，不代表完整40图或live。
- 已重试同一run失败jobs；第二次build117067139721运行中，仍是b4a50239，不改产品/审计/门槛。3文档诊断记录仅存verification/ui-a08i-retry-log，避免新main提交取消同head重试；下轮验收最新attempt和实际部署/live。无新用户决策，状态validation-pending。

## 2026-10-16 — 修正取景后生产验收

- 精确验收head707b6d49c3066bcfaa54ed3f10bfe811608e966a / [run38913520936](https://github.com/AplusNeutrino/My_Blog/actions/runs/38913520936)：build117015038501 success，deploy117019410328/live117019410572 skipped（分支，不作部署）。237 tests、4 render-only Ruby、T01保护44/5/5、authoring44/5/7、production Jekyll、Search/feed/SEO/资源/移动无障碍及192页面+14侧栏通过；本机回归/authoring/T01/diff也通过，本机未运行Jekyll/Chrome。
- 下载artifact12051129960 /226689222 bytes /sha256:b6865cf6fb81b892f9717e1b9151ccdb6ce9d663c9269423b13dd9d73970afe9，独立摘要匹配。人工查看40张四宽度双主题统计/排序首屏/末端/刷新/来源图两联系表，放大390 Light来源空提示、768 Night末端封面及1024 Light来源原图。8张来源图在真实关闭浮层后，“暂无记录”清晰可见；其他状态没有新增确认缺陷，不凭偏好修改产品。
- 8流程、40诊断重新核对通过：游戏120条、第一页24×8=192次原生封面complete/decode/自然尺寸、初始离屏覆盖；进行中优先与当前数据时长组内降序、排序刷新同URL/ID、来源0条/空提示刷新、清除恢复与返回根目录通过，scrollX=0且page<=clientWidth+1。
- Steam现状privacy_boundary_unavailable，只有无遥测数据路径有真实证据；不等同有时长/成就数据场景已验收，不绕过隐私边界或编造数据。完整库存/其余分页图片/其他全站矩阵仍pending。没有新用户决策，gh未安装，不编造Issue。
- 本轮只回写计划日志与uia08i-verified-production-*公开证据，不改产品/数据/旧COMPLETE。已验证审计交付main后，必须核对新main精确head build/deploy/live和同40图，现阶段保持validation-pending，不以分支通过冒充线上。

修正后联系表：[390/768](uia08i-verified-production-contact-narrow.jpg)、[1024/1366](uia08i-verified-production-contact-wide.jpg)；[192审计](uia08i-verified-production-audit.json)、[40诊断](uia08i-verified-production-diagnostics.json)。原PNG在上述artifact保留14天。首次取景证据仍原样保留，不能与本组混称。

## 2026-10-16 — 首次生产检查与视觉取景修正

- 验收head53b536052b7e6443ca2795d23a60c440c0f0ca9a / [run38905074465](https://github.com/AplusNeutrino/My_Blog/actions/runs/38905074465)：build116986945525 success；deploy116991131418/live116991132144 skipped（工作分支，不作部署通过）。236 tests、4项render-only Ruby、T01/authoring44/5/7、production Jekyll/Search/feed/SEO/资源/移动无障碍及192+14通过。
- artifact12047752802 /226394901 bytes /sha256:5ca17bbbf26e618c5f540f6bf5bbf16c0a6d4583cc7d8cd692b375addc91b3e0，下载后摘要独立匹配。人工看四宽度双主题40图两联系表，放大390 Light末端封面、390 Night来源、1024 Light统计原图，未确认产品缺陷。原PNG在artifact保留14天；本次40诊断、192审计与两联系表永久保存，均标production首次取景，不能冒充最终视觉验收。
- 8流程记录：游戏库存120，第1页24卡×8=192次原生封面complete/decode/natural尺寸通过，初始离屏条目有覆盖；进行中优先/时长组内降序、排序刷新URL/ID、Steam来源0条/刷新、清除与返回通过。Steam状态privacy_boundary_unavailable，不绕过隐私边界、不补造时长/成就；有遥测时视觉仍pending-no-data。
- **验收缺口而非产品缺陷**：8张source截图均在高级筛选浮层打开时拍摄，“暂无记录”被正常浮层遮住；is_displayed不等于截图中可读。此组不能据CI成功写视觉通过。仅修审计：真实点击summary关闭浮层并等待关闭，再同场景截图；空提示、数据对照与全部原断言不放宽，新增1项接线回归。
- 本次范围：现有审计/回归、UI计划日志与uia08i公开证据，不改产品/数据。修正后精确head完整40图/8流程及main/live仍validation-pending；main仍f2d463cf，无新用户决策，gh未安装不编造Issue。完整库存/其余分页与其他全站矩阵继续pending。
- 修正后本地237 tests、authoring44/5/7、T01保护44/5/5及diff通过；没有本机Ruby/Jekyll/Chrome，未将接线测试当视觉验收。

首次生产联系表：[390/768](uia08i-production-contact-narrow.jpg)、[1024/1366](uia08i-production-contact-wide.jpg)；[192审计](uia08i-production-audit.json)、[40诊断](uia08i-production-diagnostics.json)。

范围：游戏目录Steam游玩时间排序第1页原生封面滚动加载、排序刷新、Steam来源实际结果/空提示、刷新与清除恢复、返回根目录；不代表完整Library库存验收。

2026-10-16云浏览器1363×936 Light实际操作排序、来源、刷新并看图：当前Steam来源0条，暂无记录可见，刷新保留状态；未确认新产品缺陷。当前数据不支持有遥测时的成就/时长视觉验收，不注入伪数据替代。

目标：390/768/1024/1366 × Night/Light，每组统计、排序首屏、滚动末端、刷新、Steam筛选5状态，共40图；8个真实控件流程与原192+14门禁。尚未完成，保持validation-pending；main未修改。

实现：只新增真实控件/逐卡滚动审计。按当前公开JSON验证游戏category/status、分页数量、无重复、进行中优先及Steam分钟降序；逐卡scrollIntoView，保留原生loading/src、等待complete/decode/两帧并记录natural尺寸、初始离屏几何；不要求缓存未命中，不强制图片请求。Steam状态对照sync_status，缺数据只接受已有不可用提示，不造数字。排序/来源刷新、实际空提示、清除/返回与clientWidth溢出均保留严格断言。

本地236项测试、authoring44/5/7、T01保护44/5/5与diff检查通过；本机无Ruby/Jekyll/Chrome，不能冒称视觉或构建通过。完整40截图/8流程/production及main/live仍validation-pending。

真实审计实现：9f6f0fb021c35167d5419afc9a05f4c174f7a4e6，保存ui/audit-008i；5个上传blob与本地git hash-object逐项一致。随后仅追加此SHA记录，须核对最终分支head的CI，不用其他提交成功代替。
