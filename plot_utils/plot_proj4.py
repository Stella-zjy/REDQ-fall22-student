from quick_plot_helper import quick_plot

twocolordoulbe = ['tab:blue', 'tab:orange', 'tab:blue', 'tab:orange',]
twosoliddashed = ['dashed', 'dashed',  'solid', 'solid', ]
threecolordoulbe = ['tab:blue', 'tab:orange', 'tab:red', 'tab:blue', 'tab:orange', 'tab:red']
threesoliddashed = ['dashed', 'dashed', 'dashed', 'solid', 'solid', 'solid', ]
standard_6_colors = ('tab:red', 'tab:orange', 'tab:blue', 'tab:brown', 'tab:pink','tab:grey')

envs = ['Hopper-v3', 'HalfCheetah-v3']
# data_path = '../data/'
data_path = '/Users/stella/Documents/GitHub/REDQ-fall22-student/data4/'

standard_ys = ['AverageTestEpRet', 'AverageQ1Vals', 'AverageNormQBias', 'StdNormQBias', 'Time']

plot_proj4 = True
if plot_proj4:
    quick_plot(
        [
         'SAC UTD 1', 'SAC UTD 5', 'SAC UTD 1 with Reset', 'SAC UTD 5 with Reset'],
        [
            'exp_e300_q2_uf1_lr0.0003_g0.99_p0.995_ss5000_b64_h64_rmFalse',
            'exp_e300_q2_uf5_lr0.0003_g0.99_p0.995_ss5000_b64_h64_rmFalse',
            'exp_e300_q2_uf1_lr0.0003_g0.99_p0.995_ss5000_b64_h64_rmTrue',
            'exp_e300_q2_uf5_lr0.0003_g0.99_p0.995_ss5000_b64_h64_rmTrue',
        ],
        envs=envs,
        save_name='SAC_UTD',
        base_data_folder_path=data_path,
        y_value=standard_ys
    )

# if plot_proj4:
#     quick_plot(
#         [
#          'SAC UTD 1', 'SAC UTD 5'],
#         [
#             'exp_e300_q2_uf1_lr0.0003_g0.99_p0.995_ss5000_b64_h64_rmTrue',
#             'exp_e300_q2_uf5_lr0.0003_g0.99_p0.995_ss5000_b64_h64_rmTrue',
#         ],
#         envs=envs,
#         save_name='SAC_UTD_with_Reset',
#         base_data_folder_path=data_path,
#         y_value=standard_ys
#     )

