import numpy as np
from matplotlib import pyplot as plt

import matplotlib as mpl
import pandas as pd
import seaborn as sns


from stacked_bar import Bar
#mpl.style.use('seaborn-colorblind');
mpl.style.use('tableau-colorblind10')
#ax1.tick_params(axis='both', which='major', labelsize=16)





vec0=np.array([10, 1, 3, 7, 8])
list_fields0=['A0', 'B0', 'C6', 'D5', 'E8']
dfa=pd.DataFrame({'field':list_fields0} )
dfa['num']=vec0
dfa['category']='original'


df_v=dfa.copy();
df_v.at[0, 'num']=3
df_v.at[1, 'num']=7
df_v.at[2, 'num']=4
df_v.at[4, 'num']=3
df_v['category']='j0'
dfa=pd.concat([dfa, df_v],axis=0).reset_index(drop=True)

df_v.at[0, 'num']=2
df_v.at[1, 'num']=1
df_v.at[3, 'num']=1
df_v.at[4, 'num']=0
df_v['category']='j1'
df_v=df_v.sort_values(by=['num'], ascending=[True]).reset_index(drop=True)
dfa=pd.concat([dfa, df_v],axis=0).reset_index(drop=True)

df_v.at[0, 'num']=0
df_v.at[1, 'num']=0
df_v.at[2, 'num']=4
df_v.at[4, 'num']=2
df_v['category']='j2'
#df_v=df_v.iloc[:4]
df_v=df_v.sort_values(by=['num'], ascending=[True]).reset_index(drop=True)
dfa=pd.concat([dfa, df_v],axis=0).reset_index(drop=True)

df_v.at[0, 'num']=4
df_v.at[1, 'num']=8
df_v.at[3, 'num']=9
df_v.at[4, 'num']=2
df_v['category']='j3'
#df_v=df_v.iloc[:4]
df_v=df_v.sort_values(by=['num'], ascending=[True]).reset_index(drop=True)
dfa=pd.concat([dfa, df_v],axis=0).reset_index(drop=True)
#df_0['added']=vecC = [-6, 1,1, 2, -2]
#df_0['added1']=vecC = [-3, -3,-3, -2, -6]


fig0=plt.figure(figsize=(7,6), constrained_layout=True)
gs33 = fig0.add_gridspec(2, 3)
ax0 = fig0.add_subplot(gs33[0, :])
#f3_ax1.set_title('gs[0, :]')
ax1 = fig0.add_subplot(gs33[1, :])
#f3_ax2.set_title('gs[1, :-1]')

Bar(df_0=dfa, axA=ax0, bar_type='vertical');
Bar(df_0=dfa, axA=ax1, bar_type='horizontal');


ax0.set_title("the title of this image", y=1.3)
ax0.grid()
ax1.grid()
ax1.legend().remove()
plt.show()
plt.close('all')