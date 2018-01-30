# P3常见问题汇总

**项目提交重要提示！！！**

- 只要提交PDF文件，不要提交预处理代码（PDF文件内容具体请看模板）；
- 大家一定要每隔5-10分钟就保存一次项目，因为Public版本经常会有未知错误导致软件无法运行，且做的项目也无法保存；
- 一定要保证有4个Dashboard（回答4个问题）和1个Story（深入探索一个问题），并且正确命名；
- 数据预处理不是重点，但不要在可视化里出现明显的问题（比如数据严重失真，变量名称带“|”符号等），否则会视为不符合项目要求；
- 一定要仔细按照要求做项目！要求非常明确，包括需要的图形种类、数量、需要添加的部件等。请大家在满足要求的前提下再自由发挥；
- 个人建议：项目不要求多么复杂的视觉效果，也不需要自定义各种模板背景等。尤其是可视化的类型并不需要非常特殊，按照设计原则，使用最基本的条形图/散点图/折线图等就已经足够了。有时候刻意追求可视化的视觉效果反而会弄巧成拙，请大家注意。

**1. 请问Pages中的Show hisgoty在哪？**

请参阅[此链接](http://onlinehelp.tableau.com/current/pro/desktop/en-us/buildmanual_shelves_pages.html)

**2. 如何进行数据预处理，将Genres等分成多列？**

请参阅[此链接](http://discussions.youdaxue.com/t/tableau/42153/4)

**3. Revenue/Budget有0值，如何处理？**

0值在这个变量中代表的是缺失，而不是真的为0，因此在涉及这两个变量的可视化展示时，应当把为0的数据删除。（但如果展示的变量和这两个无关，则不应该删除）

**4.如何在一个工作簿中使用多个数据源？**

点击下图的Data-New Datasource，这样就可以针对不同问题选择不同的数据源。

![](https://i.imgur.com/p6ElUix.png)

**5.使用Revenue还是Revenue_adj？**

推荐使用后缀为adj的变量，因为其考虑了通货膨胀的影响，更为准确。

**6. 如何区分原创电影和改编电影？**

观察“keyword”字段是否含有“based on novel”。



