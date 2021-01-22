[![Build Status](https://github.com/hanzi-chai/chai/workflows/test/badge.svg)](https://github.com/hanzi-chai/chai/actions) [![Build Status](https://github.com/hanzi-chai/chai/workflows/documentation/badge.svg)](https://github.com/hanzi-chai/chai/actions) [![Coverage](https://codecov.io/gh/hanzi-chai/chai/branch/master/graph/badge.svg)](https://codecov.io/gh/hanzi-chai/chai/) [![Dev](https://img.shields.io/badge/docs-dev-blue.svg)](https://hanzi-chai.github.io/chai/)

昔有仓颉作书，天雨粟，鬼夜哭；今有落萧拆字，以程序之力，解世纪难题。时值元旦，万象更新，特奉上「汉字自动拆分系统」1.0，以飨码者！

---

自上世纪七十年代以来，无数的汉字编码方案经由不同的作者提出、发展、兴盛或是衰亡。今天，计算机的运算能力得到了空前的发展，然而其在汉字编码方案中应用的潜力从未被充分挖掘，绝大多数编码方案的作者仍然在使用人工拆分的方式对汉字编码。人工拆分的任务量繁重，增删一个字根就需要找出多处拆分结果进行改动，这大大降低了编码优化的效率。因此，自动化程度的提高，已经成为制约当前汉字编码方案发展的重大问题。

「汉字自动拆分系统」就是为了解决这一难题而诞生的。总览众多现行方案的拆分特点，我们抽象出了一套通用的汉字拆分框架，通过枚举可能字根的方式最大程度满足不同方案的需求，并将拆分规则以组件化的形式集成在框架中，方便用户进行调用。

现在，您只需要在配置文件中指定您的汉字编码方案所使用的字根以及拆分规则，然后运行自动拆分程序即能得到汉字拆分表，再结合编码规则即能快速输出码表。输入方案的制作从未如此简单！

汉字自动拆分系统已经封装为 Python 3 的模块包，您可以通过「pip3 install pychai」命令从 PyPI 获得。源代码及用户文档请参见 GitHub，用户名为 lanluoxiao，仓库名为 Chai。您也可以在「汉字自动拆分系统开发」中与我们一同讨论、开发。

汉字自动拆分系统以 GPL v3 协议发布，如果您的应用程序中使用了该系统的成果，请按相关规范处理。

---

下面简单说明一下汉字自动拆分系统中所蕴含的思想的发展史。

嵌套拆分的思想为汉字编码爱好者团体所熟知，它通过将汉字表示为基本部件的方式迭代生成汉字的拆分，大大降低了汉字拆分的工作量。然而，对于大多数形码方案而言，嵌套拆分仍然需要我们手动拆分数百字。我们能否在自动化的程度上更进一步？

2015 年 11 月，在百度贴吧关于「汉字信息及分部表」的讨论中，吧友逆卷炎灵提出「笔画表达式」这一概念，将汉字表达为笔画种类信息和笔画位置关系信息的字符串，通过串与串的运算得到拆分结果。2017 年我曾成功实现该方法，但发现难以确定位置关系量化的标准，容易损失信息或加入过多信息，这一尝试也就此搁置。汉字自动拆分真的是可能的吗？那时我已经基本给出了否定的答案。

2018 年的一天，在与他人讨论的过程中，我突然想到：汉字的本质是矢量图形，因而任何量化都是不完备的。但是，如果我们按笔画为单位直接存储图形信息，然后在运行时动态提取我们需要的信息完成拆分，就可以很好地解决数据库不完备的问题。虽然学业繁忙，但在漫长的时间中，这一想法如同一颗具有生命活力的种子，逐渐扎根于心中，并得到了不断的丰富与完善……

2019 年 11 月，这一想法已经孵化成熟，我将其总结为一篇论文并从数学上严格证明了自动拆分的可行性。此后的两个月中，我组建了「汉字自动拆分系统开发」讨论群，与群友一起深入交流，解决了无数实现中的难题，并将程序优化到相当高效而不失整洁的地步。

念念不忘，必有回响。汉字自动拆分系统的实现离不开很多人的鼎力支持，在发布之际，我感到非常有必要对他们表示感谢：

- Wayne，经常与我深入讨论输入法相关话题，见证了自动拆分的想法从零开始一步一步发展至今，并利用高超的 Python 架构水平搭建了现有的代码架构；
- Yb，共同奠定了数据库形式的基础，并且是退化映射的主要研究者；
- 逆卷炎灵，其笔画表达式概念直接给予了我灵感，并且提供了嵌套拆分表；
- 参与汉字信息及分部表计划的其他成员：mgcgogo、听雨、分级、雷纳德南等在贴吧的讨论揭示了设计过程中可能遇到的问题；
- 汉字自动拆分系统群友：BX、c後、Chilly Forest、老大鸽、MoGu、秋风、William8915、孖墨、佚名等在群里进行了热烈的讨论；
- 编码方案：五笔（各种版本）、郑码（及真码）、二笔（各种版本）、现代五笔、希码、C、张码、仓颉、四角号码等不同方案的接触让我能够抽象出通用的拆分框架；
- 开源中文项目文泉驿：提供了关键的汉字笔画数据。

蓝落萧
2020 年 1 月 1 日

