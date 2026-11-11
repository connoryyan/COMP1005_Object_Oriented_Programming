# Workshop 全量核对清单

核对日期：2026-11-11。范围：当前工作目录的文件、Project1.zip 内的早期版本、可读取的 Git 提交记录、测试和覆盖率结果。此次只新增审计报告与验证输出，没有继续改动业务源码。

**结论：目前不能认定“全部 workshop 要求已完成”。代码可运行、覆盖率达标，与每节演示、过程记录和提交材料齐全是不同的判断。**

状态说明：满足＝当前实现或明确历史材料满足该任务主要条款；部分＝有明确未满足子项；证据不足＝文件不能证明真实过程；缺失＝当前目录/材料中没有找到；后续演进＝旧阶段要求已被后续明确改变，不应倒退修改。满足一项任务不代表该 workshop 的真人审查记录也满足。

## 本次复核证据

- 完整 pytest：89 passed；核心实现语句覆盖 639/639，新增分支复测 162/162。测试和 main/test 演示入口被 .coveragerc 排除，两个 main 另由回归测试执行。100% 表示现有语句/分支被经过，不能证明未编写的验证规则或所有输入正确。
- pycodestyle 对 Project1/src、Project1/tests、Project2、Q1、ws1-1、a.py 和 tests 通过；注释全文句、语义准确性和架构不是该工具能证明的。
- 当前 UML 检查至 XML/源模型内容层面，没有完成可视化渲染和箭头/排版逐图验收，因此不把 XML 能解析等同于模型完全正确。
- 额外探针重现：Undead 错误类型输入触发 TypeError；dismiss(True) 删除编号 1；独立 Transaction 接受 nan；无效 setter 静默；Finance main 的显式 repr/process/cancel 调用计数均为 0。
- Project1.zip 含 implementation1.py、四类模块、旧 main、README 和 uml.uxf。Git 有早期阶段提交。它们可证明部分增量版本存在，但不能证明每次建模/复测/导师讨论的实际时序。

证据文件：[reports/workshop-audit-coverage.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-coverage.json)、[reports/workshop-audit-branch-coverage.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-branch-coverage.json)、[reports/workshop-audit-probes.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-probes.json)。

## 需要收尾的具体问题

| 编号 | 问题与对应要求 | 建议 |
|---|---|---|
| F01 | 2-2 Task 3 / 3-1、3-2 Task 7：当前 main 无显式四类 repr 展示，无 Pending 交易处理/取消展示；无完整的无效 setter、重复/无效账户、两客户分行关联切换演示。 | 增加清晰、可见且有状态断言的演示。4-2 后交易由账户组合创建；早期 Pending 演示宜单独保留历史示例，避免最终 main 独立构造 Transaction 与后续要求冲突。 |
| F02 | 1-2：初始构造不能表达不同余额；存档通过直接赋值设置，当前第三账户没有资金操作，前后余额输出不完整。 | 保留原始版本，不回填伪装历史。补说明或另做明确标注日期的演示；若当前需要构造初始余额，应受控初始化并定义初始记录规则。 |
| F03 | 2-1 / 3-1、3-2：Branch 操作及部分 setter 拒绝无效输入时无反馈。 | 增加恰当成功/拒绝反馈，并在 main 验证值不被覆盖。 |
| F04 | rubric Criterion 2 的每模块一个类：account.py 三类、exceptions.py 六类、resource.py 两类、undead.py 八类。 | 评分条文字面要求与当前结构不一致。Project3/README 有导师允许相关 actuator 共同模块的记录，但不能自动扩大为所有项目的统一豁免；严格对齐时拆模块并保持兼容导出，或提供明确适用范围的真实说明。 |
| F05 | 文档/注释：ResourceManager docstring 仍列不存在的五个独立私有字段；collect/spend 参数写成 dict[str, Resource]，spend 被描述为 Add；Client.remove_account_number 的 Args 名称错误；多个自然语言注释无大写/句号，部分 docstring 断行生硬。 | 按实际字典结构/参数/职责修正。并非“所有方法必须有 docstring”；rubric 明确要求的是至少一个项目每个类有 class docstring，这一点当前满足。方法文档不全主要影响可理解性和 README 旧声明的一致性。 |
| F06 | UML：last_error property 被列成方法，P2 多数方法缺类型；Necromancer—Undead 的法师端写 1，却存在直接创建/解散后脱离法师的对象；Account—Transaction 也有类似范围问题，standalone Pending 交易无账户归属；uml6 与 current 的最终版本指向还需清楚。 | 明确图只描述“当前受控/组合记录”还是所有合法实例。若描述全体对象，审查 0..1 归属范围；补 property/类型，并实际渲染检查抽象方法、菱形、箭头和布局。不要仅凭自动生成/能解析认定模型准确。 |
| F07 | rubric Criterion 5：高覆盖不等于 HD。Transaction 无独立 fixture；Branch 虽在不同测试类重复定义 fixture，但只有相同的基础数据，未形成多种初始状态；P2 多个被测类型也无多份 fixture；Project3 全部实现/测试缺失，不能声称每项目每类型多 fixture。 | 以正常/边界/不同状态准备多份有实际用途的 fixtures；测试行为而非为 getter 凑行覆盖。同步开发证据需由真实版本历史支持。 |
| F08 | 6-1 全套受控 AI 比较材料未找到，原始 checkpoint 反馈也未找到。 | 单独保留两轮 prompt、两份回答、三方比较、验证和真实讨论记录；本次修复对话不替代。 |
| F09 | 7-1/8-1/9-1/10-1 的 Project3 只有 README。 | 找回实际 simbricks 源码、UML、入口、测试和覆盖率，逐项复核；不能从讨论片段认定实现存在。 |
| F10 | 额外健壮性：Undead(1,"Invalid","bad",10) 抛 TypeError；dismiss(True) 匹配 id=1；Transaction 独立构造接受 nan。仪式 invalid 成本回退会抹去已给出的其它成本，策略需说明。 | 对重要类型/标识进行一致验证；交易金额/结果余额使用有限数规则；缺 Ectoplasm 的输入选择明确拒绝或定义默认策略。原文没要求所有 ID 必须为正，故负 ID 本身不作为明确违规。 |
| F11 | 8-2 Task 3：多账户 Client、按号取账户、操作与过滤目前散落于不同示例，未形成同一条完整 main 流程。 | 用同一 Client 的两种账户，逐个通过 get_account 取回、存取、访问/过滤历史并显示结果。 |
| F12 | 周审查记录不完整、错阶段或缺姓名；10-1 和 6-2 仅标题。 | 按下方周记录矩阵补真实元数据与修改/学习联系；周内可说明共享记录的真实覆盖范围，不捏造会面。 |

