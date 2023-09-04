df_lim = df.select('_c0','_c1','_c2', '_c3', '_c4', '_c5', '_c6', '_c7', '_c8', '_c9', '_c10', '_c11', '_c12', '_c13')

old_names = ['_c0','_c1','_c2', '_c3', '_c4', '_c5', '_c6', '_c7', '_c8', '_c9', '_c10', '_c11', '_c12', '_c13']
new_names = ['loan_id','period','servicer_name', 'new_int_rt', 'act_endg_upb', 'loan_age', 'mths_remng', 'aj_mths_remng', 'dt_matr', 'cd_msa', 'delq_sts', 'flag_mod', 'cd_zero_bal', 'dt_zero_bal']
for old, new in zip(old_names, new_names):
    df_lim = df_lim.withColumnRenamed(old, new)
