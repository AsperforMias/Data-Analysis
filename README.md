## 应付实验室折线图生成的

### 由常见py-external libraries生成的气-液双相平衡相图

Background:实验册快到deadline了，需要用到excel去生成一个同物理量的双折线图

ummm老实说原本想问问大智慧的llm，office到底把哪个功能放在哪个页面下，但我发现即使可以使用搜索框，也会碰上个头大的问题。llm生成的阐释与步骤里对功能的描述会存在翻译差异，比如什么“从文本”，“自文本”

而microsoft office的功能项搜索一丁点模糊匹配都没有，~~差一个字它都会跟瞎了一样（~~

有一说一,让我用excel我是根本不知道哪个功能在哪里,怎么做。但python接上扩展库,把const list整理好,只是写计算逻辑和查方法库的问题()

而且对于这些基于某份数据进行图表生成，显然“基于数据分析相关的扩展库模块生成相应代码块”比“直接生成图片”更方便~~于llm )~~

由于数据不多且没有扩展功能必要，就没有做sql而是直接hard-coding了

以后可能还会碰上这种需要excel作图的答辩，所以放个repo在这 )

### Tech Stacks
- **Lang**: Python
- **Libraries**
    - [**NumPy**](https://numpy.org/) : For numerical computing and array operations.
    - [**Matplotlib**](https://matplotlib.org/) : A comprehensive library for creating static, interactive, and animated visualizations in Python.
    - [**Pandas**](https://pandas.pydata.org/) : A powerful tool for data analysis and manipulation.

### License

[MIT](./LICENSE)