## 按 workshop、按 Task 核对

本表逐项保留原文任务编号。原文 3-1 和 3-2 内容完全相同；10-1 从 Task 6 跳到 Task 8，不擅自新增 Task 7。每项链接直达原要求。

### Workshop 1-1

原文：[workshops.md:1](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1)。

结论：**满足当前留存要求**。原文明确此节不要求 Portfolio 实现；[ws1-1/temperature.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/ws1-1/temperature.py) 保留了准备练习。不能把没有 Client/Account 视为此节缺失。

### Workshop 1-2

原文：[workshops.md:9](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:9)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Plan the Initial Classes](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:36) | 部分 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | Client/Account 的职责和属性基本齐全，当前有账户名称、类型和余额；独立的初始规划材料未找到。压缩包早期 Account 只有 id/type/balance，缺少当时要求的额外属性。 |
| [Task 2: Create the Client Class](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:80) | 满足 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py) | 有 Client、构造参数、self、独立实例状态及更改联系方式/活动状态的方法；当前实现可以运行。 |
| [Task 3: Create the Account Class](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:121) | 部分 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 存取款、余额检查、失败反馈、额外显示行为具备。早期和当前账户都固定以 0 开始，余额没有构造参数，不能用构造参数指定不同初始状态；当前 Account 抽象化属于 7-2 的后续演进。 |
| [Task 4: Create the Finance Objects](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:156) | 部分 | [Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py) | 存档 implementation1.py 有三个 Client、三个 Account、至少两类账户、两次存款/取款、超额取款、操作前后输出和独立性演示；但不同初始余额通过直接赋值设置，而不是构造参数/账户行为。当前演示 account_3 未做资金操作，各操作也并非逐次输出前后余额。 |
| [Task 5: Test and Review the Initial Model](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:195) | 部分 | [Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip)、[Project1/tests](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests)、[reports/finance-demo.txt](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/finance-demo.txt) | 有可运行的初版存档、当前行为测试和输出；未能证明初版每个方法均在不同对象上测试至少两次，初始规划材料不足。不能用后来新增测试反推最初已经完成全部测试。 |

### Workshop 2-1

原文：[workshops.md:218](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:218)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Separate the Existing Classes into Modules](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:230) | 满足 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | Client 和 Account 已分模块，main 导入并演示；初版保留在 Project1.zip。 |
| [Task 2: Create the Transaction Class](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:253) | 满足 | [Project1/src/transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/transaction.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 五个字段、Pending 默认值、处理/取消和修改描述均具备；状态机测试确认对象独立且不能取消已处理交易。早期存档也有交易演示。 |
| [Task 3: Create the Branch Class](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:293) | 部分 | [Project1/src/branch.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/branch.py)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py) | 字段、默认关闭/可指定打开、开关分行和修改电话具备；main 有三个分行及状态变化。方法本身不输出反馈，main 的反馈也未紧跟每次操作，严格按逐次反馈要求仍需补齐。 |
| [Task 4: Import the New Classes](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:323) | 后续演进 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | class 模块中不再有普通演示对象创建。当前 main 未直接导入 Transaction，由 Account 内部创建，符合 4-2 后续组合要求。历史上单类/单模块结构已有存档；当前 account.py 有三类，最终 rubric 结构问题见 F04。 |
| [Task 5: Create and Test Instances](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:350) | 部分 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 当前有至少三名客户、三个账户、三个分行和多个交易记录。当前 main 不处理/取消 Pending 交易，也不修改交易描述；存档能证明早期交易演示，但最终演示缺少这些展示。 |
| [Task 6: Review the Expanded Model](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:379) | 部分 | [Project1/src](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 职责和模块导入清楚，增量版本存在；“每模块一个类”当前不严格满足，且 main 未展示每个要求的方法。见 F01/F04。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:402) | 记录较完整 | [README.md:9](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:9) | 日期和 Lance Feldman、问题、反馈、before/after、理由和学习联系齐全；其 process(source,destination) 是历史设计，应注明后来改为账户创建记录，不应当作当前实现说明。 |

### Workshop 2-2

