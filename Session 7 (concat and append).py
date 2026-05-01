import pandas as pd
import numpy as np


def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols }
    return pd.DataFrame(data, ind)

# example DataFrame
# print(make_df('ABC', range(3)))


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


# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# np.concatenate([x, y, z])

# x = [[1, 2],
#      [3, 4]]
# print(np.concatenate([x, x],axis=1))

# ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
# ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
# print(pd.concat([ser1, ser2]))

# df1 = make_df('AB', [1, 2])
# df2 = make_df('AB', [3, 4])
# df3 = make_df('AB', [0, 1])
# df4 = make_df('CD', [0, 1])

# print(df1)
# print(df2)
# print(display('df1', 'df2', 'pd.concat([df1, df2])'))
# print(display('df3', 'df4', "pd.concat([df3, df4], axis='columns')"))
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
# y.index = x.index  # make indices match
# print(display('x', 'y', 'pd.concat([x, y])'))
#
# try:
#     pd.concat([x, y], verify_integrity=True)
# except ValueError as e:
#     print("ValueError:", e)

# print(display('x', 'y', 'pd.concat([x, y], ignore_index=False)'))
# print(display('x', 'y', "pd.concat([x, y], keys=['x', 'y'])"))
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
# print(display('df5', 'df6',
#         "pd.concat([df5, df6], join='inner')"))

# print(pd.concat([df5, df6.reindex(df5.columns, axis=1)]))

# print(display('df1', 'df2', 'df1.append(df2)'))
reviews = pd.read_csv(r"winemag-data-130k-v2 (1).csv", index_col=0)
# reviews.rename(columns={'points': 'score'}) # renames the chosen column
# print(reviews.info())
# reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# reviews.groupby('points').points.count()
# reviews.groupby('points').price.min()























































