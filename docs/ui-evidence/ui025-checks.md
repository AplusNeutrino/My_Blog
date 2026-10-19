# UI-025 — Light 星盘未选中行星符号不可辨

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