原文：[workshops.md:438](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:438)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Add Readable String Conversions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:450) | 部分 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/src/transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/transaction.py)、[Project1/src/branch.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/branch.py) | 四类均有 __str__，字段大体齐全且返回字符串。账户余额统一两位小数；Transaction 金额使用原始表示，空描述时省略 description，严格按统一货币/包含描述要求仍有差距。 |
| [Task 2: Add Object Representations](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:484) | 满足 | [Project1/src](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 四类均有包含类名和状态的 __repr__；测试覆盖 Client/Account/Transaction/Branch 的表示。无需能重新调用构造函数，这是原文允许的。 |
| [Task 3: Update the Project Demonstration](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:511) | 部分 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | main 显示对象并进行账户/分行/客户操作，但无任何显式 repr() 调用；存档 main 也没有。当前 main 也没有交易 process/cancel 的前后展示。见 F01。 |
| [Task 4: Apply Python Code Style](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:546) | 满足 | [reports/verification.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/verification.md)、[Project1/src](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src) | 已执行 autopep8，当前 pycodestyle 通过；类、模块、方法命名和四空格缩进符合本任务主要要求。自然语言注释和文档准确性仍需人工修整，见通用要求/F05。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:585) | 覆盖范围未标明 | [README.md:9](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:9) | 没有独立 2-2 标题；rubric 要求每周一次，2-1 可能覆盖第 2 周，但未明确包含 2-2。应标注真实覆盖范围，而非捏造第二次会面。 |

### Workshop 3-1

原文：[workshops.md:620](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:620)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Encapsulate the Existing Classes](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:630) | 满足 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/branch.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/branch.py)、[Project1/src/transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/transaction.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py) | 重要状态私有，余额受保护并经行为修改；main 通过属性和方法访问。_balance 的 protected 可见性属于 5-1 后续演进。 |
| [Task 2: Add Getters and Setters](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:653) | 部分 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/branch.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/branch.py)、[Project1/src/transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/transaction.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py) | 客户联系方式、交易描述、分行信息有受控修改方法，余额/状态经行为修改。账户名称目前只读，没有可更新的账户描述信息；若名称属于固定值需明确说明该选择，否则增加适当 setter。 |
| [Task 3: Validate Object Data](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:680) | 部分 | [Project1/src](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py)、[reports/workshop-audit-probes.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-probes.json) | 主要构造器类型检查、bool 排除、金额验证和保留原状态已具备；Client.set_name、Branch 三个 setter 和分行关联拒绝无效输入时静默，缺少原文要求的拒绝反馈；独立 Transaction 仍接受 nan 等非有限数。 |
| [Task 4: Model the Current Finance System](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:708) | 部分 | [Project1/diagrams/uml.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/uml.uxf)、[Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml)、[README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md) | 历史和当前模型存在，四个核心类及关系可核查，3-1 有真实记录文本；模型先于关系实现的过程不能仅凭当前文件证明。当前模型仍有属性/返回类型/多重性范围问题，见 F06。 |
| [Task 5: Implement the First Relationships](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:743) | 部分 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 聚合、空初始集合、类型检查、去重、移除和独立生命周期具备；Branch 关联可变更且存档 main 有两客户两分行和切换。当前 main 未完整重现关联切换及无效关联输入。 |
| [Task 6: Review the Model and Design](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:781) | 部分 | [Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml)、[Project1/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/README.md)、[README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md) | 职责和主要聚合/关联/组合合理，早期版本保留；缺少系统化的 SOLID/设计问题分析，当前 UML 与所有有效实例的对应范围仍需澄清。 |
| [Task 7: Demonstrate the Updated Project](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:814) | 部分 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 当前演示有效业务及部分失败；重复账户、无效对象、无效 setter、分行关联切换等多数在测试或旧存档，未全部在当前 main 展示。pytest 不能替代明确要求 main 的项目。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:841) | 记录较完整 | [README.md:76](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:76) | 日期、Lance Feldman、封装/责任问题、修改和学习反思具备；历史 public id / list 描述需标明是当时状态。 |

### Workshop 3-2

原文：[workshops.md:874](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:874)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Encapsulate the Existing Classes](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:884) | 满足 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/branch.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/branch.py)、[Project1/src/transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/transaction.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py) | 重要状态私有，余额受保护并经行为修改；main 通过属性和方法访问。_balance 的 protected 可见性属于 5-1 后续演进。 |
| [Task 2: Add Getters and Setters](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:907) | 部分 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/branch.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/branch.py)、[Project1/src/transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/transaction.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py) | 客户联系方式、交易描述、分行信息有受控修改方法，余额/状态经行为修改。账户名称目前只读，没有可更新的账户描述信息；若名称属于固定值需明确说明该选择，否则增加适当 setter。 |
| [Task 3: Validate Object Data](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:934) | 部分 | [Project1/src](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py)、[reports/workshop-audit-probes.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-probes.json) | 主要构造器类型检查、bool 排除、金额验证和保留原状态已具备；Client.set_name、Branch 三个 setter 和分行关联拒绝无效输入时静默，缺少原文要求的拒绝反馈；独立 Transaction 仍接受 nan 等非有限数。 |
| [Task 4: Model the Current Finance System](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:962) | 部分 | [Project1/diagrams/uml.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/uml.uxf)、[Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml)、[README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md) | 历史和当前模型存在，四个核心类及关系可核查，3-1 有真实记录文本；模型先于关系实现的过程不能仅凭当前文件证明。当前模型仍有属性/返回类型/多重性范围问题，见 F06。 |
| [Task 5: Implement the First Relationships](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:997) | 部分 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 聚合、空初始集合、类型检查、去重、移除和独立生命周期具备；Branch 关联可变更且存档 main 有两客户两分行和切换。当前 main 未完整重现关联切换及无效关联输入。 |
| [Task 6: Review the Model and Design](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1035) | 部分 | [Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml)、[Project1/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/README.md)、[README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md) | 职责和主要聚合/关联/组合合理，早期版本保留；缺少系统化的 SOLID/设计问题分析，当前 UML 与所有有效实例的对应范围仍需澄清。 |
| [Task 7: Demonstrate the Updated Project](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1068) | 部分 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py)、[Project1.zip](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1.zip) | 当前演示有效业务及部分失败；重复账户、无效对象、无效 setter、分行关联切换等多数在测试或旧存档，未全部在当前 main 展示。pytest 不能替代明确要求 main 的项目。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1095) | 覆盖范围未标明 | [README.md:76](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:76) | 没有独立 3-2 标题；同周 3-1 可作为每周记录的候选，需注明实际覆盖范围。原文 3-1 和 3-2 内容逐字相同，不要求倒退或复制代码。 |

