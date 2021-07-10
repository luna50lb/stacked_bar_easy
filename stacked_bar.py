import numpy as np
from matplotlib import pyplot as plt

import matplotlib as mpl
import pandas as pd
import seaborn as sns

#mpl.style.use('seaborn-colorblind');
mpl.style.use('tableau-colorblind10')
CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber = '#F5B14C'


'''
df_0
columns = {field, num, category}

'''

class Bar:
    def __init__(self, df_0, axA, bar_type='vertical'):
        if df_0[ (df_0['num']<0) ].shape[0]>0:
            print('Error! negative values may exist in column num')
            raise ValueError;

        list_field_elements=df_0.sort_values(by=['field'], ascending=[True])['field'].unique().tolist()
        n_fields0=len( list_field_elements );
        y_offset0 = np.zeros( n_fields0 )

        x_offset0 = np.zeros( n_fields0 )
        #if df_0[].shape[0]>0:
        #    print('Error! ')

        list_category_elements=df_0['category'].unique().tolist();
        n_colours0=len(list_category_elements);
        if n_colours0>200:
            print('Error! Too many colours!')
            raise ValueError;

        j_counter=0
        for j_category in list_category_elements:
            df_j=pd.DataFrame([])
            df_j=df_0[df_0['category']==j_category]
            if df_j.shape[0]!=n_fields0:
                print('Warning! check df_j field numbers!')
                print('df_j=\n', df_j)
            df_j=df_j.sort_values(by=['field'], ascending=[True])
            if df_j['field'].values.tolist()!=list_field_elements:
                print('Error!, now fields=',df_j['field'].values.tolist(), ' while appropriate category=', list_field_elements )
                raise ValueError;
            #print('df_j=\n', df_j)
            j_colour=sns.color_palette(palette='husl', n_colors=n_colours0 )[j_counter]
            
            if bar_type=='vertical':
                axA.bar(x=df_j['field'].values.tolist(), height=df_j['num'].values.tolist(), width=0.5, bottom=y_offset0, align='center', label=j_category, color=[ j_colour ] * n_fields0  ) # 
                y_offset0=y_offset0 + df_j['num'].to_numpy()

            elif bar_type=='horizontal':
                axA.barh(y=df_j['field'].values.tolist(), width=df_j['num'].values.tolist(), height=0.5, left=x_offset0, align='center', label=j_category, color=[ j_colour ] * n_fields0  ) # 
                x_offset0=x_offset0 + df_j['num'].to_numpy()

            else:
                print('Error! check bar_type. now it is ', bar_type);
                raise ValueError;
                
            j_counter=j_counter+1
            #print('y offset=\n', y_offset0)
    
        #align{'center', 'edge'}, 
        #ax0.bar(x=df_0['field'].to_numpy(), height=df_0['added'].to_numpy(), width=0.5, bottom=0, align='center', color=[sns.color_palette(palette='husl', n_colors=df_0.shape[0] )[1]] * n_fields0 ) 
        #ax0.bar(x=df_0['field'].to_numpy(), height=df_0['added1'].to_numpy(), width=0.5, bottom=0, align='center', color=[sns.color_palette(palette='husl', n_colors=df_0.shape[0] )[2]] * n_fields0 ) 

        handles0, labels0 = axA.get_legend_handles_labels()
        print('handles', handles0)
        print('labels=', labels0)
        #ggz=ax0.legend(handles=handles0[1:], labels=labels0[1:], loc='upper left', fancybox=True, framealpha=0.35)

        axA.tick_params(axis='both', which='major', labelsize=16)
        axA.legend(handles=handles0, labels=labels0, fancybox=True, framealpha=0.15, ncol=4, bbox_to_anchor=(1,1.3)   ) # frameon=False

        #for jlg in ggz.legendHandles:
        #    jlg.set_linewidth(3);
        plt.setp(axA.get_legend().get_texts(), fontsize=16)



