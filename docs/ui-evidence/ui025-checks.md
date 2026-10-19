# UI-025 — Light 星盘未选中行星符号不可辨

## 来源诊断提交与精确CI收据

- 只读诊断提交8a7ac42a690124ffbb3aea8d656c9c8556f48255已非强推保存ui/fix-025；[run39299220841](https://github.com/AplusNeutrino/My_Blog/actions/runs/39299220841)真实创建、in_progress，head精确匹配。289tests/T01/authoring/diff本机通过；尚无新head完整build/production图或失败来源关联现场，不声称诊断已定位根因。
- main再次核对仍004447db，UI024/025 validation-pending；产品CSS/v41/app.js/工作流未变，未部署。此收据另存audit/ui-a12-focus，不推进工作分支取消CI；下一项核对同8a7ac42a完整结果，若字体再失败检查候选src及缓存关联，缺失证据明确保留，不盲重跑/放宽门禁。无新用户决定，全站IN PROGRESS，不暂停。

## 2026-10-20 字体来源诊断预定范围

- Task UI-A09-F/UI024/UI025；base/main004447db、工作ac3430d9、审计父9776385f。已知复现是run39281958731在1366 Night THINK的30s document.fonts.ready超时，原PNG/JSON见ui025-ac3430-evidence；3个Noto Sans SC面仍loading但51请求finished，缺少src关联，不能认定产品缺陷或网络根因。
- 只改tools/check_think_build_visual.py失败路径只读诊断、tests/test_font_network_diagnostics.py必要执行回归、计划日志。失败后从该次导航已有performance事件识别fonts.googleapis.com/css或/css2响应，用CDP Network.getResponseBody读取浏览器已有公开CSS（不fetch/新增请求、不读任意body或headers）；解析font-face family/style/weight/unicode/src，关联loading FontFace与Font资源/网络缓存元数据。读取失败/匹配不唯一明确记录，不强行判因。
- 原document.fonts.ready/30s/截图/raise与所有视觉交互门禁不变；不清缓存、重载、替换字体、主动font.load、拦截网络或改产品。诊断只在原失败后执行，未出现超时不伪称收集到真实故障；新head本机/production/完整CI及部署按实际保留pending，先工作分支，main不动。验收包括实际helper执行、无关/敏感响应不读、Unicode/weight关联、读取失败保留，及新head精确CI结果。无新用户决定，gh不可用。
- 本机289tests（3.441s）、authoring44/5/7、T01保护44/5/5及diff通过；4新执行回归覆盖真实helper的来源限制/base64/weight/Unicode/缓存/缺失多候选/错误与只读失败接线。当前只有模拟输入执行，不是新增真实浏览器故障证据；原失败历史保留，新精确head CI/production及部署仍待验证。CSS/v41/app.js和工作流不变。

## 2026-10-20 ac3430d9生产专项通过、完整构建字体阻塞

- [run39281958731](https://github.com/AplusNeutrino/My_Blog/actions/runs/39281958731)精确head ac3430d954ae4ac2e6009d0bb798e63a5c5d95f3；build118157843464 failure于2026-10-19 16:15:30 UTC。285tests/T01/authoring/production Jekyll、图标8组、OBSERVE8组成功；后续THINK1366 Night等待document.fonts.ready超时。deploy118173857688/live118170749265 skipped，main仍004447db，不称本修复上线。
- 本轮实际看图标8原图：普通/active符号均清晰；隔离built CSS+原PNG而非整应用业务。OBSERVE58帧用8联系表全看，放大1024 Night及1366 Light loading-wrap原图；标题无遮挡、disabled fixture焦点date→末checkbox且inside=true，8组原回环/导航/Escape通过。16帧为明确disabled UI fixture，当前没有已加载完整行星菜单，不认证服务健康或自然已加载图标；1366短内容scroll0不虚称滚动。
- 原始ZIP摘要、已看图、原audit、失败原图/字体快照与全部58PNG哈希尺寸见[本head来源清单](ui025-ac3430-evidence/source.json)。3个包摘要独立匹配。THINK包只看失败PNG/JSON，其他2165文件未人工验收；没有把总包存在当整页矩阵通过。
- 失败快照fontSet=loading，566面中112loaded/3loading/451unloaded；3loading为Noto Sans SC400/500/600同Unicode段，51个采集Font请求均finished、46resource条目。不同于UI024旧Serif面，不强归同因；尚无CSS src到面/请求一一关联，不推断CDN/缓存/Chrome。未重跑、不增timeout/跳字体、不改产品。UI024/025完整CI/部署复验仍pending，无新增用户决定。
- 下一项：字体CSS规则src/Unicode/weight与FontFace/网络缓存生命周期的受控诊断，原超时门禁必须保留；独立UI-A12自然业务控件可继续。仅证据提交audit/ui-a12-focus，不再推进产品分支制造新CI。

## 最新fixture修订提交

- `ac3430d954ae4ac2e6009d0bb798e63a5c5d95f3` 已非强推更新ui/fix-025；[run39281958731](https://github.com/AplusNeutrino/My_Blog/actions/runs/39281958731)真实创建且queued。仅修测试fixture并加强前提，产品CSS/v41/app.js与9e1e5a13相同；285tests（3.253s）/T01/authoring/diff本机通过，非视觉验收。
- 下一轮先核对同ac3430d9完整CI与原回环门禁、新head截图，不用旧图或产品存在代替通过。main仍004447db，UI025与UI024 pending；本收据另存audit/ui-a12-focus，不再推进工作分支取消检查，无新用户决定。

## 2026-10-19 反向Tab诊断判因与预定修订

- Base/main004447db，工作9e1e5a13，审计父31004361。run39274494467 build118135137834 failure，图标8场景、283tests/T01/authoring/Jekyll成功，OBSERVE此次在1024 Night失败（不是此前1366）。deploy118136152642/live118136154401 skipped。无新用户决定、gh不可用。
- artifact12196887004（1884332bytes），ZIP SHA25664b2374542fb9d397695ec375d67dbccbbbf0167c0e990716d6209b04a42983a匹配。原audit显示按键前1742.4ms active=datetime，但first=refresh、refresh.disabled=false/export=true；按键后1753.1ms active=refresh、inside=true，控件集合未变化。实际看1024 Night loading-focus/wrap两图，刷新已明亮可用且后图焦点仍在弹层内。因此本次是异步请求回调破坏“首两button disabled”fixture前提，不是产品反向Tab逃出，不据此改trap。不能反推上次无快照1366失败原因一定相同。
- 本轮先限定仅tools/check_observe_dialog.py中既有明确disabled UI fixture：在此可丢弃场景临时固定两按钮disabled getter/原生disabled属性，保存应用回调希望写入的最新值，finally恢复原own descriptor及最新请求值；不改全局prototype、不拦截网络/取消请求、不冻结其他控件，不修改app.js/CSS/v41。原自然加载/真实Tab/滚动/导航检查不变，另加强按键前first=datetime和两按钮disabled前提断言，末控件回环断言保持。新增实际执行fixture安装/恢复回归及故障拒绝，保存原失败两图/audit。
- 未验证修订只ui/fix-025，main不动，完整新head/部署复验仍pending；UI024字体阻塞不因局部fixture修订关闭，不冒称远端服务健康。

## 最新诊断提交

- 只读诊断修订 `9e1e5a137bbaf06523d894fb9856909b97d12a8c` 已非强推更新ui/fix-025；[run39274494467](https://github.com/AplusNeutrino/My_Blog/actions/runs/39274494467)真实创建且in_progress。产品CSS/v41/app.js与b0939630相同，新增按键前后快照、保留原focusIsLast门禁及失败后截图、1项诊断执行回归和已看八图/真实失败记录；283tests/T01/authoring/diff本机通过，不称新CI通过。
- 下轮先核对该head完整CI及反向Tab前后快照，不根据未知原因改产品，不把此前8图成功替代新head完整验收。main仍004447db，无新用户决定，UI025/UI024及全站pending；本收据另存audit/ui-a12-focus，避免取消新工作分支CI。

## 2026-10-19 八图通过但完整构建受阻

- 本轮base/main004447db，工作head b0939630，审计父88c7923a。run39265653590 build118104425275于14:06:43 UTC failure；282tests/T01/authoring/production Jekyll与图标8场景成功，但OBSERVE第7流程1366 Night反向Tab断言失败，deploy118105593856/live118105594009 skipped。不交付main、不称全通过。
- 图标artifact12192852185（306732bytes），ZIP SHA2561edd7b9b38c756ac957056aff4f02ded84c76233cae19b7ec74ade6a919b595c独立匹配；实际逐张看四宽度双主题8正常viewport，普通/选中太阳/月亮/土星清晰。8audit均6张原PNG加载、无溢出/正确底色通过，4个Light旧色精确注入拒绝；Night未发生旧色差异，oldLightFillRejected=false是预期，不当失败。此隔离fixture仅CSS/PNG，不是服务/整应用布局验收。
- OBSERVE artifact12193391732（3088261bytes）SHA25649236205d7d120f6799fb70b263e883a0c580d65d03cbafbef3d329fe3b97d98匹配。6流程passed；1366 Night initial/loadingFocus=datetime后反向Tab失败，1366 Light未开始。仅实际查看1366 Night loading-focus原PNG：截图时服务仍加载，两个首按钮disabled；未捕获按键后active/disabled/控件列表，不能判断是加载完成后可用控件变化、DOM替换或实际焦点逃出。
- 修改前范围限定：tools/check_observe_dialog.py仅记录原断言按键前后焦点/启用控件/是否末端/加载节点数和失败截图；同一selector与最后控件断言不变，不增加自动重试、不mock网络/钉死disabled、不改产品。必要执行诊断回归、计划日志及公开证据；没有根据推测修复业务。
- 保存图标8原PNG/audit、OBSERVE原audit及1已看失败前PNG至ui025-production/；其余48 OBSERVE原PNG未逐张看，仅Actions保留。新head完整CI/部署仍pending，UI024字体阻塞也不由本次生产结果关闭；gh不可用，无新用户决定。

## 最新精确修订与CI入口

- 审计时序修订 `b09396304d5418203d27c2ed82aebfd6f5a78176` 已非强推更新ui/fix-025；[run39265653590](https://github.com/AplusNeutrino/My_Blog/actions/runs/39265653590)真实创建且in_progress。产品CSS/v41与ae6f7c7d相同，仅审计时序、2回归及真实失败/部分截图记录变化。282tests/T01/authoring/diff本机通过非视觉验收。
- 下轮先核对同一b0939630完整build及新8帧；旧4图仅首轮部分证据。main仍004447db，未部署本次修复，UI025保持validation-pending；本收据另存audit/ui-a12-focus，不再次推进工作分支取消CI。无新用户决定。

## 2026-10-19 首轮失败与审计时序修订范围

- 本轮base/main004447db、工作head ae6f7c7d、审计父8a157def。run39259609173 build118083524733 failure：production Jekyll/280tests/T01/authoring成功，图标fixture在768 Light注入旧heading后立即读取仍rgb(255,248,231)，未等待fill180ms过渡；不是产品普通浅底断言失败。deploy118084179998/live118084180556 skipped，不称上线。
- artifact12188139422（149657bytes）独立ZIP SHA25625ea2cd95f17d5f3d52b110fe9d536511b77ec9d62a7df7a8ca2998ab11c3ccb匹配。实际看390/768双主题4正常viewport PNG，普通与选中太阳/月亮/土星符号清晰；不是完整8图，1024/1366未执行、audit.json未写出，不把其余矩阵或线上算通过。
- 预记仅修tools/check_atlas_planet_icons.py的故障注入时序及必要执行回归、计划/日志/本记录和部分公开证据ui025-production-partial。等待实际computed fill精确达到旧Light rgb(23,68,90)，有限5s，未达到仍失败；不禁动画/放宽原产品底色或图片加载/溢出门禁，不改CSS/v41/PNG/业务/字体等待。首轮390 Light可能读到中间色也不当充分故障注入证据。
- 未验证修订仍ui/fix-025，main不动，完整新head CI/8图/部署复验pending；UI024字体阻塞不变，gh不可用未建Issue，无新用户决定。

## 精确工作提交与验收入口

- 实现 `ae6f7c7d1d544990e5f8a200cb07de4f4ddba01c`，工作分支 `ui/fix-025`；[Actions39259609173](https://github.com/AplusNeutrino/My_Blog/actions/runs/39259609173)真实创建且in_progress。main复核仍004447db，未部署本次修复，不称8图/完整build成功。
- 本收据单独保存audit/ui-a12-focus，不推进ui/fix-025避免取消精确head CI；下一轮先核对同一ae6f7c7d完整build、图标8帧与原门禁，未验收不合main。UI024失败及字体根因未证实状态仍有效。

- 2026-10-19 confirmed，P2内容可读性，不是用户偏好。base/main `004447dbdf2a8187c2cac9e7ab568709296ac8ab`；审计父 `77a3c16a17a5335133a8cb193d47313fb1b9d1ea`。gh不可用未建Issue，无新用户决定。
- 实际云Chrome1363×936 Prospero Light，真实服务自然加载完成，未选中10个行星节点只显深色圆饼，符号几乎不可辨；选择左表太阳后，太阳圆底变浅且相同PNG符号立即清晰。实际截图uia12b-light-lines-off.jpg、uia12b-light-sun-hidden.jpg及ui025-light-selected-before.jpg；前两图分别是0连线10节点、10连线9节点，菜单临时开关已恢复原值，不伪称全程默认。
- DOM/源码佐证：normal circle fill=rgb(23,68,90)，来自`fill:var(--atlas-heading)`；active fill=rgb(255,248,231)。planet-sun PNG是透明背景深青符号（原图已看），左表及选中同资源清晰，所以不是图标缺失。root主题heading浅色而Light heading深色，错误复用文字token使Light圆底与深色符号低对比。
- 预定最小产品范围：occult-atlas-app/styles.css分离planet普通底色token，Night保持原#e7ecf3，Light用既有选中浅底#fff8e7；_data/occult_atlas.yml版本40→41；必要图标对比回归及四宽度双主题真实Chrome图标fixture专项/接入，计划日志与公开证据。不得改PNG、图标形状/布局、业务/远端/私密边界或外部仓库，不放宽旧门禁。
- 验收：真实原PNG普通/active圆底均清晰，Night不变，hover/选择和显示开关保持；四宽度双主题图及实际部署同场景复验。图标fixture必须明确仅视觉CSS/资源隔离，不等于服务/整应用业务通过。未完成验证前仅工作分支，UI024字体阻塞仍保留。

## 最小实现与待验收

- 普通节点fill分离为--atlas-planet-fill，Night=#e7ecf3与旧值相同，Light=#fff8e7复用既有active浅底；active规则不变。资源v41；图标PNG/形状/布局/业务不改。
- 本机280tests（3.327s）、authoring44/5/7、T01保护44/5/5及AST/diff通过，不是视觉验收。新实际Chrome隔离fixture覆盖4宽度×2主题、太阳/月亮/土星普通及选中6个原PNG、加载/无溢出/普通底色和旧耦合故障拒绝，8viewport等待CI实际产生和人工查看。该fixture不认证远端或整应用布局。
- 云真实Night自然加载后10普通节点底色rgb(231,236,243)，图标可辨，ui025-night-before.jpg已看；作为修复前Night基线而非修复后证据。Night左表图标另有低对比候选S-A12-02，未扩入本次节点修复，也不将其当审美直接改动；后续单独确认可读性范围。
- 完整production Jekyll/8图/精确实现CI与main部署复验均validation-pending，工作分支ui/fix-025，main仍004447db，UI024字体阻塞保留；无新用户决定。