### Workshop 4-1

原文：[workshops.md:1128](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1128)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Model Project 2](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1142) | 部分 | [Project2/UML1.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/UML1.uxf)、[Project2/UML2.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/UML2.uxf)、[Project2/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/current.puml) | 已有早期和当前 UML，资源、仪式、亡灵、法师、职责及主要关系具备；先画图后编码的时序证据不足，P2 多个方法无参数/返回类型，当前图也未补全；见 F06。 |
| [Task 2: Implement the Resource System](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1182) | 满足 | [Project2/resource.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/resource.py)、[Project2/test.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/test.py) | 五类资源均用 Resource 保存私有非负整数，quantity 只读；字典统一提供资源访问。批量收集/校验/整体扣除、最小常量及字符串输出具备，失败不会部分扣除。ResourceManager 是 ResourcePool 职责的等价实现，无需只因名字不同而改名。 |
| [Task 3: Implement the Initial Undead](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1219) | 后续演进 | [Project2/undead.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/undead.py)、[Project2/test.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/test.py) | 标识、名称、生命、力量、等级、上下限、成长、最高等级、只读属性和字符串输出齐全。生命/力量/等级现为 protected，符合 5-2 的后续要求，不应为满足旧阶段再全部改回 private。构造参数非法类型仍有额外健壮性问题，见 F10。 |
| [Task 4: Implement Summoning Rituals](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1257) | 满足 | [Project2/ritual.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/ritual.py)、[Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[Project2/test.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/test.py) | 仪式保存名称、起始状态、五项成本和具体召唤类型；每个仪式有 Ectoplasm，可检查/消耗/创建亡灵，main 有四种既有仪式。异常成本默认策略和具体子类边界的一致性建议见 F10。 |
| [Task 5: Demonstrate the Initial Project 2 Classes](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1304) | 后续演进 | [Project2/test.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/test.py)、[Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[Project2/UML1.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/UML1.uxf) | 独立资源/仪式/亡灵/升级在原测试中可查，当前 main 已按 4-2 连接全系统；不应为了“暂不连接完整系统”删除后续实现。独立阶段的完整前后输出和最初运行时点证据有限。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1337) | 缺少映射 | [README.md:172](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:172) | 没有 4-1 标题；4-2 有资源设计讨论，是否也覆盖第 4 周前半课需真实说明，且审查人/学习联系不完整。 |

### Workshop 4-2

原文：[workshops.md:1370](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1370)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Complete the Necromancer](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1379) | 满足 | [Project2/necromancer.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/necromancer.py)、[Project2/tests/test_summoning.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/tests/test_summoning.py) | 法师内部组合 ResourceManager，私有列表和递增 ID、容量限制、仪式验证、召唤、查找帮助方法、按 ID 解散和升级具备。先构造再扣费是保护失败状态的实现选择，不改变对象职责。 |
| [Task 2: Demonstrate the Connected Summoning System](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1417) | 满足 | [Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[reports/necromancy-demo.txt](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/necromancy-demo.txt)、[Project2/tests/test_summoning.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/tests/test_summoning.py) | 四类召唤、资源消耗、失败、补资源重试、按法师升级、解散和最终状态均有演示；失败资源保护另有断言。UML 的精确类型/多重性仍归 F06。 |
| [Task 3: Refine Project 1 with Properties and Composition](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1457) | 满足 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py) | 适当属性化，ID/余额只读，账户内部私有 helper 创建交易、记录金额/结果余额、内部持有列表并返回副本；成功/失败及组合行为均已测试和演示。main 不直接构造 Transaction 符合此阶段要求。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1496) | 部分 | [README.md:172](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:172)、[Project2/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/README.md) | 有日期、资源拆分/字典/参数选择和示例；缺审查人姓名，修改结果与学习联系不够完整，多个文件重复。 |

### Workshop 5-1

原文：[workshops.md:1529](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1529)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Model the Account Inheritance Hierarchy](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1541) | 部分 | [Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml)、[Project1/diagrams/uml5.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/uml5.uxf) | 父类、两种子类、常量、利率、组合和 Client 聚合存在；get_type 从具体类推导，设计合理。先更新图再编码无法由当前状态证明；当前图存在 F06 的表达问题。 |
| [Task 2: Refactor Account as the Parent Class](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1580) | 满足 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py) | 共享字段、存取款验证、余额与交易创建集中在父类；ID/余额只读，交易列表不能从外部替换；protected 只用于继承相关行为。 |
| [Task 3: Implement the Specialised Accounts](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1613) | 满足 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/tests/test_savings_account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_savings_account.py)、[Project1/tests/test_everyday_account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_everyday_account.py) | 两种子类使用 super，具有利率/最低余额或单次上限，并覆盖 withdraw。具体规则通过覆盖 _check_withdrawal 在父类 withdraw 中动态调用，先验证后规则再扣款，属于有效的复用设计，无需复制父类逻辑。 |
| [Task 4: Integrate the Inheritance Hierarchy](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1651) | 满足 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1/tests/test_integration.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_integration.py) | 同一 Client 接受两种具体账户，存款、有效/无效取款、isinstance、交易记录和不同规则均有演示。图的精确一致性单列 F06。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1690) | 部分 | [README.md:261](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:261) | 有日期及资源参数验证/取舍讨论，但无审查人，主要内容是 Project2，未对应本节 Finance 继承任务；需要真实说明审查对象和结果。 |

