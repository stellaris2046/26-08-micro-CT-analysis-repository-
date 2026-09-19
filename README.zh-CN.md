# 通用小鼠颌骨 micro-CT 分析 skill

[English](README.md) · [MIT 许可证](LICENSE)

面向小鼠上颌骨、下颌骨研究，提供校准多平面重建（MPR）、第二磨牙（M2）定位、釉牙骨质界至牙槽嵴顶（CEJ–ABC）距离测量，以及根分叉区域骨体积分数（BV/TV）的人工复核流程。

本仓库提供 **skill 指令、方法说明及一个坐标距离计算工具**。它不是自动完成图像分割的完整软件。图像读取、MPR、分割和解剖学复核需要研究者自行提供数据及适用工具。本公开版本不提供实验影像、样本信息、人工标注、测量结果或凭据。

## 使用方式

将 [`mimics-mouse-jaw-analysis`](mimics-mouse-jaw-analysis/SKILL.md) 文件夹复制到 Codex 的个人 skills 目录，通常为 `~/.codex/skills/`。若已有同名 skill，先比较版本，只保留一个活动版本，避免覆盖正在使用的研究方案。也可以直接阅读方法说明，手动执行分析。

调用示例：

> 使用 $mimics-mouse-jaw-analysis 分析我的小鼠下颌骨 DICOM。先核查校准、覆盖范围和 M2 方向，再提出 CEJ–ABC 标志点。实验数据和结果保存在仓库之外。

配套距离计算器使用 Python 3.10+ 标准库，不需要额外 Python 依赖。图像处理软件必须支持可靠的物理坐标和校准 MPR；Mimics 可作为一种选择，但需自行取得其许可证。本仓库不附带 Mimics 或自动控制接口。

## 合成示例

在仓库根目录运行：

```sh
python mimics-mouse-jaw-analysis/scripts/calibrated_cej_abc_distance.py --self-test
mkdir results
python mimics-mouse-jaw-analysis/scripts/calibrated_cej_abc_distance.py examples/synthetic-landmarks.json --output-json results/distances.json --output-csv results/distances.csv
python -m unittest discover -s tests -v
```

示例坐标完全虚构，预期投影距离分别为 0.06 mm、0.04 mm，只验证计算逻辑。输入 spacing 的顺序是 **x/列、y/行**，与 DICOM `PixelSpacing` 的行、列顺序不同。详见[计算器输入约定](mimics-mouse-jaw-analysis/references/measurement-tool.md)。

## 科学适用范围

- 在原始灰度 MPR 及相邻切片上确认解剖结构；三维显示和阈值掩膜不能单独确定 CEJ 或 ABC。
- 研究开始前固定测量方向、切面选择和排除标准。25%/50%/75% 切面是本 skill 的一种方案，不宣称适用于所有研究。
- BV/TV 的区域大小、牙体排除、缓冲区和分割阈值需独立确定并验证。几何位置被接受，不代表分割或 BV/TV 已获验证。
- 不提供通用灰度阈值，不宣称自动定位准确率或观察者一致性。BMD/TMD、骨小梁厚度及间距等需要各自的校准和有效性验证。

## 数据与贡献

请提交合成测试和通用方法改进；不要提交真实扫描、DICOM 元数据、样本映射、诊断图、个人路径或凭据。参见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [SECURITY.md](SECURITY.md)。`.gitignore` 不能清除已提交内容或 Git 历史。

原有私人实验归档及其专用运行脚本不属于此公开发行版。不要将旧研究归档重新合并回公开仓库；个人实验记录应独立保管。

## 许可证

本发行版的原创代码和文档采用 [MIT](LICENSE)，允许其他研究者使用、修改、分发及商业使用，需保留版权与许可声明。MIT 无需向机构申请；发布许可的前提是有权授权相应内容。第三方软件、数据与服务仍遵守各自的许可。
