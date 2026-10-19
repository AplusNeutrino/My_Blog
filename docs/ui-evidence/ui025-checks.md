# UI-025 — Light 星盘未选中行星符号不可辨

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