### Workshop 5-2

原文：[workshops.md:1723](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1723)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Model the Undead Inheritance Hierarchy](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1732) | 部分 | [Project2/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/current.puml)、[Project2/UML2.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/UML2.uxf) | Undead、两个中间父类、四种具体类及关系正确，protected 状态和 command 方法可查；先图后实现及完整参数/返回类型仍未充分证明。 |
| [Task 2: Implement the Undead Hierarchy](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1770) | 满足 | [Project2/undead.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/undead.py)、[Project2/test.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/test.py) | 共同状态/升级在父类，Warrior/Cursed 使用 super 构造并合作覆盖 command，四类使用自己的边界，保留既有起始强度并共享升级。 |
| [Task 3: Connect Specialised Summons to the Existing System](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1819) | 满足 | [Project2/ritual.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/ritual.py)、[Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[Project2/test.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/test.py) | 仪式标识具体类型，按法师提供 ID 创建四类，Rune/Ectoplasm 成本和资源职责保留；有类型检查、升级和不同 command 演示。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1857) | 覆盖范围未标明 | [README.md:261](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:261) | 没有 5-2 标题；第 5 周已有记录但未明确覆盖此节，未找到亡灵继承的完整审查→修改→反思证据。 |

### Workshop 6-1

原文：[workshops.md:1890](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1890)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Respond to Checkpoint Feedback](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1900) | 证据不足 | [DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md)、[README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md) | 有当前修复和运行记录，但未找到原始 checkpoint 反馈，无法逐条对应反馈→实现→UML→复测→审查反思；不能把本次 AI 维护替代当时课程反馈。 |
| [Task 2: Create a Baseline AI Prompt](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1937) | 缺失 | [DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md) | 未找到基准 prompt、基于问题描述生成的第一份独立回答及保存文件。本次向 AI 提供现有源码做修复不等于该受控实验。 |
| [Task 3: Evaluate the Baseline Response](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:1965) | 缺失 | [DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md) | 未找到原解与基准回答在类、属性、方法、关系、继承、验证/封装、课程约束等方面的逐点比较和 OOP 理由。 |
| [Task 4: Improve the Prompt](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2002) | 缺失 | [DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md) | 未找到 Context/Goal/Existing Design/Requirements/Constraints/Output 六部分改进 prompt，以及与评估项目分开的第二份回答。 |
| [Task 5: Compare the Two AI Responses](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2036) | 缺失 | [DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md) | 未找到第一/第二回答之间的变化、剩余问题、过度约束风险以及改进是否有效的论证。 |
| [Task 6: Verify Before You Trust](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2068) | 缺失 | [DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md) | 未找到对一份生成实现的运行验证、遗漏/假设/不必要复杂度检查，及选定设计决策的解释和同伴讨论记录。不可补造历史讨论。 |

### Workshop 6-2

原文：[workshops.md:2096](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2096)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Extend the Project 2 Model](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2106) | 部分 | [Project2/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/current.puml)、[Project2/UML3.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/UML3.uxf) | DeathKnight 双父类、diamond、起始/边界/成长常量及 combat_style/compare 方法都有；未证明先图后代码，方法类型和脱离法师状态的多重性见 F06。 |
| [Task 2: Implement the DeathKnight](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2147) | 满足 | [Project2/undead.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/undead.py)、[Project2/tests/test_summoning.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/tests/test_summoning.py) | Warrior/Cursed 提供 combat_style，DeathKnight 按相同顺序多继承，起始 100/80 高于四种既有召唤物，独立边界/成长常量，super 构造、isinstance 均具备。 |
| [Task 3: Investigate Ambiguity and the MRO](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2180) | 满足 | [Project2/undead.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/undead.py)、[Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[Project2/tests/test_summoning.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/tests/test_summoning.py) | 覆盖 combat_style 调用 super，显示 MRO；compare 显式调用两父类，测试验证 Warrior 优先且 Undead 在 MRO 只出现一次。 |
| [Task 4: Integrate and Demonstrate the Death Knight](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2209) | 满足 | [Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[Project2/tests/test_summoning.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/tests/test_summoning.py) | 五种成本均为 8，高于旧仪式；经 Necromancer 正常召唤，展示类型/MRO/两种调用、通过法师 command/level_up。源模型对应主要结构，精确问题单列 F06。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2252) | 缺失 | [README.md:295](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md:295) | 只有带日期的标题，无实际讨论、审查人、修改或学习联系。 |

### Workshop 7-1

原文：[workshops.md:2286](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2286)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Finalise Project 2](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2295) | 部分 | [Project2/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/main.py)、[Project2/undead.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/undead.py)、[Project2/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project2/current.puml) | 完整游戏演示包含五类召唤及死亡骑士，资源/升级/指令均可运行。仍有文档失配、未使用导入、UML 类型等收尾项；undead.py 的旧 __main__ 演示与最终 main 部分重复。 |
| [Task 2: Choose Your Creative Piece](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2320) | 部分 | [Project3/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md) | simbricks、设备/端口/时钟/齿轮等讨论能间接识别机器人仿真领域；缺少独立、清晰的程序说明、可操作范围和对象行为概述。 |
| [Task 3: Begin the Object Model](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2352) | 缺失 | [Project3/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md)、[case.uxf](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/case.uxf) | 本目录没有 Creative Piece 的有效 UML/类关系图。根目录 case.uxf 是空图，不能作为 Project3 模型。 |
| [Task 4: Build the Foundation](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2381) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 未找到 Project3 Python 源码、构造器、模块、受控状态、字符串转换或 main.py；README 中示例片段不能代替可运行实现。 |
| [Task 5: Apply the Concepts You Have Learned](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2400) | 证据不足 | [Project3/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md) | 有 Device(ABC)、集合等讨论片段，但没有完整实现核对合理的关系、常量、helper、继承/覆盖/super、抽象与多态。ABC 基类片段本身也不能证明具有抽象方法。多继承仅要求有真实用途时使用，不强行要求 Project3 增加。 |
| [Task 6: Create an Initial Creative Piece Demonstration](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2432) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有 main.py 或可运行的多对象交互/继承/多态演示，也没有对应模型；无法检查一致性或后续扩展计划。 |
| [Task 7: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2448) | 缺少映射 | [Project3/README.md:3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:3) | 7-2 下有 Creative Piece 讨论可作为同周候选；缺审查人及明确的题号/阶段对应，不自动认定完整。 |

