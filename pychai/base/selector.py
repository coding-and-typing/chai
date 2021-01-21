from typing import List, Callable, Tuple
from .character import Component
from ..log import chaiLogger

class Selector:
    '''
    选择器
    '''

    def __init__(self, sieveList: List[Callable[[Component], None]]):
        self.sieveList = sieveList

    def __call__(self, component: Component) -> Tuple[int, ...]:
        schemeList = component.schemeList.copy()
        chaiLogger.debug(f'择优列表：{schemeList}')
        for sieve in self.sieveList:
            chaiLogger.debug(f'择优函数：{sieve.__name__}')
            scoreList = [sieve(component, scheme) for scheme in schemeList]
            chaiLogger.debug(f'择优得分：{scoreList}')
            bestScore = min(scoreList)
            schemeList = [scheme
                for scheme, score in zip(schemeList, scoreList)
                if score == bestScore]
            chaiLogger.debug(f'剩余列表：{schemeList}')
        if len(schemeList) == 1:
            # 理论上把字根的二进制表示放进去才完备，但除了 C 输入要用到之外都不用，先不写
            # return tuple(
            #     {
            #         'name': char.powerDict[x],
            #         'slice': x
            #     }
            #     for x in char.schemeList[0])
            return schemeList[0]
        else:
            # 理论上经过选择器序贯处理后应该只剩下一个 scheme。如果不是这样，报错
            raise ValueError('您提供的拆分规则不能唯一确定拆分结果。例如，字「%s」有如下拆分方式：%s' \
                % (component.name, schemeList))
