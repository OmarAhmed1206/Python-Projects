import pandas as pd
import numpy as np


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
#
# df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
#
#                     'group': ['Accounting', 'Engineering',
#
#                               'Engineering', 'HR']})
#
# df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
#
#                     'hire_date': [2004, 2008, 2012, 2014]})
#
# print(display('df1', 'df2'))
#
# df3=pd.merge(df1,df2)
# print(df3)

pop = pd.read_csv('state-population.csv')
areas= pd.read_csv('state-areas.csv')
abbrevs= pd.read_csv('state-abbrevs.csv')
print(display('pop.head(5)','areas.head(5)','abbrevs.head(5)'))
print(pop.info())
print(areas.info())
print(abbrevs.info())
merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged.isnull().any()
print(merged[merged['population'].isnull()])
print(merged.loc[merged['state'].isnull(), 'state/region'].unique())
merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States '
final = pd.merge(merged,areas,on='state',how='left')
print(final)
print(merged.loc[merged['state'].isnull(), 'state/region'].unique())

data2010 = final.query('year == 2010 & ages == "total"') # is the same as final[final['ages'] == 'total' & final ['years'] == 2010]
print(data2010.head(2))