### Workshop 7-2

原文：[workshops.md:2479](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2479)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Make Account Abstract](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2487) | 满足 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | Account(ABC) 有 abstractmethod withdraw，两子类满足接口；pytest 直接创建 Account 并验证 TypeError。当前 main 移除直接创建，符合本 workshop Task 3，并非矛盾。 |
| [Task 2: Demonstrate Account Polymorphism](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2505) | 满足 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1/tests/test_integration.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_integration.py) | 通过同一 withdraw 行为操作两种具体类型，1500 余额取 1200 时结果不同；业务调用不以具体类型分支选行为，存款和交易保留。 |
| [Task 3: Update the Project 1 Model and Demonstration](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2520) | 部分 | [Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py) | main 不创建 Account，具备明确多态示例和对象关系；模型标记抽象类/抽象行为及继承。模型形式/精确表达尚需 F06 的人工确认。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2538) | 部分 | [Project3/README.md:3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:3) | 有日期和 simbricks 结构/ABC 讨论，但未记录审查人；本节材料是 Project3 而非 Finance 抽象任务。可据实说明同周覆盖范围。 |

### Workshop 8-1

原文：[workshops.md:2571](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2571)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Choose Your Data Structures](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2578) | 部分 | [Project3/README.md:28](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:28) | 记录解释了 SimClock 集合去重/顺序不重要适合 Set、齿轮顺序适合 List；能证明选择理由的一部分，但未找到两结构在最终类中的实际实现。 |
| [Task 2: Implement the Data Structures](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2597) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有类实现可证明两种数据结构经对象行为维护、封装或存储对象。 |
| [Task 3: Extend the Creative Piece](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2615) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有可核对的添加/删除/查询/集合操作/过滤等领域行为，也没有更新后的 UML。 |
| [Task 4: Demonstrate the Data Structures](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2634) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 无 main.py，无法证明两结构均被有意义地填充、展示各自特点并与模型对应。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2648) | 部分 | [Project3/README.md:28](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:28) | 有日期、Set/List 选择、before/after、并发与模块讨论，信息有价值；缺审查人，当前源码无法核实修改确已落地。 |

### Workshop 8-2

原文：[workshops.md:2681](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2681)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Store Client Accounts in a Dictionary](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2688) | 满足 | [Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 整数账户号作字典 key，Account 作 value，添加/去重/查询/按号删除齐全，集合返回副本，字符串遍历使用 values。 |
| [Task 2: Manage Transactions with a List](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2708) | 满足 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/tests/test_transaction.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_transaction.py) | 交易按顺序保存在 list，存取款自动创建，返回副本，列表推导按类型/状态/金额过滤，整数/浮点边界均支持。 |
| [Task 3: Use the Structures Through Existing Behaviour](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2727) | 部分 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[Project1/tests/test_integration.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_integration.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | main 分别展示多账户 Client 和按号取账户操作，但未串成“同一多账户 Client→按号取两种账户→多次存取→取回交易→过滤”的完整可见演示。自动测试证明许多子行为，仍应补齐 main 的单条业务流程。 |
| [Task 4: Update the Project Model](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2742) | 部分 | [Project1/diagrams/current.puml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/diagrams/current.puml) | 字典/list、Client 多重性、Account 抽象层次和交易组合均有；standalone Transaction 对归属多重性的影响和 property 表达等见 F06。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2756) | 覆盖范围未标明 | [Project3/README.md:28](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:28) | 没有 Finance 8-2 记录；第 8 周 Project3 讨论不能证明 Finance 数据结构已被审查。是否共享周记录需真实标明。 |

### Workshop 9-1

