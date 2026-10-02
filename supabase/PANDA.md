# 熊猫学习伙伴

成长记录由 `foamlab_pet` RPC 管理，用户登录后读取。等级、签到及社区经验由数据库计算；`foamlab_private.pet_items` 定义形态、服饰与动作的解锁等级。

## 动作与声音

现有 42 项收藏：5 种形态、13 件服饰、17 组动作、7 种场景装饰。一级开放挥爪、打盹、打滚、踢踏舞、爬行、唱歌和伸懒腰；后续动作包括吃竹子、读书、浇花、钓鱼、冥想和小实验。形态在 Lv.1、4、8、12、18 解锁。既有经验、服饰与选用动作保留。

页面右下方熊猫的 `♫` 按钮可临时播放已解锁动作；个人中心的动作收藏用于选择常用动作。爬行会在视口内移动，靠近或拖动熊猫时停止自动移动。

声音默认关闭。动作菜单或个人中心的声音开关只保存到当前浏览器；打开后，主动选择唱歌会播放一段原创合成旋律。自动动作不播放声音。收起熊猫、关闭声音、退出登录或切换后台标签都会停止声音。点击粒子也可在个人中心关闭；两项效果都遵循系统的减少动态效果设置。

## 文件

- `themes/foam-lab/source/assets/panda-art.js`：矢量熊猫。所有部件（身体、四肢、表情、5 种形态、13 件服饰、7 种场景、动作道具）画在同一个 160 × 180 的 SVG 中，`window.foamPandaArt(faceOnly)` 返回整只熊猫或头像。
- `panda-character.css`：配色（含暗色）、按 `data-form`/`data-outfit`/`data-decoration` 显示部件、按 `data-action` 播放 17 组 CSS 动画；`data-preview-action` 显示静态关键帧，用于收藏预览。帽子互斥：服饰帽子优先于形态帽子，航天头盔优先于所有帽子。
- 旧的像素版（`panda-pixels.js`、`panda-sprites-v2.webp`）已不再加载，可以删除。
- `tools/panda-catalog.json`：42 项收藏的标题、说明与等级，供迁移核对和隔离测试使用；实际权限仍以数据库为准。
- `panda-animation.css`：动作菜单和点击粒子的界面样式。
- `panda-motion.js`：动画时长、取消与 Web Audio 旋律。
- `panda-pet.js`：登录、拖动、搜索、动作菜单、成长收藏。
- `panda-particles.js`：点击反馈及设备偏好。
- `foamlab-theme.css`：全站配色与表面样式（取代原 `panda-theme.css`，后者已不再加载）。
- 竹林照片背景已停用，页面背景改为浅色网格纹理。

## 检查

`node tools/check-panda-growth.cjs` 检查成长路线、全部收藏的外观差异和装饰保存；`node tools/check-panda.cjs` 检查宠物功能；`node tools/check-panda-animation.cjs` 检查 17 组动作确实在动、音效开关、粒子数量、手机菜单和暗色首页。截图保存在 `.openfoam-work/panda/`。

`supabase/tests/panda-companion.sql` 使用事务回滚测试账号及内容，检查经验、解锁、权限和重复操作。新增动作对应迁移 `20261002100304_panda_action_expansion.sql`；像素养成扩展对应 `20261002103139_panda_pixel_growth.sql`。装饰保存在 `foamlab_pets.decoration`，仍通过受权限保护的装备 RPC 更新。

熊猫是本站原创的矢量造型，未使用游戏或第三方素材。首页上，熊猫出现在视口内时，右下角的悬浮熊猫会暂时隐藏，避免同屏出现两只。
