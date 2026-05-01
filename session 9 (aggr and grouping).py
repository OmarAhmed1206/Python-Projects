import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):  # number of words
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

# print(sns.get_dataset_names())
# planets = sns.load_dataset('planets')
# print(planets.shape)
# print(planets.info())
# print(planets.describe())
# planets.groupby('method')['method'].count()
# planets['method'].value_counts()

# print(planets.groupby('method')['year'].describe().unstack())

# rng = np.random.RandomState(0)
# df = pd.DataFrame({'key': ['A','B','C','A','B','C'],
#                    'data1': range(6),
#                    'data2': rng.randint(0,10,6)},
#                   columns = ['key','data1','data2'])
# print(df)
# print(df.groupby('key').mean())
# print(df.groupby('key').aggregate(['min',np.median,max,sum]))
# print(df.groupby('key').aggregate({'data1': 'min',
#                                    "data2": 'max'})) # .aggregate is something to use when you want multiple things done

def filter_func(x):
    return x['data2'].std() >4

# display('df',"df.groupby('key').std()","df.groupby('key').filter('filter_func')")

# planets['decade'] = 10 * (planets['year']//10)
# groupedby = (planets.groupby(['method','decade'])['number'].sum().unstack())
# print(groupedby)


# print(titanic.head())
# print(titanic.info())
# print(titanic.groupby(['sex','class'])['survived'].aggregate('mean').unstack())
# print(titanic.pivot_table(values='survived',index='sex',columns='class',aggfunc='mean'))
# age = pd.cut(titanic['age'], [0,10,50,90])
# print(titanic.pivot_table('survived', ['sex',age], 'class', aggfunc=sum))
# fare = pd.qcut(titanic['fare'],4)
# age = pd.qcut(titanic['age'],4)
# print(titanic.pivot_table('survived', ['sex',age],[fare,'class'], dropna=True,sort=True))
# print(titanic.pivot_table(index='sex',columns='class',
#                           aggfunc={'survived':sum,
#                                    'fare': 'mean'}))

# print(titanic.pivot_table('survived',index='sex',columns='class',margins_name='summery', margins=False))



df = pd.read_csv('births.csv')
# print(df.head(2))
# print(df.info())
df['year'] = 10 * (df['year'] // 10)
# print(df.pivot_table('births',index='year', columns='gender',aggfunc='sum'))
print(df.pivot_table('births',index='year', columns='gender',aggfunc='sum').plot())
print(plt.show())