原文：[workshops.md:2789](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2789)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Identify What Needs Testing](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2796) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有 Project3 实现或行为测试计划可核对成功/失败/边界场景。 |
| [Task 2: Create the Pytest Test Suite](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2821) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有 Project3 的 pytest 模块，无法检查每类测试、approx 或有意义的断言。 |
| [Task 3: Create and Use Fixtures](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2843) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有针对 Creative Piece 的可复用 fixtures、已填充对象或关联对象设置。 |
| [Task 4: Test Object Interactions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2861) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有 Creative Piece 对象关系、集合、继承/多态和失败后状态的交互测试。 |
| [Task 5: Measure Code Coverage](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2876) | 缺失 | [reports/coverage.xml](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/coverage.xml)、[Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 现有 100% 覆盖率只包括 Project1/Project2，不能作为 Project3 的覆盖率报告；Project3 未纳入测试或 coverage source。 |
| [Task 6: Run the Complete Test Suite](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2899) | 缺失 | [pytest.ini](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/pytest.ini)、[Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 当前 suite 不包含任何 Project3 测试，不能声称其所有类/fixtures/覆盖率/正常演示已验证。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2919) | 缺少映射 | [Project3/README.md:81](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:81) | 有 9-2 标题的同周记录，但没有 Project3 测试计划/实际 suite/覆盖率变化，不能代替本节结果。 |

### Workshop 9-2

原文：[workshops.md:2952](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2952)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Identify Testable Behaviour](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2959) | 部分 | [Project1/tests](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 测试涉及全部六个具体 Finance 类型、继承父类行为、成功失败和边界。少量断言只是读取 Transaction getter 值，不能以覆盖 getter 为测试目的；应融入行为场景。 |
| [Task 2: Create the Project 1 Test Suite](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:2985) | 满足 | [Project1/tests](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests) | 按 pytest 命名划分模块，共享账户经具体子类测试；储蓄最低余额、日常上限、失败不变、交易状态、Client 字典等均有有意义断言。 |
| [Task 3: Use Pytest Fixtures](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3011) | 满足 | [Project1/tests/test_account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_account.py)、[Project1/tests/test_client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_client.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 已使用已知余额 Savings/Everyday 和有关联账户 Client 等 fixtures，行为在测试体执行。若目标 HD，还需每个被测类多份有实际用途的 fixture，当前仍有缺口，见 F07。 |
| [Task 4: Test Finance Object Interactions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3029) | 满足 | [Project1/tests/test_integration.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_integration.py)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 测试 Client/Account/Transaction 交互、顺序、失败不变和两子类的同一接口规则；按 Client.get_account 查找后保留对象引用的行为也有测试。 |
| [Task 5: Measure and Improve Code Coverage](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3044) | 满足 | [reports/workshop-audit-coverage.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-coverage.json)、[reports/workshop-audit-branch-coverage.json](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/workshop-audit-branch-coverage.json) | 重新运行后 Finance 全部计入的实现语句/分支均达 100%；排除了测试和 main 演示文件，后者另有回归执行。高覆盖率不是所有场景正确的证明，见新探针。 |
| [Task 6: Run the Complete Finance Test Suite](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3064) | 满足 | [reports/verification.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/verification.md)、[Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 本次重跑完整 suite 89 通过，其中包含 Finance main 执行；全部 Finance 具体类型和交互均有测试。同步开发过程不能由本次重跑证明，属于 rubric 独立证据。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3084) | 部分 | [Project3/README.md:81](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:81) | 有日期与 fixtures/模块讨论，缺审查人和清晰的改后证据/学习联系。关于 fixture 是常量或跨测试共用同一对象的概括不准确：默认 function scope 会为每个测试创建新对象；应保留原问答并另加纠正反思。 |

### Workshop 10-1

原文：[workshops.md:3117](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3117)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Identify Exceptional Situations](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3124) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有异常场景清单/触发条件和领域信息记录。 |
| [Task 2: Create Custom Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3140) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有 Creative Piece 自定义异常类。Finance 的异常不能代替 Project3 异常。 |
| [Task 3: Raise Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3155) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有领域行为实现可核查 raise 时点与失败前状态保护。 |
| [Task 4: Handle Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3169) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有负责类内部的 try/except、错误反馈或继续运行逻辑可核对。 |
| [Task 5: Test Raised Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3183) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 没有 Creative Piece pytest.raises、异常信息或失败状态保持测试。该任务明确要求直接观察异常的测试，不能用 Finance last_error 测试代替。 |
| [Task 6: Demonstrate the Updated Creative Piece](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3203) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 无 main 正常/失败/恢复演示，无法核对继承/抽象/结构保留。 |
| [Task 8: Finalise Project 3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3217) | 缺失 | [Project3](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3) | 原文编号从 Task 6 跳到 Task 8；按原编号审计。缺少实现、模型、测试、覆盖率和入口，无法完成最终提交检查。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3251) | 缺失 | [Project3/README.md:126](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project3/README.md:126) | 只有带日期的标题，无讨论正文。 |

### Workshop 10-2

原文：[workshops.md:3284](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3284)。

| 原任务 | 结论 | 证据 | 核对与未满足子项 |
|---|---|---|---|
| [Task 1: Identify Finance Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3291) | 部分 | [Project1/src/exceptions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/exceptions.py)、[Project1/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/README.md) | 已识别无效金额、余额不足、最低余额、单次上限和账户不存在；触发原因在代码中，建议集中记录每种异常的触发/消息/恢复/状态约定。 |
| [Task 2: Create Custom Finance Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3308) | 满足 | [Project1/src/exceptions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/exceptions.py)、[Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py) | 自定义异常统一继承 FinanceError(Exception)，覆盖真实业务限制；主要消息包括账号、金额、余额或上限。极大数/非法筛选消息较简短但可用。 |
| [Task 3: Raise and Handle Exceptions](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3323) | 满足 | [Project1/src/account.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/account.py)、[Project1/src/client.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/client.py)、[Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py) | 规则处 raise，负责类内部 catch；先验证后变更，失败不改余额/交易/账户集合；main 无 try/except。 |
| [Task 4: Extend the Project 1 Test Suite (Optional)](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3338) | 部分 | [Project1/tests/test_regressions.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/tests/test_regressions.py) | 此 Task 为 Optional，未做完不计为必做缺失。现有测试验证异常类型和失败原子性，但未断言多数异常消息关键信息。公开方法内部捕获，所以不应强行对 deposit/withdraw 使用 pytest.raises。 |
| [Task 5: Update the Finance Demonstration](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3356) | 满足 | [Project1/src/main.py](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/src/main.py)、[reports/finance-demo.txt](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/finance-demo.txt) | 同时展示 Savings/Everyday、正常和失败取款、无效金额、缺失账户、继续成功操作及 Client/Account/Transaction 交互；模型精确问题仍归 F06。 |
| [Task 6: Finalise Project 1](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3371) | 部分 | [Project1](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1)、[reports/verification.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/reports/verification.md)、[DEVELOPMENT_NOTES.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/DEVELOPMENT_NOTES.md) | 代码/测试/演示可运行，核心覆盖率足够；当前每模块一类、文档、最终演示、UML、每周反馈/原始 checkpoint/AI 对比材料仍有缺口，不能认定提交材料全部完成。 |
| [Task: Record Your Weekly Code Review](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/workshops.md:3402) | 缺失 | [Project1/README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/Project1/README.md)、[README.md](D:/Users/Connor/Work/COMP1005_Object_Oriented_Programming/README.md) | 没有第 10 周 Finance 异常处理的真人审查记录；AI maintenance 不能冒充导师审查。 |

## Weekly Code Review 解释与证据

每节原文都重复要求写当前 workshop 标题、日期、审查人、反馈、修改证据和学习联系；最终 rubric 写每周一次。因此这里同时检查单节映射与每周实际记录，不机械要求每周伪造两次会面。若一条真实周记录覆盖两次 workshop，可如实注明范围。

目前第 2 周和第 3 周记录较完整；第 4/5/7/8/9 周有内容但元数据、主题映射或结果证据不足；第 6/10 周有空标题或缺失。日期/姓名的真实性只能由本人确认，此审计只核查记录是否包含它们。AI 维护日志不计为导师 review。

## 最低要求与最终 rubric 交叉检查

| 要求 | 当前结论 |
|---|---|
| 两种结构有意义使用 | Project1 为账户 dict + 交易 list；Project2 为资源 dict + 亡灵 list，均有实际行为。Project3 无实现，不能核对。 |
| 代码 79 / docstring 72、缩进、空白 | pycodestyle 通过；业务源码 docstring 长度另有人工/脚本检查记录。源码中的自然语言注释大写/句号未全部符合。 |
| Imports | 无逗号合并两个 import 语句或通配符；from module import 多个名称属常见 Python 形式。如果课程对“each on separate lines”采用更严格解释，可拆开，不把工具通过等同于导师认可。 |
| snake_case / PascalCase | Finance 与 Necromancy 核心命名符合；独立练习 Q1/p4.py 的 ID 大写实例字段、product1 等与标准 snake_case 不完全一致，若该练习也纳入同一评估范围应统一。 |
| 异常由负责类处理 | Finance 业务类内部 raise/catch，main 不使用异常处理，符合核心最低要求；Project3 未知。P2 非法输入探针仍有未处理 TypeError。 |
| main 集成演示 | 两项目都有可运行 main；Finance 指定展示和完整 8-2 流程仍缺，见 F01/F11。 |
| 标准库和教学内容 | 核心只依赖标准库；pytest/cov/格式化工具属开发验证依赖。未用外部业务框架。具体未教过概念是否可用需按课程材料，不臆造禁止条款。 |
| Criterion 1：OOP/模型 | Finance 抽象/继承/多态、聚合/关联/组合及 P2 多继承有实现。UML 精确性/过程/SOLID 理由及 Project3 材料不完整。 |
| Criterion 2：实现/结构 | 常规路径和现有测试通过；一模块多类、部分冗余演示/未使用导入及缺失子要求影响“全部遵循”。 |
| Criterion 3：异常/结构 | Finance 两结构与内部异常满足主要功能；P2 结构合理但非法输入仍有缺口；Project3 不可审。 |
| Criterion 4：专业实践 | 所有当前 Finance/P2 类已有 class docstring，因此满足至少一个项目每类 class docstring；具体字段说明/注释句式仍需修正。 |
| Criterion 5：测试 | P1/P2 覆盖率超过 95%，但未满足每被测类型多 fixtures/每项目源码齐全等全部 HD 条件；不据此给出分数保证。 |
| Criterion 6：增量/反馈 | ZIP、旧 UML、Git 历史提供部分真实增量证据；每周完整 review 和学习联系不足，不可用当前最终状态回填历史。 |

## 建议处理顺序

1. 找回 Project3 的实际实现并加入审计；它影响多节 workshop 和最终多个 criterion。
2. 补 Finance 当前 main 的规定演示和完整 8-2 业务流程；保留早期阶段演示时明确与 4-2 组合规则的阶段区别。
3. 修复新增非法输入探针、setter 反馈、文档和模块结构问题。
4. 精确校正并渲染最终 UML，明确 current 是当前版本、其它是历史快照。
5. 补真实 weekly review、checkpoint 反馈映射和 6-1 AI 比较材料；不生成伪造的历史。
6. 修改实现后重新执行测试/覆盖率/入口验证，并按此清单复核，而不是只看测试绿灯。
